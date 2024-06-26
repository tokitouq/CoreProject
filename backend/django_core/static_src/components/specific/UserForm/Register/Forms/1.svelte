<script lang="ts">
    import CoreText from "$icons/CoreText/Index.svelte";
    import Tick from "$icons/Tick/Index.svelte";
    import Info from "$icons/Info/Index.svelte";
    import ArrowUpRight from "$icons/ArrowUpRight/Index.svelte";
    import Arrow from "$icons/Arrow/Index.svelte";

    import { beforeUpdate, createEventDispatcher } from "svelte";
    import Markdown from "$components/minor/Markdown/Index.svelte";
    import * as _ from "lodash-es";
    import { z } from "zod";
    import { handle_input } from "../../functions/handle_input";
    import { zxcvbn, zxcvbnOptions, type OptionsType } from "@zxcvbn-ts/core";
    import { cn } from "$functions/classname";
    import { reverse } from "$functions/urls";
    import { get_csrf_token } from "$functions/get_csrf_token";
    import { FETCH_TIMEOUT } from "$constants/fetch";
    import { enhance_anchor } from "$functions/anchor_enhancements";
    import { autofocus } from "$functions/autofocus";

    export let pages_state: [{ email: string }, { password: string }, { confirm_password: string }];

    let combined_state: { [key: string]: string } | null = null;
    $: combined_state = Object.assign({}, ...pages_state);

    let confirm_password_element: HTMLInputElement | null = null;

    beforeUpdate(async () => {
        const zxcvbnCommonPackage = await import("@zxcvbn-ts/language-common");
        const zxcvbnEnPackage = await import("@zxcvbn-ts/language-en");
        const zxcvbnCsPackage = await import("@zxcvbn-ts/language-cs");
        const zxcvbnDePackage = await import("@zxcvbn-ts/language-de");
        const zxcvbnEsEsPackage = await import("@zxcvbn-ts/language-es-es");
        const zxcvbnFiPackage = await import("@zxcvbn-ts/language-fi");
        const zxcvbnFrPackage = await import("@zxcvbn-ts/language-fr");
        const zxcvbnIdPackage = await import("@zxcvbn-ts/language-id");
        const zxcvbnItPackage = await import("@zxcvbn-ts/language-it");
        const zxcvbnJaPackage = await import("@zxcvbn-ts/language-ja");
        const zxcvbnNlBePackage = await import("@zxcvbn-ts/language-nl-be");
        const zxcvbnPlPackage = await import("@zxcvbn-ts/language-pl");
        const zxcvbnPtBrPackage = await import("@zxcvbn-ts/language-pt-br");

        const options: OptionsType = {
            translations: zxcvbnEnPackage.translations,
            graphs: zxcvbnCommonPackage.adjacencyGraphs,
            dictionary: {
                ...zxcvbnCommonPackage.dictionary,
                ...zxcvbnCsPackage.dictionary,
                ...zxcvbnDePackage.dictionary,
                ...zxcvbnEsEsPackage.dictionary,
                ...zxcvbnFiPackage.dictionary,
                ...zxcvbnFrPackage.dictionary,
                ...zxcvbnIdPackage.dictionary,
                ...zxcvbnItPackage.dictionary,
                ...zxcvbnJaPackage.dictionary,
                ...zxcvbnNlBePackage.dictionary,
                ...zxcvbnPlPackage.dictionary,
                ...zxcvbnPtBrPackage.dictionary,
                ...zxcvbnEnPackage.dictionary,

                // Check inputs
                userInputs: [password.value, email.value, confirm_password.value]
            },
            useLevenshteinDistance: true
        };

        zxcvbnOptions.setOptions(options);
    });

    let email = {
            value: combined_state?.email ?? "",
            error: new Array<string>()
        },
        password = {
            value: combined_state?.password ?? "",
            error: new Array<string>()
        },
        confirm_password = {
            value: combined_state?.confirm_password ?? "",
            error: new Array<string>()
        };

    let password_strength = 0;
    let form_is_submitable = false;

    function check_if_form_is_submitable() {
        form_is_submitable = [email, password, confirm_password].every((field) => {
            return field.value && _.isEmpty(field.error);
        });
    }

    const dispatch = createEventDispatcher();

    const password_error_mapping: { [key: string]: string } = {
        atleast_8: "minimum 8 characters",
        missing_one_special_character: "minimum 1 special character",
        missing_one_number: "minimum 1 number",
        missing_one_upper_or_lowercase: "minimum 1 lower-case or upper-case character"
    };

    // Bindings

    function handle_submit() {
        if (form_is_submitable) {
            dispatch("submit", {
                email: email.value,
                password: password.value
            });
        }
        // Show some errors here
    }

    const handle_email_input = async (event: Event) => {
            handle_input({ event: event, schema: z.string().email("Please enter a valid email address"), error_field: email });
            if (_.isEmpty(email.error)) {
                const res = await fetch(reverse("email-validity-endpoint"), {
                    method: "POST",
                    headers: {
                        Accept: "application/json",
                        "Content-Type": "application/json",
                        "X-CSRFToken": get_csrf_token()
                    },
                    signal: AbortSignal.timeout(FETCH_TIMEOUT),
                    body: JSON.stringify({
                        email: email.value
                    })
                });

                // 302 = username found
                // 404 = not found

                switch (Number(res.status)) {
                    case 302:
                        email.error = [...email.error, `Email **${email.value}** is already taken. Perhaps you want to **[login](${reverse("login_view")})**`];
                        break;
                    case 404:
                        break;
                    default:
                        throw new Error("Not Implemented");
                }
            }
        },
        handle_password_input = (event: Event) => {
            if (password.value) {
                handle_input({
                    event: event,
                    schema: z
                        .string()
                        .min(8, "atleast_8")
                        .refine((val) => /(?=.*[!@#$%^&*()_+|~\-=?;:'",.<>{}[\]\\/])/.test(val), "missing_one_special_character")
                        .refine((val) => /(?=.*\d)/.test(val), "missing_one_number")
                        .refine((val) => /(?=.*[A-Z])|(?=.*[a-z])/.test(val), "missing_one_upper_or_lowercase"),
                    error_field: password
                });
                password_strength = zxcvbn(password.value).score;
            } else {
                password_strength = password.error.length = 0;
            }
            if (confirm_password.value) {
                const event = new Event("input", {});
                confirm_password_element?.dispatchEvent(event);
            }
        },
        handle_confirm_password = (event: Event) => {
            handle_input({
                event: event,
                schema: z.string(),
                error_field: confirm_password
            });
            if (confirm_password.value !== password.value) {
                confirm_password.error = [...confirm_password.error, `**Password** and **Confirm Password** must match`];
            }
        };
</script>

<form
    use:autofocus
    on:submit|preventDefault={handle_submit}
    class="flex h-full flex-col justify-between"
>
    <div class="flex flex-col items-start">
        <span class="text-lg font-bold uppercase leading-none tracking-widest text-warning md:text-[1.25vw]">
            create your
            <CoreText />
            account
        </span>
        <button
            on:click={() => window.history.back()}
            class="btn btn-link h-max min-h-full p-0 md:gap-[0.5vw] md:text-[1.25vw]"
        >
            <Arrow
                variant="fill"
                class="-rotate-90 md:size-[1.25vw]"
            />
            Go Back
        </button>
    </div>
    <div class="flex flex-col gap-5 md:gap-[1.5vw]">
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <label
                for="email"
                class="mt-4 text-lg font-semibold leading-none md:mt-[1.1vw] md:text-[1.1vw]"
            >
                Email:
            </label>
            <input
                bind:value={email.value}
                on:input|preventDefault={handle_email_input}
                on:input={check_if_form_is_submitable}
                placeholder="Email address"
                class="w-full rounded-xl border-2 border-neutral bg-transparent p-3.5 px-5 text-base font-medium leading-none outline-none !ring-0 transition-colors duration-300 placeholder:text-white/50 focus:border-primary md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1.1vw] md:py-[0.8vw] md:text-[1.1vw]"
            />
            <div class="flex items-center gap-2 text-xs leading-none md:gap-[0.5vw] md:text-[0.75vw]">
                <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                {#if _.isEmpty(email.error) || _.isEmpty(email.value)}
                    <span>we’ll send you a verification email, so please ensure it’s active</span>
                {:else}
                    <span class="text-error">
                        <Markdown
                            markdown={email.error.join("")}
                            unsafe={true}
                        ></Markdown>
                    </span>
                {/if}
            </div>
        </div>
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <label
                for="password"
                class="text-lg font-semibold leading-none md:text-[1.1vw]"
            >
                Password:
            </label>
            <input
                bind:value={password.value}
                on:input={handle_password_input}
                on:input={check_if_form_is_submitable}
                placeholder="Password"
                class="w-full rounded-xl border-2 border-neutral bg-transparent p-3.5 px-5 text-base font-medium leading-none outline-none !ring-0 transition-colors duration-300 placeholder:text-white/50 focus:border-primary md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1.1vw] md:py-[0.8vw] md:text-[1.1vw]"
            />
            <div class="flex flex-col">
                <div class="grid grid-cols-4 gap-[1.5vw] md:gap-[0.75vw]">
                    {#each Array(password_strength) as _, index}
                        {@const backgrounds = ["bg-primary opacity-60", "bg-primary opacity-70", "bg-primary opacity-80", "bg-primary opacity-90"]}
                        <span class={cn(backgrounds[index], "col-span-1 h-[1.75vw] w-full rounded-[0.5vw] md:h-[0.625vw] md:rounded-[0.1875vw]")} />
                    {/each}
                    {#each Array(4 - password_strength) as _}
                        <span class="h-[1.75vw] rounded-[0.5vw] border-white/25 transition-colors md:h-[0.75vw] md:rounded-[0.1875vw] md:border-[0.15vw]"></span>
                    {/each}
                </div>

                <div class="mt-3 md:mt-[1.25vw]">
                    <span class="text-surface-50 text-sm font-semibold uppercase leading-none tracking-wider md:text-[1vw]">must contain</span>

                    <div class="flex flex-col gap-1 md:mt-[0.5vw] md:gap-[0.3vw]">
                        {#each Object.entries(password_error_mapping) as item}
                            {@const key = item[0]}
                            {@const value = item[1]}

                            <div class="flex items-center gap-2 md:gap-[0.5vw]">
                                {#if (_.isEmpty(password.error) && _.isEmpty(password.value)) || (password.value && password.error.includes(key))}
                                    <div>
                                        <Tick class="w-3 text-primary opacity-30 transition-opacity md:w-[1vw]" />
                                    </div>
                                {:else}
                                    <!-- Filled tick  -->
                                    <div>
                                        <Tick class="w-3 text-primary transition-opacity md:w-[1vw]" />
                                    </div>
                                {/if}

                                <span class="text-surface-300 text-[0.7rem] leading-none md:text-[0.75vw]">{value}</span>
                            </div>
                        {/each}
                    </div>
                </div>
            </div>
        </div>
        <div class="flex flex-col gap-[0.3rem] md:gap-[0.5vw]">
            <label
                for="confirm-password"
                class="text-lg font-semibold leading-none md:text-[1.1vw]"
            >
                Confirm Password:
            </label>
            <input
                bind:value={confirm_password.value}
                bind:this={confirm_password_element}
                on:input={handle_confirm_password}
                on:input={check_if_form_is_submitable}
                placeholder="Confirm Password"
                class="w-full rounded-xl border-2 border-neutral bg-transparent p-3.5 px-5 text-base font-medium leading-none outline-none !ring-0 transition-colors duration-300 placeholder:text-white/50 focus:border-primary md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1.1vw] md:py-[0.8vw] md:text-[1.1vw]"
            />
            <div class="flex items-center gap-2 text-xs leading-none md:gap-[0.5vw] md:text-[0.75vw]">
                {#if _.isEmpty(confirm_password.error)}
                    <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                    <span>Please make sure you enter the same password in both fields</span>
                {:else}
                    <Info class="w-3 opacity-70 md:w-[0.9vw]" />

                    <Markdown
                        class="text-error"
                        markdown={confirm_password.error.join("")}
                    />
                {/if}
            </div>
        </div>
    </div>
    <div class="flex items-center justify-between">
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <span class="text-surface-100 text-xs leading-none md:text-[0.75vw]">Already have an account?</span>
            <a
                href={reverse("login_view")}
                use:enhance_anchor={{ verb: "GET", target: "body" }}
                class="btn btn-link size-max min-h-full p-0 text-base leading-none md:text-[1.1vw]"
            >
                Login
            </a>
        </div>
        <button
            type="submit"
            class:btn-disabled={!form_is_submitable}
            class={cn(`btn btn-primary h-max min-h-max rounded-lg p-4 text-base font-semibold leading-none text-accent md:rounded-[0.75vw] md:px-[1.25vw] md:py-[1vw] md:text-[0.95vw]`)}
        >
            <span>Continue</span>
            <ArrowUpRight class="w-4 rotate-45 md:w-[1vw]" />
        </button>
    </div>
</form>

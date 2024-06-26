<script lang="ts">
    import { search_modal_state } from "./store";
    import ScrollArea from "$components/minor/ScrollArea/Index.svelte";
    import { reverse } from "$functions/urls";
    import { Anime } from "../../../types/anime";
    import { FormatDate } from "$functions/format_date";
    import * as _ from "lodash-es";
    // Icon imports
    import Search from "$icons/Search/Index.svelte";
    import Cross from "$icons/Cross/Index.svelte";
    import Circle from "$icons/Circle/Index.svelte";
    import { get_csrf_token } from "$functions/get_csrf_token";
    import { FETCH_TIMEOUT } from "$constants/fetch";
    import { user_authenticated } from "$stores/user";
    import { cn } from "$functions/classname";
    import { enhance_anchor } from "$functions/anchor_enhancements";

    let active_index = 0,
        active_core: "anime" | "manga" | "sound" = "anime",
        search_query = "";

    // Bindings
    let dialog_element: HTMLDialogElement | null = null,
        anime_search_results_container_element: HTMLDivElement | null = null;

    const handle_search_key_down = async (e: KeyboardEvent) => {
            if (!dialog_element?.open) return;
        },
        handle_search_key_press = async (e: KeyboardEvent) => {
            if (e.key.toLowerCase() === "enter") return;
            active_index = 0;
        },
        handle_core_mouse_enter = async (core: typeof active_core, index: number) => {
            active_index = index;
            active_core = core;
        },
        handle_input = async () => {
            search_promise = search_query === "" ? null : get_anime_with_serach_parameters();
        },
        handle_global_input = async (e: KeyboardEvent) => {
            const search_results = await search_promise;
            if (_.isNull(search_results)) return;

            switch (e.key.toLowerCase()) {
                case "arrowdown":
                    active_index = (active_index + 1) % search_results.length;
                    break;
                case "arrowup":
                    active_index = (active_index - 1 + search_results.length) % search_results.length;
                    break;
                // do tab logic of switching core
                // case "tab":
                //     break;
                case "enter":
                    const active_anime_element = anime_search_results_container_element?.children[active_index] as HTMLAnchorElement;
                    active_anime_element.click();
                    break;
                default:
                    break;
            }
        };

    const get_anime_with_serach_parameters = async () => {
        const headers: { [key: string]: string } = {};

        if ($user_authenticated) {
            headers["X-CSRFToken"] = get_csrf_token();
        }
        const res = await fetch(reverse(`anime-list`) + "?" + new URLSearchParams({ name: search_query }), {
            method: "GET",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
                "X-CSRFToken": get_csrf_token()
            },
            signal: AbortSignal.timeout(FETCH_TIMEOUT)
        });
        const json = await res.json();
        if (res.ok) {
            return json["results"] as Array<Anime>;
        } else {
            throw new Error("Something is wrong from the backend");
        }
    };
    let search_promise: Promise<Anime[]> | null = null;

    search_modal_state.subscribe((val) => {
        if (val) {
            dialog_element?.showModal();
            search_modal_state.set(false);
        }
    });
</script>

<svelte:window on:keyup={(event) => dialog_element?.open && handle_global_input(event)} />
<dialog
    class="modal modal-bottom bg-secondary/50 backdrop-blur"
    bind:this={dialog_element}
>
    <div class="modal-box max-h-max flex w-max mx-auto flex-col bg-secondary items-center md:p-[2vw]">
        <form
            on:submit|preventDefault
            class="relative flex w-[40vw] items-center"
        >
            <button
                class="btn absolute left-[1.25vw] min-h-max border-none !bg-transparent p-0"
                aria-label="Search"
            >
                <Search style="width: 1.25vw;" />
            </button>
            <input
                bind:value={search_query}
                on:input={handle_input}
                on:keydown={handle_search_key_down}
                on:keypress={handle_search_key_press}
                type="text"
                placeholder="Search for animes, mangas and musics"
                class="w-full rounded-[0.625vw] border-none bg-neutral pl-[3.50vw] p-[1vw] text-[1.1vw] font-semibold text-white shadow-lg !ring-0 placeholder:font-medium placeholder:text-accent/75 outline-none"
            />

            <button
                type="button"
                aria-label="Clear"
                class="btn absolute right-[1.25vw] min-h-max border-none !bg-transparent p-0"
                on:click={() => (search_query = "")}
            >
                <Cross style="width: 1.5vw; opacity: 0.7;" />
            </button>
        </form>

        <div class="mt-[1.5vw] flex gap-[4vw]">
            <div>
                <span class="text-surface-50 text-[1.2vw] font-semibold">anime</span>
                <ScrollArea
                    offset_scrollbar
                    gradient_mask
                    parent_class="md:mt-[0.2vw] md:h-[30vw] md:w-[20vw]"
                    class="size-full"
                >
                    {#if search_promise}
                        {#await search_promise}
                            <div class="grid h-full place-items-center">
                                <span class="loading loading-ring loading-lg"></span>
                            </div>
                        {:then results}
                            {#if !_.isEmpty(results)}
                                <div bind:this={anime_search_results_container_element}>
                                    {#each results as item, index}
                                        {@const is_active = active_core === "anime" && active_index === index}
                                        {@const mapping = [
                                            {
                                                value: `TV`,
                                                class: `flex items-center gap-[0.3vw]`
                                            },
                                            {
                                                value: item.episode_count ? `${item.episode_count} eps` : null,
                                                class: "flex items-center gap-[0.3vw]"
                                            },
                                            {
                                                value: item.aired_from ? new FormatDate(item.aired_from).format_to_human_readable_form : null,
                                                class: "flex items-center gap-[0.3vw]"
                                            }
                                        ]}
                                        <a
                                            use:enhance_anchor={{ verb: "GET", target: "#page" }}
                                            on:mouseenter={() => handle_core_mouse_enter("anime", index)}
                                            on:click={() => dialog_element?.close()}
                                            href={reverse("anime_info_view", "mal", String(item.mal_id))}
                                            class={cn(is_active && "bg-neutral/50", "flex w-full auto-rows-max items-center gap-[1vw] rounded-[0.7vw] p-[0.8vw] transition duration-200 hover:bg-neutral/75")}
                                        >
                                            <img
                                                src={item.cover}
                                                alt={search_query}
                                                class="size-[3.5vw] flex-shrink-0 rounded-[0.5vw] object-cover"
                                            />
                                            <div class="flex flex-col leading-none md:gap-[0.5vw]">
                                                <span class="text-[1.1vw] line-clamp-1 font-semibold leading-none text-white">
                                                    {item.name}
                                                    <span class="text-accent/50 font-medium">({item.name_japanese})</span>
                                                </span>
                                                <div class="flex items-center md:gap-[0.35vw] md:text-[0.9vw]">
                                                    {#each mapping as item, index}
                                                        {@const show_dot = index !== mapping.length - 1}

                                                        {#if !_.isNull(item.value)}
                                                            <span class={item.class}>{item.value}</span>
                                                            {#if show_dot}
                                                                <Circle class="md:w-[0.25vw]" />
                                                            {/if}
                                                        {/if}
                                                    {/each}
                                                </div>
                                            </div>
                                        </a>
                                    {/each}
                                </div>
                            {:else}
                                <div class="flex h-full flex-col items-center justify-center gap-[0.2vw] text-[1.1vw]">
                                    <span class="font-medium leading-none">No match found!</span>
                                    <span class="text-center font-semibold leading-none text-error">Couldn't find animes with: "{search_query}"</span>
                                </div>
                            {/if}
                        {:catch error}
                            <div class="flex h-full flex-col items-center justify-center gap-[0.2vw] text-[1.1vw]">
                                <span class="font-medium leading-none">Oh no, something is wrong!</span>
                                <span class="text-center font-semibold leading-none text-error">{@html error}</span>
                            </div>
                        {/await}
                    {:else}
                        <div class="flex h-full flex-col items-center justify-center gap-[0.2vw] text-[1.1vw]">
                            <span class="font-medium leading-none">Search Away</span>
                            <span class="font-semibold leading-none">"Find Your Anime Bliss"</span>
                        </div>
                    {/if}
                </ScrollArea>
            </div>

            <div>
                <span class="text-surface-50 text-[1.2vw] font-semibold">manga</span>
                <div class="bg-surface-400 mt-[0.2vw] h-[30vw] w-[21.875vw] rounded-[0.75vw] shadow-lg">
                    <div class="flex h-full flex-col items-center justify-center gap-[0.2vw] text-[1.1vw]">
                        <span class="font-medium leading-none">mangacore integration</span>
                        <span class="font-semibold leading-none">coming soon</span>
                    </div>
                </div>
            </div>

            <div>
                <span class="text-surface-50 text-[1.2vw] font-semibold">music</span>
                <div class="bg-surface-400 mt-[0.2vw] h-[30vw] w-[21.875vw] rounded-[0.75vw] shadow-lg">
                    <div class="flex h-full flex-col items-center justify-center gap-[0.2vw] text-[1.1vw]">
                        <span class="font-medium leading-none">soundcore integration</span>
                        <span class="font-semibold leading-none">coming soon</span>
                    </div>
                </div>
            </div>
        </div>

        <p class="mt-[2vw] text-[0.8vw]">
            <b>Note:</b>
            Navigate through animes, mangas and sounds with
            <kbd class="kbd kbd-xs text-[0.8vw] rounded-full">▲</kbd>
            <kbd class="kbd kbd-xs text-[0.8vw] rounded-full">▼</kbd>
            and
            <kbd class="kbd kbd-xs text-[0.8vw] rounded-full">Tab</kbd>
            keys.
        </p>
    </div>
    <form
        method="dialog"
        class="modal-backdrop"
    >
        <button>close</button>
    </form>
</dialog>

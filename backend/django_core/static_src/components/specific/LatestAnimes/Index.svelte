<script lang="ts">
    import JSON5 from "json5";

    import Chevron from "$icons/Chevron/Index.svelte";
    import Circle from "$icons/Circle/Index.svelte";
    import Play from "$icons/Play/Index.svelte";
    import Info from "$icons/Info/Index.svelte";
    import Edit from "$icons/Edit/Index.svelte";

    import ScrollArea from "$components/minor/ScrollArea/Index.svelte";

    import { swipe } from "svelte-gestures";
    import { Timer as EasyTimer } from "easytimer.js";
    import { tweened } from "svelte/motion";
    import { FormatDate } from "$functions/format_date";
    import { blur } from "svelte/transition";
    import { enhance_anchor } from "$functions/anchor_enhancements";

    type LatestAnimes = {
        id: number;
        name: string;
        type: string;
        episodes: number;
        status: string;
        release_date: string;
        studio: string;
        genres: string[];
        synopsis: string;
        image: string;
    }[];

    export let latest_animes: string;
    // parse to JSON
    const latest_animes_data = JSON5.parse(latest_animes) satisfies LatestAnimes;

    const slider_delay = 10,
        timer = new EasyTimer({
            target: {
                seconds: slider_delay
            },
            precision: "secondTenths"
        }),
        slide_buttons = [
            { background: "bg-accent", border: "border-accent" },
            { background: "bg-info", border: "border-info" },
            { background: "bg-warning", border: "border-warning" },
            { background: "bg-white", border: "border-white" },
            { background: "bg-primary", border: "border-primary" },
            { background: "bg-error", border: "border-error" }
        ];

    /* Slider codes */
    let main_hero_slider_element: HTMLElement,
        main_hero_slide_active_index = 0;

    const add_one_to_main_hero_slide_active_index = () => {
            if (main_hero_slide_active_index + 1 === latest_animes_data.length) {
                main_hero_slide_active_index = 0;
                return;
            }
            main_hero_slide_active_index += 1;
        },
        minus_one_to_main_hero_slide_active_index = () => {
            if (main_hero_slide_active_index === 0) {
                main_hero_slide_active_index = latest_animes_data.length - 1;
                return;
            }
            main_hero_slide_active_index -= 1;
        },
        swipe_handler = (event: CustomEvent) => {
            const direction = event.detail.direction;
            timer.reset();

            if (direction === "left") {
                add_one_to_main_hero_slide_active_index();
            } else if (direction === "right") {
                minus_one_to_main_hero_slide_active_index();
            }
        };

    // Progress bar code //
    let progress_value = 0,
        tweened_progress_value = tweened(progress_value);
    $: tweened_progress_value.set(progress_value);
    timer.start();
    timer.on("targetAchieved", () => {
        // change slider
        add_one_to_main_hero_slide_active_index();
        timer.reset();
    });

    timer.on("secondTenthsUpdated", () => {
        const time = timer.getTotalTimeValues().secondTenths,
            value = (100 / slider_delay) * (time / 10);

        progress_value = value;
    });
</script>

<svelte:head>
    {#each latest_animes_data as anime}
        <link
            rel="prefetch"
            href={anime.image}
        />
    {/each}
</svelte:head>

<div
    class="relative h-96 w-full md:h-[27.875vw] md:w-[42.1875vw]"
    use:swipe={{ timeframe: 300, minSwipeDistance: 100, touchAction: "pan-y" }}
    on:swipe={swipe_handler}
    bind:this={main_hero_slider_element}
>
    {#each latest_animes_data as anime, index}
        {@const active = index === main_hero_slide_active_index}
        {@const formated_aired_on = new FormatDate(anime.release_date).format_to_season}

        {#if active}
            <anime-slides
                role="presentation"
                class="absolute inset-0 md:bottom-[2vw]"
                transition:blur
                on:mouseenter={() => {
                    timer?.pause();
                }}
                on:mouseleave={() => {
                    timer?.start();
                }}
                on:touchstart={() => {
                    timer?.pause();
                }}
                on:touchend={() => {
                    timer?.start();
                }}
            >
                <img
                    src={anime.image}
                    alt=""
                    class="absolute h-full w-full object-cover object-center md:rounded-t-[0.875vw]"
                />

                <div class="md:to-surface-900/25 absolute inset-0 bg-gradient-to-t from-secondary/90 to-secondary/50" />
                <div class="from-surface-900 to-surface-900/25 md:from-surface-900/50 absolute inset-0 hidden bg-gradient-to-r md:flex" />

                <div class="absolute flex flex-col bottom-0 md:left-0 p-4 md:px-[3.75vw] md:py-[2.625vw]">
                    <span class="text-3xl font-bold text-white md:text-[2vw] md:leading-[2.375vw]">{anime.name}</span>
                    <div class="flex flex-wrap items-center gap-2 py-2 text-xs font-semibold text-white/90 md:gap-[0.65vw] md:pb-0 md:pt-[0.5vw] md:text-[0.9375vw]">
                        <span class="leading-[1.125vw]">
                            {anime.type}
                        </span>
                        <Circle class="w-1 opacity-75 md:w-[0.25vw]" />
                        <span class="leading-[1.125vw]">
                            {anime.episodes} eps
                        </span>
                        <Circle class="w-1 opacity-75 md:w-[0.25vw]" />
                        <span class="leading-[1.125vw]">Completed</span>
                        <Circle class="w-1 opacity-75 md:w-[0.25vw]" />
                        <span class="capitalize leading-[1.125vw]">
                            {formated_aired_on}
                        </span>
                        <Circle class="w-1 opacity-75 md:w-[0.25vw]" />
                        <span class="leading-[1.125vw]">
                            {anime.studio}
                        </span>
                        <div>
                            <anime-genres class="flex gap-2 pb-2 pt-3 md:gap-[0.5vw] md:pt-0">
                                {#each anime.genres as genre}
                                    <span class="rounded-lg bg-secondary p-2 px-3 text-xs capitalize leading-none md:rounded-[0.35vw] md:px-[0.75vw] md:py-[0.4vw] md:text-[0.75vw] md:font-semibold">
                                        {genre}
                                    </span>
                                {/each}
                            </anime-genres>

                            <ScrollArea
                                gradient_mask
                                offset_scrollbar
                                parent_class="max-h-16 md:max-h-[6vw] hidden md:flex"
                                class="text-surface-200 text-xs font-medium leading-4 md:pt-[0.75vw] md:text-[0.85vw] md:leading-[1.1vw]"
                            >
                                {anime.synopsis}
                            </ScrollArea>

                            <div class="mb-2 mt-5 flex items-center gap-2 md:mb-0 md:mt-[1.5vw] md:gap-[1vw]">
                                <a
                                    href="mal/{anime.id}/episode/1"
                                    use:enhance_anchor={{ verb: "GET", target: "#page" }}
                                    class="btn btn-warning flex h-max min-h-max justify-center gap-2 rounded-xl px-6 py-4 text-base font-bold leading-none text-secondary md:gap-[0.5vw] md:rounded-[0.625vw] md:px-[1.25vw] md:py-[1vw] md:text-[0.875vw]"
                                >
                                    <Play class="text-surface-900 w-4 md:w-[1vw]" />
                                    <span>Ep 1</span>
                                </a>
                                <a
                                    href="mal/{anime.id}"
                                    use:enhance_anchor={{ verb: "GET", target: "#page" }}
                                    class="btn btn-secondary flex h-max min-h-max items-center justify-center rounded-xl px-6 py-4 text-base font-semibold leading-none md:gap-[0.5vw] md:rounded-[0.5vw] md:px-[1.25vw] md:py-[1vw] md:text-[0.875vw] md:font-bold"
                                >
                                    <Info class="text-surface-50 w-5 md:w-[1.25vw]" />
                                    <span>Details</span>
                                </a>
                                <button
                                    class="bg-surface-900 text-surface-50s btn btn-secondary h-max min-h-max rounded-xl p-4 text-[3vw] font-bold leading-none md:rounded-[0.5vw] md:p-[0.9vw] md:text-[0.875vw]"
                                >
                                    <Edit class="text-surface-50 w-4 md:w-[1.25vw]" />
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </anime-slides>
        {/if}
    {/each}

    <div class="absolute bottom-0 flex w-full flex-col">
        <div
            class="h-[0.2rem] bg-warning md:h-[0.145vw] {slide_buttons[main_hero_slide_active_index].background}"
            style="width: {$tweened_progress_value}%;"
        />

        <div class="hidden w-full grid-cols-6 gap-[0.9375vw] md:mt-[1.25vw] md:grid">
            {#each latest_animes_data as _, index}
                <button
                    class="col-span-1 h-[0.625vw] w-full rounded-[0.1875vw] border-[0.15vw] {slide_buttons[index].border} hover:border-surface-50/50 transition duration-300 {index ===
                    main_hero_slide_active_index
                        ? slide_buttons[index].background
                        : ''}"
                    on:click={() => {
                        timer?.reset();
                        timer?.start();
                        main_hero_slide_active_index = index;
                    }}
                />
            {/each}
        </div>
    </div>

    <button
        class="btn btn-primary absolute -left-[1vw] top-[12vw] z-20 hidden h-[2.25vw] min-h-max w-[2.25vw] rounded-[0.375vw] p-0 text-accent md:flex"
        on:click={() => {
            timer?.reset();
            timer?.start();
            minus_one_to_main_hero_slide_active_index();
        }}
    >
        <Chevron class="w-[1.25vw] rotate-90" />
    </button>
    <button
        class="bg-secondary-800 btn btn-primary absolute -right-[1vw] top-[12vw] z-20 hidden h-[2.25vw] min-h-max w-[2.25vw] rounded-[0.375vw] p-0 text-accent md:flex"
        on:click={async () => {
            timer?.reset();
            timer?.start();
            add_one_to_main_hero_slide_active_index();
        }}
    >
        <Chevron class="w-[1.25vw] -rotate-90" />
    </button>
</div>

<script lang="ts">
    import JSON5 from "json5";

    type IAnime = {
        name: string;
        image: string;
        status: string;
        current_ep: string;
        total_ep: string;
        synopsis: string;
        studio: string;
        genres: string[];
    }[];

    export let my_anime_list: string;
    // parse to JSON
    const my_anime_list_data = JSON5.parse(my_anime_list) satisfies IAnime;

    // Pass styles
    export let dropdown_class: string;

    import Dot from "$icons/Dot/Index.svelte";
    import ScrollArea from "$components/minor/ScrollArea/Index.svelte";
    import { cn } from "$functions/classname";
    import Star from "$icons/Star/Index.svelte";
    import Circle from "$icons/Circle/Index.svelte";
    import Play from "$icons/Play/Index.svelte";
    import Info from "$icons/Info/Index.svelte";
    import { enhance_anchor } from "$functions/anchor_enhancements";
    import HoverExpand from "$components/minor/HoverExpand/Index.svelte";

    let main_element: HTMLElement;

    // Styles
    let style_left: string;

    // Both of these functions require that parentElement is not changed
    // Please tatoo dont change the position of the element
    function calculate_style() {
        style_left = window.getComputedStyle(main_element).width;
    }
</script>

{#each my_anime_list_data as anime}
    <div
        class="dropdown dropdown-hover w-full"
        bind:this={main_element}
    >
        <a
            on:mouseenter|preventDefault={() => {
                calculate_style();
            }}
            href="mal/1"
            class="relative w-full"
            tabindex="0"
            aria-expanded={false}
        >
            <img
                class="w-full h-44 rounded-lg object-cover object-center md:h-[15vw] md:rounded-[0.75vw] md:rounded-b-none"
                src={anime.image}
                alt={anime.name}
                loading="lazy"
            />
            <div class="flex flex-col gap-1 pt-2 md:gap-[0.35vw] md:p-[1vw] md:bg-neutral/50 md:rounded-b-[0.75vw]">
                <HoverExpand
                    class="line-clamp-1 w-full text-start text-sm font-semibold text-accent md:line-clamp-none md:text-[1vw] md:leading-[1.35vw]"
                    height="md:max-h-[1.35vw] hover:max-h-[10vw]"
                >
                    {anime.name}
                </HoverExpand>
                <div class="text-surface-50 flex items-center gap-2 text-xs leading-none md:gap-[0.5vw] md:text-[0.8vw]">
                    <span class="hidden capitalize md:flex">
                        {anime.status}
                    </span>
                    <Dot class="hidden opacity-75 md:flex md:w-[0.25vw]" />
                    <span>
                        {`${anime.current_ep}/${anime.total_ep}`}
                    </span>
                </div>
            </div>
        </a>

        <button
            tabindex="0"
            class={cn(dropdown_class, "dropdown-content top-0 z-10 hidden flex-col leading-none md:flex md:w-[20vw]")}
            style="left:{style_left};"
        >
            <div class="flex flex-col bg-neutral text-start md:gap-[0.35vw] md:rounded-[0.75vw] md:rounded-t-[0.3vw] md:p-[1vw]">
                <anime-name class="font-semibold text-accent md:text-[1vw] md:leading-[1.25vw]">
                    {anime.name}
                </anime-name>
                <div class="text-surface-50 flex w-full items-center md:gap-[0.35vw] md:text-[0.8vw]">
                    <rating class="flex items-center md:gap-[0.5vw]">
                        <Star class="md:w-[0.9vw]" />
                        <span class="text-surface-50 leading-none md:text-[0.8vw]">4.5 rating</span>
                    </rating>
                    <Circle class="w-1 md:w-[0.25vw]" />
                    <anime-type>TV</anime-type>
                    <Circle class="w-1 md:w-[0.25vw]" />
                    <episodes-count>
                        {anime.total_ep} episdoes
                    </episodes-count>
                </div>
                <studio class="text-surface-50 md:text-[0.75vw]">
                    <span>{anime.studio}</span>
                </studio>
                <genres class="flex items-center md:my-[0.35vw] md:gap-[0.5vw]">
                    {#each anime.genres as genre}
                        <genre class="capitalize bg-warning font-semibold leading-none text-black md:rounded-[0.25vw] md:px-[0.6vw] md:py-[0.3vw] md:text-[0.8vw]">
                            {genre}
                        </genre>
                    {/each}
                </genres>
                <ScrollArea
                    gradient_mask={true}
                    parent_class="md:max-h-[4vw]"
                    class="text-surface-50 md:text-[0.8vw] md:leading-[1vw]"
                >
                    {anime.synopsis}
                </ScrollArea>
                <div class="divider md:m-0 md:before:h-[0.15vw] md:after:h-[0.15vw]"></div>
                <options class="flex items-center md:gap-[0.5vw]">
                    <a
                        use:enhance_anchor={{ verb: "GET", target: "#page" }}
                        href="/anime/mal/1/episode/4"
                        class="btn btn-primary h-[2.75vw] min-h-full flex-1 leading-none text-accent md:rounded-[0.5vw]"
                    >
                        <Play class="md:w-[0.9vw]" />
                        <span class="font-semibold md:text-[0.9vw]">
                            Continue Ep
                            {anime.current_ep}
                        </span>
                    </a>
                    <a
                        use:enhance_anchor={{ verb: "GET", target: "#page" }}
                        href="/anime/mal/1"
                        class="btn btn-square h-[2.75vw] min-h-full p-0 leading-none md:rounded-[0.5vw]"
                    >
                        <Info class="md:w-[1.2vw]" />
                    </a>
                </options>
            </div>
        </button>
    </div>
{/each}

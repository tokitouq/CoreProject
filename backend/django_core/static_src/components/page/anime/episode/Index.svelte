<script lang="ts">
    import Chevron from "$icons/Chevron/Index.svelte";
    import Download from "$icons/Download/Index.svelte";
    import DoubleArrow from "$icons/DoubleArrow/Index.svelte";
    import Share from "$icons/Share/Index.svelte";
    import Play from "$icons/Play/Index.svelte";
    import Settings from "$icons/Settings/Index.svelte";
    import Cross from "$icons/Cross/Index.svelte";
    import Filter from "$icons/Filter/Index.svelte";
    import Chat from "$icons/Chat/Index.svelte";

    import CommentBox from "$components/specific/CommentBox/Index.svelte";
    import Comment from "$components/minor/Comment/Index.svelte";
</script>

<div class="mt-16 flex flex-col md:mt-0 md:gap-[3.5vw] md:py-[2vw] md:pl-[1vw] md:pr-[3.75vw]">
    <div class="grid grid-cols-12 md:gap-[5vw]">
        <div class="col-span-12 flex flex-col md:col-span-8 md:gap-[0.75vw]">
            <div class="relative h-64 w-full md:z-30 md:h-[35vw]">
                <div class="h-full w-full rounded-none object-cover md:rounded-[0.5vw]">
                    <img
                        class="h-full w-full rounded-none object-cover md:rounded-[0.5vw]"
                        src="https://mangathrill.com/wp-content/uploads/2022/02/pjimage-2022-02-09T013124.016.jpg"
                        alt="Episode"
                        loading="lazy"
                    >
                </div>
            </div>
            <div class="flex flex-col gap-2 px-5 md:flex-row md:items-center md:justify-between md:gap-0 md:p-0">
                <div class="flex gap-2 md:items-center md:gap-[1vw]">
                    <div class="hidden items-center gap-[0.75vw] md:flex">
                        <span class="text-[1vw] font-semibold uppercase">sub/dub:</span>
                        <button class="btn !bg-transparent min-h-full flex items-center gap-[0.5vw] rounded-[0.35vw] px-[0.75vw] py-[0.5vw] text-[1vw] leading-none">
                            Vidstreaming (sub) 
                            <Chevron class="w-[1vw]" />
                        </button>
                    </div>
                    <button class="btn !bg-transparent min-h-full hidden items-center p-0 text-xs leading-none md:flex md:text-[0.9vw]">
                        <span>Lights:</span>
                        <div class="font-semibold text-primary-300">Off</div>
                    </button>
                </div>
                <div class="flex w-full items-center justify-between md:w-auto">
                    <div class="flex items-center gap-2 md:hidden">
                        <span class="text-xs font-semibold uppercase">sub/dub:</span>
                        <button class="btn flex items-center gap-2 rounded bg-surface-400 px-3 py-2 text-xs leading-none">
                            Vidstreaming (sub)
                            <Chevron />
                        </button>
                    </div>
                    <div class="flex items-center gap-3 md:gap-[0.75vw]">
                        <a href="/anime/mal/1/episode/1">
                            <Download class="w-4 md:w-[1.4vw]" />
                        </a>
                        <a href="/anime/mal/1/episode/1">
                            <DoubleArrow class="w-4 md:w-[1.4vw] rotate-180" />
                        </a>
                        <a href="/anime/mal/1/episode/1">
                            <DoubleArrow class="w-4 md:w-[1.4vw]" />
                        </a>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-span-12 flex flex-col gap-3 p-5 md:col-span-4 md:gap-[0.5vw] md:p-0">
            <header class="flex items-center justify-between">
                <span class="text-lg font-semibold md:text-[1.35vw]">Episodes</span>
                <button class="btn !bg-transparent min-h-full flex items-center gap-2 rounded bg-surface-400 px-3 py-2 text-xs font-semibold leading-none md:gap-[0.5vw] md:rounded-[0.35vw] md:px-[0.75vw] md:py-[0.5vw] md:text-[1vw]">
                    EPS: 1 - 60
                    <Chevron class="w-3 md:w-[1vw]" />
                </button>
            </header>
            <div class="grid grid-cols-7 gap-2 md:grid-cols-6 md:gap-[0.75vw]">
                {#each {length: 60} as _, index}
                    {@const idx_number = index + 1}
                    <a
                        href="../{idx_number}"
                        class="btn btn-neutral rounded md:h-[2.5vw] min-h-full text-sm font-semibold leading-none md:rounded-[0.35vw] md:text-[1.2vw] text-accent"
                    >
                        {idx_number}
                    </a>
                {/each}
            </div>
        </div>
    </div>
    <div class="grid grid-cols-12 gap-5 p-5 md:gap-[5vw] md:p-0">
        <div class="col-span-12 flex flex-col gap-2 md:col-span-8 md:gap-[1vw]">
            <div class="flex items-center justify-between">
                <div>
                    <a href="/mal/1" class="flex flex-col gap-1 text-lg leading-none md:gap-[0.25vw] md:text-[1.1vw]">
                        <span class="font-semibold uppercase">Demon Slayer S1</span>
                        <span class="text-base text-surface-50 md:text-[1vw]">Kimetsu no yaiba</span>
                    </a>
                </div>
                <button class="btn bg-transparent p-0">
                    <Share class="md:w-[1.25vw]" />
                </button>
            </div>
            <div class="accordion w-full space-y-1 ">
                <div class="accordion-item">
                    <button type="button" class="accordion-control text-start w-full flex items-center space-x-4 p-0 bg-transparent rounded-container-token text-base text-warning font-semibold md:text-[1.25vw] md:leading-[1vw] md:pb-[1vw]" id="accordion-control-0.4186117384197431" aria-expanded="true" aria-controls="accordion-panel-0.4186117384197431">
                        <div class="accordion-lead">EP1</div>
                        <div class="accordion-summary flex-1">Monotone/Colorful</div>
                        <div class="accordion-summary-caret fill-current w-3 transition-transform duration-[200ms] md:w-[1.25vw] rotate-180">
                            <Chevron />
                        </div>
                    </button>
                    <div class="accordion-panel  p-0 rounded-container-token text-surface-50 text-sm leading-snug md:text-[1vw] md:leading-[1.35vw]" id="accordion-panel-0.4186117384197431" role="region" aria-hidden="false" aria-labelledby="accordion-control-0.4186117384197431">The autumn he was twelve, piano prodigy Kousei Arima suddenly found himself unable to play the piano after his mother's death. Ever since then, it's like he's been frozen in time. His childhood friend, Tsubaki Sawabe, watches over him with concern; one day, she invites him on a double date. Kousei's other childhood friend, Ryouta Watari, is being introduced to a certain girl. Kousei reluctantly heads over to the rendezvous spot. There, he sees a girl playing a melodica. This girl, who allegedly has a crush on Watari, is Kaori Miyazono. And she turns out to be a violinist!</div>
                </div>
            </div>
            <a href="/mal/1" class="btn btn-neutral md:h-[3vw] min-h-max md:w-[10vw] rounded-md text-sm font-semibold leading-none md:rounded-[0.5vw] md:text-[1vw]">
                <span>View detail</span>
                <Chevron class="w-3 -rotate-90 md:w-[1vw]" />
            </a>
        </div>
        <div class="col-span-4 hidden flex-col md:flex">
            <span class="font-semibold uppercase md:text-[1.1vw]">next episode</span>
            <a href="/anime/mal/1/episode/1/2" class="flex md:mt-[0.75vw] md:gap-[1vw]">
                <div class="relative">
                    <div class="h-full md:w-[12vw] md:rounded-[0.25vw]">
                        <img class="md:w-[12vw] md:rounded-[0.25vw]" src="https://mangathrill.com/wp-content/uploads/2022/02/pjimage-2022-02-09T013124.016.jpg" alt="" loading="lazy">
                    </div>
                    <overlay class="absolute inset-0 flex items-center justify-center bg-secondary/50">
                        <play class="rounded-full bg-secondary/75 md:p-[1vw]">
                            <Play class="md:w-[1.25vw] text-white" />
                        </play>
                    </overlay>
                </div>
                <div class="flex flex-col justify-between leading-none md:py-[1vw]">
                    <div class="flex flex-col md:gap-[0.5vw]">
                        <span class="text-warning font-semibold md:text-[1.1vw]">Finally they met</span>
                        <span class="md:text-[1vw]">Episode - 2</span>
                    </div>
                    <span class="text-surface-50 md:text-[1vw]">23 min</span>
                </div>
            </a>
        </div>
    </div>
    <div class="grid grid-cols-12 p-5 md:gap-[5vw] md:p-0">
        <div class="col-span-12 flex flex-col md:col-span-7 md:gap-[0.75vw]">
            <span class="flex gap-2 border-b-2 border-surface-50/25 pb-1 text-lg font-semibold md:gap-[0.75vw] md:border-none md:pb-0 md:text-[1.25vw] md:leading-[1.5vw]">Comments</span>
            <div class="mt-2 flex items-center justify-between md:hidden">
                <p class="flex items-center gap-1">
                    <span class="text-base font-bold leading-none">69</span>
                    <span class="text-sm font-semibold text-surface-50">comments</span>
                </p>
                <button class="btn btn-icon h-7 w-auto rounded bg-surface-400 p-0 font-semibold md:ml-0 md:h-[2.4vw] md:w-[2.4vw] md:rounded-[0.5vw] md:leading-[0.9vw]" aria-label="Filter">
                    <svg viewBox="0 0 20 18" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-3 md:w-[1vw]" color="lightgray">
                        <path d="M18.3332 1.5H1.6665L8.33317 9.38333V14.8333L11.6665 16.5V9.38333L18.3332 1.5Z" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></path>
                    </svg>
                </button>
            </div>
            <CommentBox />
            <Comment api_url="" />
        </div>
        <div class="col-span-12 mt-10 flex flex-col gap-5 md:col-span-5 md:mt-0 md:gap-[2vw]">
            <div>
                <div class="flex gap-2 border-b-2 border-surface-50/10 pb-1 md:gap-[0.75vw] md:border-none md:pb-0">
                    <div class="text-base font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Forum Posts</div>
                    <button class="btn btn-secondary min-h-full hidden rounded bg-surface-400 p-0 md:flex md:h-[1.5vw] md:w-[1.5vw]">
                        <Settings class="w-[0.9vw] opacity-75" />
                    </button>
                </div>
                <div class="mt-2 flex items-center justify-between md:mt-[0.75vw]">
                    <p class="flex items-center gap-1 md:hidden">
                        <span class="text-base font-bold leading-none">106</span>
                        <span class="text-sm font-semibold text-surface-50">posts</span>
                    </p>
                    <div class="flex items-center gap-2 md:w-full md:justify-between">
                        <button class="btn btn-secondary min-h-full h-7 gap-2 rounded bg-surface-400 px-2 text-xs font-semibold md:h-[2.4vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.875vw]">
                            <Cross class="w-4 rotate-45 md:w-[1vw]" />
                            Create New
                        </button>
                        <button class="btn btn-secondary min-h-full h-7 w-auto rounded bg-surface-400 p-0 font-semibold md:ml-0 md:h-[2.4vw] md:w-[2.4vw] md:rounded-[0.5vw] md:leading-[0.9vw]" aria-label="Filter">
                            <Filter class="w-3 md:w-[1vw]" />
                        </button>
                    </div>
                </div>
                <div class="mt-4 grid grid-cols-2 flex-col gap-4 md:mt-[1.25vw] md:flex md:gap-[1vw]">
                    <a href="/" class="card w-full grid-cols-7 overflow-hidden rounded-lg !bg-neutral/50 md:grid md:rounded-[0.625vw]">
                        <div class="col-span-2 block h-16 md:h-full md:w-full">
                            <img
                                src="https://timelinecovers.pro/facebook-cover/download/anime-your-lie-in-april-kaori-and-arima-facebook-cover.jpg"
                                alt=""
                                class="h-full w-full object-cover object-center"
                            >
                        </div>
                        <div class="flex h-36 flex-col justify-between p-3 md:col-span-5 md:h-full md:gap-[0.375vw] md:p-[1vw]">
                            <div>
                                <div class="line-clamp-2 text-xs font-extrabold md:text-[0.875vw] md:leading-[1.25vw]">Celebrating 10 years of Hyouka!</div>
                                <div class="mt-2 line-clamp-3 text-[0.6rem] font-medium leading-snug text-surface-50 md:mt-[0.5vw] md:line-clamp-2 md:text-[0.75vw] md:leading-[1.125vw]">Ousei Arima is a child prodigy known as the "Human Metronome" for playing the piano with precision and perfection. Guided by a strict mother and rigorous training, Kousei dominates every competition he enters</div>
                            </div>
                            <div class="flex items-end justify-between text-[0.6rem] leading-none md:mt-[0.75vw] md:items-center md:text-[0.75vw]">
                                <div class="flex flex-col gap-1 md:flex-row md:items-center md:gap-[0.25vw]">
                                    <div>Posted by <span class="text-[0.65rem] font-semibold md:text-[0.85vw]">Eiennlaio</span>
                                    </div>
                                    <div class="text-surface-50">7 months ago</div>
                                </div>
                                <div class="flex items-center gap-1 md:gap-[0.25vw]">
                                    <Chat class="w-3 md:w-[1vw]" />
                                    <div>69</div>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>
            </div>
            <div>
                <span class="text-lg font-semibold md:text-[1.35vw]">Recommendations</span>
                <div class="mt-3 grid grid-cols-3 gap-4 md:mt-[1.25vw] md:grid-cols-3 md:gap-[1vw]">
                    {#each {length: 3} as _}
                        <a href="/myanimelist/38000" class="card relative col-span-1 h-44 w-full overflow-hidden md:h-[15vw] md:rounded-[0.75vw]">
                            <div class="h-full w-full object-cover object-center">
                                <img class="h-full w-full object-cover object-center" src="https://mangathrill.com/wp-content/uploads/2022/02/pjimage-2022-02-09T013124.016.jpg" alt="" loading="lazy">
                            </div>
                            <div class="absolute bottom-3 z-10 flex w-full flex-col items-center gap-1 px-[0.5vw] text-center md:bottom-[1vw] md:gap-[0.25vw]">
                                <div class="text-white text-sm font-semibold leading-snug duration-500 ease-in-out md:h-auto md:max-h-[2.5vw] md:overflow-hidden md:text-[1vw] md:leading-[1.25vw] md:hover:max-h-[7vw] md:hover:overflow-y-scroll md:hover:scrollbar-thin">Demon Slayer: Kimetsu no Yaiba</div>
                                <div class="text-xs leading-none md:text-[0.9vw]">鬼滅の刃</div>
                                <div class="text-xs leading-none text-surface-50 duration-500 ease-in-out md:h-auto md:max-h-[2.5vw] md:overflow-hidden md:text-[0.9vw] md:hover:max-h-[7vw] md:hover:overflow-y-scroll md:hover:scrollbar-thin">Episodes: <b>12</b>
                                </div>
                            </div>
                            <div class="gradient absolute inset-0 rounded-b-[0.45vw] bg-gradient-to-t from-secondary/90 to-secondary/25"></div>
                        </a>
                    {/each}
                </div>
                <div class="mt-3 flex w-full justify-center md:mt-[1vw]">
                    <button class="btn btn-neutral min-h-full h-7 gap-2 rounded px-3 text-xs font-semibold md:h-[2.4vw] md:rounded-[0.5vw] md:px-[0.9vw] md:text-[0.875vw]">
                        Load more
                        <Chevron class="w-4 md:w-[1vw]" />
                    </button>
                </div>
            </div>
        </div>
    </div>
</div>

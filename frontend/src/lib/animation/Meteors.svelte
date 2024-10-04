<script lang="ts">
<<<<<<< HEAD
  import { cn } from "$lib/utils";
  import { onMount } from "svelte";

  export let text="TerraTales"
  export let number = 10;
  let meteorStyles: any = [];
  let changeMeteors = (num: number) => {
    meteorStyles = [];
    const styles = [...new Array(num)].map(() => ({
      top: -20,
      left: Math.floor(Math.random() * 100) + "%",
      animationDelay: Math.random() * 1 + 0.2 + "s",
      animationDuration: Math.floor(Math.random() * 8 + 2.9) + "s",
    }));
    meteorStyles = styles;
  };
  onMount(() => {
    changeMeteors(number);
  });
    $: changeMeteors(number);
</script>
<div
class="relative flex h-fit w-full  items-center justify-center overflow-hidden rounded-lg  bg-secondaryColor p-20 md:shadow-xl"
>
{#each meteorStyles as style, idx}
  <span
    id="meteor-{idx+1}"
    class={cn(
      "pointer-events-none absolute left-1/2 top-1/2 size-[2.4px] rotate-[215deg] animate-meteor rounded-full bg-slate-500 shadow-[0_0_0_1px_#ffffff10]"
    )}
    style="top: {style.top}px; left: {style.left}; animation-delay: {style.animationDelay}; animation-duration: {style.animationDuration};"
  >
    <!-- Meteor Tail  -->
    <div
      class="pointer-events-none absolute top-1/2 -z-10 h-px w-[50px] -translate-y-1/2 bg-gradient-to-r from-slate-500 via-blue-600/30 to-transparent"
    />
  </span>
{/each}
<p
class="z-10 w-[70%] mx-auto text-center text-5xl tracking-[1.5em] font-semibold text-fill-transparent bg-clip-text"
style="background-image: url('/TerraTales.png'); background-size: 160%; background-position: 60% 50%; -webkit-background-clip: text;"
=======
    import { cn } from "$lib/utils";
    import { onMount } from "svelte";
  
    export let text="TerraTales"
    export let number = 10;
    let meteorStyles: any = [];
    let changeMeteors = (num: number) => {
      meteorStyles = [];
      const styles = [...new Array(num)].map(() => ({
        top: -20,
        left: Math.floor(Math.random() * 100) + "%",
        animationDelay: Math.random() * 1 + 0.2 + "s",
        animationDuration: Math.floor(Math.random() * 8 + 2.9) + "s",
      }));
      meteorStyles = styles;
    };
    onMount(() => {
      changeMeteors(number);
    });
      $: changeMeteors(number);
  </script>
  <div
  class="relative flex h-fit w-full  items-center justify-center overflow-hidden rounded-lg  bg-secondaryColor p-14 md:shadow-xl"
>
  {#each meteorStyles as style, idx}
    <span
      id="meteor-{idx+1}"
      class={cn(
        "pointer-events-none absolute left-1/2 top-1/2 size-[2.4px] rotate-[215deg] animate-meteor rounded-full bg-slate-500 shadow-[0_0_0_1px_#ffffff10]"
      )}
      style="top: {style.top}px; left: {style.left}; animation-delay: {style.animationDelay}; animation-duration: {style.animationDuration};"
    >
      <!-- Meteor Tail  -->
      <div
        class="pointer-events-none absolute top-1/2 -z-10 h-px w-[50px] -translate-y-1/2 bg-gradient-to-r from-slate-500 via-blue-600/30 to-transparent"
      />
    </span>
  {/each}
  <p
  class="z-10 w-[70%] mx-auto text-center text-5xl tracking-[1.5em] font-semibold text-fill-transparent bg-clip-text"
  style="background-image: url('/TerraTales.png'); background-size: 160%; background-position: 60% 50%; -webkit-background-clip: text;"
>>>>>>> ee375e6b68eaa20033e2bc3dfcd4dbe057b2525b
>
{text}
</p>
</div>

<style>
  p {
    -webkit-text-fill-color: transparent;
    background-clip: text;
    -webkit-background-clip: text;
  }
</style>
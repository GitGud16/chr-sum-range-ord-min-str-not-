<script>
	import Meteors from '$lib/animation/Meteors.svelte';
</script>


<div class="flex flex-col min-h-screen place-items-center justify-start pt-10 ">

    <img src="/TerraTales.png" class="w-auto h-auto max-h-[40vh] object-contain mb-8" alt="TerraTales Logo">
	<Meteors number={100} text="TerraTales" />

	<p class="text-xl w-[60%] mt-10 text-center">
		Explore how accelerating urbanization has shaped our cities and world. Follow the evolution of cities and changing air quality over the past twenty years, and explore the future outlook that shapes our future. Our website offers you interactive maps and accurate data to help you understand the relationship between urban growth and air pollution, and how we can build more sustainable cities in the future.
	</p>
	<button class="mt-8 px-6 py-3 bg-secondaryColor hover:bg-opacity-80 text-white font-semibold rounded-lg shadow-md transition duration-300 ease-in-out transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-opacity-50 focus:ring-white">
		Start Your Adventure
	</button>
</div>


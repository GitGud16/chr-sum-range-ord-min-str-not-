<script>
	//Ahmed Alsaggaf was here 
	import Meteors from '$lib/animation/Meteors.svelte';
	import { goto } from '$app/navigation';


</script>


<div class="flex flex-col min-h-screen place-items-center justify-start pt-10 ">

    <img src="/TerraTales.png" class="w-auto h-auto max-h-[40vh] object-contain mb-8" alt="TerraTales Logo">
	<Meteors number={100} text="TerraTales" />

	<p class="text-xl w-[60%] mt-10 text-center">
		Explore how accelerating urbanization has shaped our cities and world. Follow the evolution of cities and changing air quality over the past twenty years, and explore the future outlook that shapes our future. Our website offers you interactive maps and accurate data to help you understand the relationship between urban growth and air pollution, and how we can build more sustainable cities in the future.
	</p>
	<button on:click={()=>goto('./Map')} class="mt-8 px-6 py-3 custom hover:bg-opacity-80 text-white font-semibold rounded-lg shadow-md transition duration-300 ease-in-out transform hover:scale-105 hover:ring-2 hover:ring-white hover:ring-opacity-50 focus:outline-none">
		Start Your Adventure
	</button>
</div>


<style>



.custom {
		padding: 10px 20px;
		background-color: #168ee2; /* Consistent color for all buttons */
		color: white;
		border: none;
		border-radius: 8px;
		cursor: pointer;
		font-size: 16px;
		font-weight: bold;
		transition: all 0.3s ease-in-out;
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	}

	.custom:hover {
		background-color: #333333; /* Darker shade for hover state */
		transform: scale(1.05);
		box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
	}

</style>


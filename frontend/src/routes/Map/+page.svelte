<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import L from 'leaflet';
	import 'leaflet/dist/leaflet.css';
	import Papa from 'papaparse';
	import csvData from '$lib/data/aerosol_data_riyadh.csv?raw';

	let mapElement: HTMLElement;
	let map: L.Map;
	let currentDateIndex = 0;
	let dates: string[] = [];
	let dataByDate: Map<string, [number, number, number][]> = new Map();
	let currentMarkers: L.CircleMarker[] = [];
	let isPlaying = false;
	let playInterval: ReturnType<typeof setInterval>;
	let years: number[] = [];
	let maxDateIndex = 0;

	$: currentDate = dates[currentDateIndex] || '';
	$: currentYear = new Date(currentDate).getFullYear();

	function getColor(value: number): string {
		value = Math.max(0, Math.min(1, value));
		const lightness = 100 - (value * 80);
		return `hsl(0, 100%, ${lightness}%)`;
	}

	function updateMap() {
		if (!map) return;
		currentMarkers.forEach(marker => marker.remove());
		currentMarkers = [];

		const points = dataByDate.get(currentDate) || [];
		points.forEach(point => {
			const [lat, lng, value] = point;
			const marker = L.circleMarker([lat, lng], {
				radius: 5,
				fillColor: getColor(value),
				color: 'black',
				weight: 1,
				opacity: 1,
				fillOpacity: 0.8
			}).addTo(map)
				.bindPopup(`Aerosol value: ${value.toFixed(4)}`);
			currentMarkers.push(marker);
		});
	}

	function togglePlay() {
		isPlaying = !isPlaying;
		if (isPlaying) {
			playInterval = setInterval(() => {
				if (currentDateIndex < maxDateIndex) {
					currentDateIndex++;
				} else {
					isPlaying = false;
					clearInterval(playInterval);
				}
			}, 1000);
		} else {
			clearInterval(playInterval);
		}
	}

	$: if (currentDateIndex !== undefined) {
		updateMap();
	}

	onMount(() => {
		map = L.map(mapElement).setView([24.7136, 46.6753], 10);
		L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
			attribution: '© OpenStreetMap contributors'
		}).addTo(map);

		Papa.parse(csvData, {
			header: true,
			dynamicTyping: true,
			complete: (results: Papa.ParseResult<any>) => {
				results.data.forEach((row: any) => {
					if (row.Date && row.Latitude && row.Longitude && row.Aerosol_Optical_Thickness) {
						if (!dataByDate.has(row.Date)) {
							dataByDate.set(row.Date, []);
							dates.push(row.Date);
						}
						dataByDate.get(row.Date)?.push([row.Latitude, row.Longitude, row.Aerosol_Optical_Thickness]);
					}
				});

				dates.sort((a, b) => new Date(a).getTime() - new Date(b).getTime());
				maxDateIndex = dates.length - 1;
				years = [...new Set(dates.map(date => new Date(date).getFullYear()))];
				currentDateIndex = 0;
			}
		});
	});
</script>

<div class="container">
	<h1>Aerosol Optical Thickness Map</h1>
	<div class="map-container">
		<div bind:this={mapElement} class="map"></div>
		<div class="legend">
			<h3>Legend</h3>
			<div class="legend-item">
				<span class="color-box" style="background-color: hsl(0, 100%, 100%);"></span>
				<span>Low</span>
			</div>
			<div class="legend-item">
				<span class="color-box" style="background-color: hsl(0, 100%, 50%);"></span>
				<span>High</span>
			</div>
		</div>
	</div>
	<div class="controls">
		<button on:click={togglePlay} class="custom-button">{isPlaying ? 'Pause' : 'Play'}</button>
		<span class="date-display">{currentDate} (Year: {currentYear})</span>
	</div>
	<div class="year-timeline">
		{#each years as year}
			<span class:active={year === currentYear}>{year}</span>
		{/each}
	</div>
	<button on:click={() => goto('/Charts')} class="custom-button charts-button">View Charts</button>
</div>

<style>
	.container {
		max-width: 1200px;
		margin: 0 auto;
		padding: 20px;
		font-family: Arial, sans-serif;
	}

	h1 {
		text-align: center;
		color: #333;
		margin-bottom: 20px;
	}

	.map-container {
		position: relative;
		margin-bottom: 20px;
	}

	.map {
		height: 500px;
		width: 100%;
		border-radius: 8px;
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	}

	.legend {
		position: absolute;
		bottom: 20px;
		right: 20px;
		background-color: white;
		padding: 10px;
		border-radius: 4px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	.legend h3 {
		margin-top: 0;
		margin-bottom: 10px;
	}

	.legend-item {
		display: flex;
		align-items: center;
		margin-bottom: 5px;
	}

	.color-box {
		width: 20px;
		height: 20px;
		margin-right: 10px;
		border: 1px solid #ccc;
	}

	.controls {
		display: flex;
		align-items: center;
		justify-content: center;
		margin-bottom: 20px;
	}

	.date-display {
		font-size: 18px;
		font-weight: bold;
		margin-left: 20px;
	}

	.year-timeline {
		display: flex;
		justify-content: space-between;
		margin-bottom: 20px;
		background-color: #e0e0e0; /* Changed to a light gray */
		padding: 10px;
		border-radius: 8px;
	}

	.year-timeline span {
		padding: 5px 10px;
		border-radius: 4px;
		cursor: pointer;
		transition: background-color 0.3s ease, color 0.3s ease;
		color: #555; /* Darker text color for better contrast */
	}

	.year-timeline span.active {
		background-color: #4a4a4a; /* Darker gray for active year */
		color: white;
	}

	.custom-button {
		padding: 10px 20px;
		background-color: #4a4a4a; /* Consistent color for all buttons */
		color: white;
		border: none;
		border-radius: 8px;
		cursor: pointer;
		font-size: 16px;
		font-weight: bold;
		transition: all 0.3s ease-in-out;
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	}

	.custom-button:hover {
		background-color: #333333; /* Darker shade for hover state */
		transform: scale(1.05);
		box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
	}

	.custom-button:focus {
		outline: none;
		box-shadow: 0 0 0 3px rgba(74, 74, 74, 0.5);
	}

	.charts-button {
		display: block;
		margin: 0 auto;
	}

	.charts-button:hover {
		background-color: #4d4d4d; /* Darker shade for hover state */
	}
</style>
<script lang="ts">
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    import { Chart, LineController, LineElement, PointElement, LinearScale, TimeScale, Title, Tooltip } from 'chart.js';
    import { Line } from 'svelte-chartjs';
    import Papa from 'papaparse';
    import csvData from '$lib/data/aerosol_data_riyadh.csv?raw';
    import 'chartjs-adapter-date-fns';

    Chart.register(LineController, LineElement, PointElement, LinearScale, TimeScale, Title, Tooltip);

    let chartData: any = null;

    onMount(() => {
        Papa.parse(csvData, {
            header: true,
            dynamicTyping: true,
            complete: (results) => {
                const data = results.data as any[];
                const dateMap = new Map<string, number[]>();

                data.forEach((row) => {
                    if (row.Date && row.Aerosol_Optical_Thickness) {
                        if (!dateMap.has(row.Date)) {
                            dateMap.set(row.Date, []);
                        }
                        dateMap.get(row.Date)?.push(row.Aerosol_Optical_Thickness);
                    }
                });

                const dates = Array.from(dateMap.keys()).sort();
                const averages = dates.map(date => {
                    const values = dateMap.get(date) || [];
                    return values.reduce((a, b) => a + b, 0) / values.length;
                });

                chartData = {
                    labels: dates.map(date => new Date(date)),
                    datasets: [
                        {
                            label: 'Average Aerosol Optical Thickness',
                            data: averages,
                            borderColor: 'rgb(74, 74, 74)',
                            backgroundColor: 'rgba(74, 74, 74, 0.5)',
                        }
                    ]
                };
            }
        });
    });

    function goToMap() {
        goto('/Home');
    }
</script>

<div class="container">
    <h1>Aerosol Optical Thickness Over Time</h1>

    {#if chartData}
        <div class="chart-container">
            <Line 
                data={chartData} 
                options={{
                    responsive: true,
                    scales: {
                        x: {
                            type: 'time',
                            time: {
                                unit: 'day'
                            },
                            title: {
                                display: true,
                                text: 'Date'
                            }
                        },
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Average Aerosol Optical Thickness'
                            }
                        }
                    }
                }}
            />
        </div>
    {:else}
        <p>Loading chart data...</p>
    {/if}

    <div class="button-container">
        <button on:click={goToMap} class="custom-button">Home</button>
    </div>
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

    .chart-container {
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        padding: 20px;
        background-color: white;
    }

    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    .custom-button {
        padding: 10px 20px;
        background-color: #168ee2;
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
        background-color: #333333;
        transform: scale(1.05);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }

    .custom-button:focus {
        outline: none;
        box-shadow: 0 0 0 3px rgba(74, 74, 74, 0.5);
    }
</style>
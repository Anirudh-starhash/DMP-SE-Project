<template>
    <div class="chart-container">
      <canvas ref="pieChart"></canvas>
    </div>
  </template>
  
  <script>
  import { Pie } from 'vue-chartjs';
  import { Chart, ArcElement, Tooltip, Legend } from 'chart.js';
  
  Chart.register(ArcElement, Tooltip, Legend);
  
  export default {
    name: 'PieChart',
    props: {
      sectionInfo: {
        type: Object,
        required: true,
      },
    },
    mounted() {
      this.renderChart();
    },
    methods: {
      renderChart() {
        const labels = Object.keys(this.sectionInfo); // Team names
  
        const totalDisasters = Object.values(this.sectionInfo).map(info => info.total); // Total disasters
        const successRates = Object.values(this.sectionInfo).map(info => info.successRate); // Success rates
  
        // Define custom colors for each team
        const disasterColors = [
          '#FF5733', // Red
          '#33FF57', // Green
          '#3357FF', // Blue
          '#FF33A1', // Pink
          '#FFD700', // Yellow
          '#8A2BE2', // Purple
          '#FF6347', // Tomato
          '#32CD32', // Lime Green
          '#FF4500', // Orange Red
          '#20B2AA', // Light Sea Green
        ];
  
        const successRateColors = [
          '#FF8C00', // Dark Orange
          '#8A2BE2', // BlueViolet
          '#3CB371', // Medium Sea Green
          '#DAA520', // Goldenrod
          '#7B68EE', // Medium Slate Blue
          '#D2691E', // Chocolate
          '#FF1493', // Deep Pink
          '#00BFFF', // Deep Sky Blue
          '#32CD32', // Lime Green
          '#FF4500', // Orange Red
        ];
  
        const data = {
          labels: labels,  // Use Team 1, Team 2, ...
          datasets: [
            {
              label: 'Total Disasters Handled',
              backgroundColor: disasterColors.slice(0, labels.length), // Assign disaster colors
              data: totalDisasters, // Total disasters for each team
              borderColor: '#333', // Darker border for visibility
              borderWidth: 1,
              hoverOffset: 25, // 3D hover effect
            },
            {
              label: 'Success Rate (%)',
              backgroundColor: successRateColors.slice(0, labels.length), // Assign success rate colors
              data: successRates, // Success rates for each team
              borderColor: '#333', // Darker border for visibility
              borderWidth: 1,
              hoverOffset: 25, // 3D hover effect
            },
          ],
        };
  
        const options = {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              position: 'bottom',
              labels: {
                boxWidth: 20,
                padding: 15,
              },
            },
            tooltip: {
              enabled: true,
              callbacks: {
                title: function (tooltipItem) {
                  const sectionLabel = tooltipItem[0].label; // Get section label
                  return `Section: ${sectionLabel}`;  // Display Team name
                },
                label: function (tooltipItem) {
                  const datasetLabel = tooltipItem.dataset.label || '';
                  const value = tooltipItem.raw;
                  if (datasetLabel === 'Total Disasters Handled') {
                    return `${datasetLabel}: ${value} disasters`; // Display total disasters
                  } else if (datasetLabel === 'Success Rate (%)') {
                    return `${datasetLabel}: ${value}%`; // Display success rate
                  }
                  return '';
                },
              },
            },
          },
        };
  
        this.chart = new Chart(this.$refs.pieChart, {
          type: 'pie',
          data: data,
          options: options,
        });
      },
    },
    beforeDestroy() {
      if (this.chart) {
        this.chart.destroy(); // Clean up chart instance
      }
    },
  };
  </script>
  
  <style scoped>
  .chart-container {
    position: relative;
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
    background: #f9f9f9;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    padding: 20px;
  }
  
  canvas {
    display: block;
    width: 100%;
    height: auto;
  }
  
  .pie-chart-3d {
    background-color: aliceblue;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2); /* Adding shadow for 3D effect */
  }
  </style>
  
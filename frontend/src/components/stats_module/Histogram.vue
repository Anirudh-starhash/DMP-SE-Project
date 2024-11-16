<template>
    <div class="chart-container">
      <canvas ref="barChart"></canvas>
    </div>
  </template>
  
  <script>
  import { Bar } from 'vue-chartjs';
  import { Chart, BarElement, CategoryScale, LinearScale, Tooltip, Legend } from 'chart.js';
  
  Chart.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);
  
  export default {
    name: 'BarChart',
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
        // Create Team 1, Team 2, ... labels dynamically based on the order
        const labels = Object.keys(this.sectionInfo).map((_, index) => `Team ${index + 1}`);
  
        const totalDisasters = Object.values(this.sectionInfo).map(info => info.total); // Total disasters
        const successRates = Object.values(this.sectionInfo).map(info => info.successRate); // Success rates
  
        const data = {
          labels: labels,  // Use Team 1, Team 2, ...
          datasets: [
            {
              label: 'Total Disasters Handled',
              backgroundColor: '#36A2EB',
              data: totalDisasters,
              borderColor: '#1E74FF',
              borderWidth: 1,
            },
            {
              label: 'Success Rate (%)',
              backgroundColor: '#FF6384',
              data: successRates,
              borderColor: '#FF3366',
              borderWidth: 1,
            },
          ],
        };
  
        const options = {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: {
              beginAtZero: false,  // Start from 1
              min: 1,
              title: {
                display: true,
                text: 'Count / Percentage',
              },
            },
          },
          plugins: {
            tooltip: {
              callbacks: {
                title: function (tooltipItem) {
                  const teamLabel = tooltipItem[0].label; // Get Team label (e.g., Team 1)
                  return `Disaster Team: ${teamLabel}`;
                },
                label: function (tooltipItem) {
                  const datasetLabel = tooltipItem.dataset.label || '';
                  const disasterDetails = tooltipItem.raw;
                  if (datasetLabel === 'Total Disasters Handled') {
                    return `${datasetLabel}: ${disasterDetails} disasters`;
                  } else if (datasetLabel === 'Success Rate (%)') {
                    return `${datasetLabel}: ${disasterDetails}%`;
                  }
                  return '';
                },
              },
            },
          },
        };
  
        new Chart(this.$refs.barChart, {
          type: 'bar',
          data: data,
          options: options,
        });
      },
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
  </style>
  
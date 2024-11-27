<template>
  <div class="chart-container">
    <canvas ref="pieChart"></canvas>
  </div>
</template>

<script>

import { Chart, ArcElement, Tooltip, Legend, PieController } from 'chart.js';

Chart.register(ArcElement, Tooltip, Legend, PieController); // Register PieController

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
        '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFD700',
        '#8A2BE2', '#FF6347', '#32CD32', '#FF4500', '#20B2AA',
      ];

      const successRateColors = [
        '#FF8C00', '#8A2BE2', '#3CB371', '#DAA520', '#7B68EE',
        '#D2691E', '#FF1493', '#00BFFF', '#32CD32', '#FF4500',
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
            backgroundColor: '#333', // Dark background for tooltips
            titleColor: '#fff', // White title text
            bodyColor: '#fff', // White body text
            padding: 10,
          },
        },
        animation: {
          animateRotate: {
            duration: 1500, // Slow down the rotation animation
            easing: 'easeOutBounce', // Add ease out bounce effect
          },
          animateScale: {
            duration: 1000, // Scaling animation duration
            easing: 'easeInOutQuad', // Easing effect
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
/* Chart Container */
.chart-container {
  position: relative;
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  background: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  overflow: hidden;
  transform: scale(0.95);
  transition: transform 0.3s ease-in-out;
}

/* Hover Effect for the Chart Container */
.chart-container:hover {
  transform: scale(1); /* Slight zoom on hover */
}

/* Pie chart CSS styling */
canvas {
  display: block;
  width: 100%;
  height: auto;
  transition: transform 0.3s ease; /* Animation for scaling */
}

/* 3D Effect for the Pie chart */
.pie-chart-3d {
  background-color: aliceblue;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2); /* Adding shadow for 3D effect */
}

/* Tooltip Styling */
.chartjs-tooltip {
  background-color: #333 !important;
  color: #fff !important;
  border-radius: 5px;
  padding: 10px;
}
</style>

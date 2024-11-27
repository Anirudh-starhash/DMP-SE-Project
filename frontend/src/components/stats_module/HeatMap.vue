<template>
  <div class="chart-container">
    <canvas ref="heatmapChart"></canvas>
  </div>
</template>

<script>
import { Chart, Tooltip, Legend, CategoryScale, LinearScale, PointElement } from 'chart.js';

Chart.register(Tooltip, Legend, CategoryScale, LinearScale, PointElement);

export default {
  name: 'HeatmapChart',
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
      if (this.chart) {
        this.chart.destroy(); // Destroy previous chart instance
      }

      // Prepare data for heatmap: 
      // Using Team 1, Team 2, etc., and their total disasters and success rates
      const labels = Object.keys(this.sectionInfo); // Team names
      const totalDisasters = Object.values(this.sectionInfo).map(info => info.total); // Total disasters
      const successRates = Object.values(this.sectionInfo).map(info => info.successRate); // Success rates

      // Combine the two data arrays (totalDisasters and successRates) for heatmap
      const heatmapData = [
        ...labels.map((label, index) => ({
          x: index + 1, // Use 1-based index for team names
          y: totalDisasters[index],
          label: `${label} Total Disasters`,
        })),
        ...labels.map((label, index) => ({
          x: index + 1, // Use 1-based index for team names
          y: successRates[index],
          label: `${label} Success Rate`,
        }))
      ];

      const data = {
        datasets: [{
          label: 'Heatmap Data',
          data: heatmapData,
          backgroundColor: (context) => {
            if (!context.raw) {
              return 'rgba(0,0,0,0.1)';
            }

            const value = context.raw.y; // y-value (either total disasters or success rate)
            const red = Math.min(255, value * 2);
            const green = Math.min(255, 255 - value * 2);
            const blue = Math.min(255, value * 1.5);
            return `rgba(${red}, ${green}, ${blue}, 0.7)`; // Return RGBA color
          },
          borderWidth: 1,
          pointRadius: 10,
        }],
      };

      const options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            type: 'category', // Use category scale to display Team names as labels
            labels: labels, // Set x-axis labels to be the team names
            title: {
              display: true,
              text: 'Teams',
            },
          },
          y: {
            type: 'linear',
            position: 'left',
            title: {
              display: true,
              text: 'Values (Disasters / Success Rate)',
            },
          },
        },
        plugins: {
          legend: {
            display: false,
          },
          tooltip: {
            callbacks: {
              title: function (tooltipItem) {
                const teamIndex = tooltipItem[0].raw.x - 1; // Get the index based on x value (1-based)
                return `Team-${teamIndex + 1}`;  // Format "Team-1", "Team-2", etc.
              },
              label: function (tooltipItem) {
                return `Value: ${tooltipItem.raw.y}`; // Show the y-value (either total disasters or success rate)
              },
            },
          },
        },
      };

      this.chart = new Chart(this.$refs.heatmapChart, {
        type: 'scatter', // Scatter chart type to simulate heatmap
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
</style>

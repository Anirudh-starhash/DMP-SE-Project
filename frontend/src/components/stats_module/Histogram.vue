<template>
  <div class="chart-container">
    <canvas ref="histogramChart"></canvas>
  </div>
</template>

<script>
import { Chart, BarElement, CategoryScale, LinearScale, Tooltip, Legend } from 'chart.js';

Chart.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

export default {
  name: 'HistogramChart',
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

      const disasterCounts = Object.values(this.sectionInfo).map(info => info.total); // Total disasters

      const data = {
        labels: labels, // Labels for each team
        datasets: [
          {
            label: 'Disaster Frequency',
            backgroundColor: '#36A2EB',
            data: disasterCounts,
            borderColor: '#1E74FF',
            borderWidth: 1,
            barThickness: 30,  // Adjust thickness of the bars for a histogram effect
          },
        ],
      };

      const options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            title: {
              display: true,
              text: 'Teams',
            },
          },
          y: {
            beginAtZero: true,  // Start from 0
            title: {
              display: true,
              text: 'Frequency',
            },
          },
        },
        plugins: {
          tooltip: {
            callbacks: {
              title: function (tooltipItem) {
                const teamLabel = tooltipItem[0].label; // Get Team label (e.g., Team 1)
                return `Team: ${teamLabel}`;
              },
              label: function (tooltipItem) {
                const datasetLabel = tooltipItem.dataset.label || '';
                const disasterDetails = tooltipItem.raw;
                return `${datasetLabel}: ${disasterDetails} disasters`;
              },
            },
          },
        },
      };

      new Chart(this.$refs.histogramChart, {
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

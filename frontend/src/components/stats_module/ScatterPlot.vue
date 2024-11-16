<template>
  <div class="scatter-plot">
    <canvas ref="scatterChart"></canvas>
  </div>
</template>

<script>
import { Scatter } from 'vue-chartjs';
import { Chart, ScatterController, LinearScale, PointElement, Tooltip, Legend } from 'chart.js';

Chart.register(ScatterController, LinearScale, PointElement, Tooltip, Legend);

export default {
  name: 'ScatterPlot',
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
      const dataPoints = Object.values(this.sectionInfo); // Disaster data

      const data = {
        datasets: [
          {
            label: 'Disasters Handled',
            data: labels.map((label, index) => {
              const info = dataPoints[index];
              return {
                x: info.total, // x-axis is the total number of disasters handled
                y: info.successRate, // y-axis is the success rate of the disaster handling
                label: label, // Store the disaster team name
                details: info, // Store additional details for use in tooltips
              };
            }),
            backgroundColor: '#FF6384',
            pointBorderColor: '#36A2EB',
            pointBackgroundColor: '#FFCE56',
            pointBorderWidth: 2,
            pointRadius: 6,
            hoverBackgroundColor: '#FF9F40', // Change color on hover
            hoverBorderWidth: 3,
            hoverBorderColor: '#FF5733',
          },
        ],
      };

      const options = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: true,
          },
          tooltip: {
            enabled: true,
            callbacks: {
              title: function (tooltipItem) {
                return `Team: ${tooltipItem[0].raw.label}`; // Show the team name (e.g., Team 1)
              },
              label: function (tooltipItem) {
                const { details } = tooltipItem[0].raw;
                return `Success Rate: ${details.successRate}%\nTotal Disasters: ${details.total}\nLocation: ${details.location}\nTime: ${details.time}`;
              },
            },
          },
        },
        scales: {
          x: {
            type: 'linear',
            position: 'bottom',
            title: {
              display: true,
              text: 'Total Disasters Handled',
            },
          },
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Success Rate (%)',
            },
          },
        },
      };

      new Chart(this.$refs.scatterChart, {
        type: 'scatter',
        data: data,
        options: options,
      });
    },
  },
};
</script>

<style scoped>
.scatter-plot {
  background-color: aliceblue;
  background-size: cover;
  background-position: center;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
}

canvas {
  display: block;
  width: 100%;
  height: auto;
}
</style>

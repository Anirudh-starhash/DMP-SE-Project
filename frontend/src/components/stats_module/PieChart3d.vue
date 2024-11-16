<template>
  <div class="chart-container">
    <canvas ref="pieChart3D"></canvas>
  </div>
</template>

<script>
import { Pie } from 'vue-chartjs';
import { Chart, ArcElement, Tooltip, Legend } from 'chart.js';

Chart.register(ArcElement, Tooltip, Legend);

export default {
  name: 'PieChart3D',
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
      
      const dataValues = Object.values(this.sectionInfo); // Disaster data (total disasters handled)

      const data = {
        labels: labels,  // Team 1, Team 2, ...
        datasets: [
          {
            label: 'Disasters Handled',
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'],
            data: dataValues.map(item => item.total), // Extract total disasters from sectionInfo
            borderWidth: 1,
            borderColor: '#333',
            hoverBorderColor: '#000',
            hoverOffset: 25, // Stronger hover effect for a 3D look
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
                const teamLabel = tooltipItem[0].label; // Get Team label (e.g., Team 1)
                return `Disaster Team: ${teamLabel}`;
              },
              label: function (tooltipItem) {
                const datasetLabel = tooltipItem.dataset.label || '';
                const disasterDetails = tooltipItem.raw;
                return `${datasetLabel}: ${disasterDetails} disasters`;
              },
            },
          },
        },
        elements: {
          arc: {
            borderWidth: 2,
            borderColor: 'rgba(0,0,0,0.1)',
            hoverBorderColor: 'rgba(0,0,0,0.3)',
            hoverOffset: 15, // More pronounced shadow effect on hover
          },
        },
      };

      new Chart(this.$refs.pieChart3D, {
        type: 'pie',
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

.pie-chart-3d {
  background-color: aliceblue;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2); /* Adding shadow for 3D effect */
}
</style>

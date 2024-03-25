<template>
  <div class="line-chart">
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto'

export default {
  name: 'LineChart',
  props: {
    data: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      chart: null
    }
  },
  mounted() {
    this.renderChart()
  },
  watch: {
    data() {
      this.renderChart()
    }
  },
  methods: {
    renderChart() {
      if (!this.$refs.chartCanvas) return

      // 销毁现有的图表实例
      if (this.chart) {
        this.chart.destroy()
      }

      // 创建新的图表实例
      this.chart = new Chart(this.$refs.chartCanvas.getContext('2d'), {
        // ... (保持图表配置不变)
      })
    }
  }
}
</script>

<style scoped>
.line-chart {
  width: 100%;
  height: 100%;
}
</style>
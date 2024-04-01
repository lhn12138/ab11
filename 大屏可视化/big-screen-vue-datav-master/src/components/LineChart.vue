<template>
  <div class="line-chart-container">
    <div ref="lineChart" class="line-chart"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  props: {
    data: {
      type: Array,
      required: true
    },
    labels: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      chartInstance: null
    }
  },
  mounted() {
    this.renderLineChart()
  },
  watch: {
    data() {
      this.renderLineChart()
    },
    labels() {
      this.renderLineChart()
    }
  },
  methods: {
    renderLineChart() {
      if (this.$refs.lineChart) {
        this.chartInstance = echarts.init(this.$refs.lineChart)
        this.chartInstance.setOption({
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross',
              label: {
                backgroundColor: '#6a7985'
              }
            }
          },
          xAxis: {
            type: 'category',
            data: this.labels,
            axisLabel: {
              rotate: 45,
              fontSize: 12
            }
          },
          yAxis: {
            type: 'value',
            axisLabel: {
              formatter: '{value}'
            }
          },
          series: [
            {
              data: this.data,
              type: 'line',
              smooth: true,
              itemStyle: {
                color: 'rgba(75, 192, 192, 1)'
              },
              areaStyle: {
                color: 'rgba(75, 192, 192, 0.2)'
              },
              emphasis: {
                focus: 'series'
              }
            }
          ]
        })

        this.chartInstance.on('mouseover', (params) => {
          this.chartInstance.dispatchAction({
            type: 'showTip',
            seriesIndex: params.seriesIndex,
            dataIndex: params.dataIndex
          })
        })

        this.chartInstance.on('mouseout', () => {
          this.chartInstance.dispatchAction({
            type: 'hideTip'
          })
        })
      }
    }
  }
}
</script>

<style scoped>
.line-chart-container {
  width: 100%;
  height: 300px;
}

.line-chart {
  width: 100%;
  height: 100%;
}
</style>
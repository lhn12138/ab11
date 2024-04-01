<template>
  <div class="radar-chart">
    <div id="radarChart" ref="radarChart" style="width: 100%; height: 300px;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'RadarChart',
  props: {
    data: {
      type: Array,
      required: true
    },
    title: {
      type: String,
      default: '评分指标',
      style: {
        color: '#eae5e5',
        fontSize: '30px',
        fontWeight: 'bold'
      }
    },
    indicatorNames: {
      type: Array,
      default: () => ['外观', '内饰', '配置', '空间', '舒适性', '操控', '动力']
    },
    maxValue: {
      type: Number,
      default: 5
    }
  },
  data() {
    return {
      chartInstance: null
    }
  },
  mounted() {
    this.initRadarChart()
  },
  watch: {
    data() {
      this.initRadarChart()
    }
  },
  methods: {
    initRadarChart() {
      this.chartInstance = echarts.init(this.$refs.radarChart)

      this.chartInstance.setOption({
        title: {
          text: this.title,
          textStyle: {
            color: '#dad7d7',
            fontSize: '30px',
            fontWeight: 'bold'
          }
        },
        tooltip: {
          trigger: 'item'
        },
        radar: {
          // shape: 'circle',
          indicator: this.indicatorNames.map(name => ({ name, max: this.maxValue }))
        },
        series: [
          {
            name: '评分',
            type: 'radar',
            data: [
              {
                value: this.data,
                name: '评分'
              }
            ],
            emphasis: {
              areaStyle: {
                color: 'rgba(0,250,0,0.2)'
              }
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
</script>

<style scoped>
.radar-chart {
  width: 100%;
  height: 300px;
}
</style>
<template>
  <div>
    <!--    <Chart :cdata="cdata" />-->
    <div ref="chart" style="width: 100%;height: 480px" v-bind:key="cdata.lineData[0]"
         @mouseenter="startAction" @mouseleave="cancelAction"></div>
  </div>
</template>

<script>
// import Chart from './chart.vue'
export default {
  data() {
    return {
      isHovered: true,
      cdata: {
        category: [],
        lineData: [],
        barData: [],
        rateData: []
      },
      currentIndex: 0
    };
  },
  components: {
    // Chart,
  },
  async mounted() {
    const res = await this.$http.get('myapp/data2')
    this.$set(this.cdata, 'category', res.data.yearsList)
    this.$set(this.cdata, 'lineData', res.data.rateList)
    this.$set(this.cdata, 'barData', res.data.volumeList)
    this.initChart()
    this.stratDataUpdateInterval()
  },

  updated() {
    this.initChart()
    this.stratDataUpdateInterval()

  },
  methods: {

    startAction() {
      this.isHovered = false
      this.stratDataUpdateInterval()
    },
    cancelAction() {
      this.isHovered = true
      this.stratDataUpdateInterval()
    },
    initChart() {
      this.myChart = this.$echarts.init(this.$refs.chart);

      const option = {
        tooltip: {
          trigger: "axis",
          backgroundColor: "rgba(255,255,255,0.1)",
          axisPointer: {
            type: "shadow",
            label: {
              show: true,
              backgroundColor: "#7B7DDC"
            }
          }
        },
        dataZoom: [
          {
            type: "slider",
            start: 0,
            end: 95,
            show: false

          }
        ],
        legend: {
          data: ["同比变化", "销售情况"],
          textStyle: {
            color: "#B4B4B4",
            fontSize: 20
          },
          top: "0%"
        },
        grid: {
          x: "8%",
          width: "88%",
          y: "4%"
        },
        xAxis: {
          data: this.cdata.category.slice(this.currentIndex, this.currentIndex + 12),
          axisLine: {
            lineStyle: {
              color: "#ea3131"
            }
          },
          axisLabel: {
            show: true,
            interval: 0,
            fontSize: 15
          },
          axisTick: {
            show: false
          }
        },
        yAxis: [
          {
            splitLine: {show: false},
            axisLine: {
              lineStyle: {
                color: "#d76d6d"
              }
            },

            axisLabel: {
              formatter: "{value} "
            }
          },
          {
            splitLine: {show: false},
            axisLine: {
              lineStyle: {
                color: "#c07979"
              }
            },
            axisLabel: {
              formatter: "{value} "
            }
          }
        ],
        series: [
          {
            name: "同比变化",
            type: "line",
            smooth: true,
            showAllSymbol: true,
            symbol: "emptyCircle",
            symbolSize: 8,
            yAxisIndex: 1,
            itemStyle: {
              normal: {
                barBorderRadius: 5,
                color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  {offset: 0, color: "#e06024"},
                  {offset: 1, color: "#ab885c"}
                ])
              }
            },
            data: this.cdata.lineData.slice(this.currentIndex, this.currentIndex + 12)
          },
          {
            name: "销售情况",
            type: "bar",
            barWidth: 10,
            itemStyle: {
              normal: {
                barBorderRadius: 5,
                color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  {offset: 0, color: "#3e7cb9"},
                  {offset: 1, color: "white"}
                ])
              }
            },
            data: this.cdata.barData.slice(this.currentIndex, this.currentIndex + 12)
          },
        ]
      }
      this.myChart.setOption(option)
    },
    changeData(x) {
      var st = x[0]
      for (var i = 0; i < x.length - 1; i++) {
        x[i] = x[i + 1]
      }
      x[x.length - 1] = st
    },
    updateBarChart() {
      if (this.isHovered) {
        this.currentIndex = (this.currentIndex + 1) % this.cdata.category.length
        if (this.currentIndex + 12 > this.cdata.category.length) {
          this.currentIndex = 0
        }
        // console.log('currentIndex:', this.currentIndex)
        this.myChart.setOption({
          xAxis: {
            data: this.cdata.category.slice(this.currentIndex, this.currentIndex + 12)
          },
          series: [
            {
              data: this.cdata.lineData.slice(this.currentIndex, this.currentIndex + 12)
            },
            {
              data: this.cdata.barData.slice(this.currentIndex, this.currentIndex + 12)
            }
          ]
        })
      } else {
        clearInterval(this.timer)
      }
    },

    stratDataUpdateInterval() {
      if (this.isHovered) {
        const interval = 2500
        clearInterval(this.timer)
        console.log('Timer started')
        this.timer = setInterval(this.updateBarChart, interval)
      } else {
        console.log('Timer stopped')
        clearInterval(this.timer)
        this.updateBarChart()
      }
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
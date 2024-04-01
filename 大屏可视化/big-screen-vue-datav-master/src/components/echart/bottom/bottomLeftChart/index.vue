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
        category: [

        ],
        lineData: [

        ],
        barData: [

        ],
        rateData: []
      }
    };
  },
  components: {
    // Chart,
  },
  async mounted() {
    const res = await this.$http.get('myapp/data3')
    this.$set(this.cdata, 'category', res.data.yearList)
    this.$set(this.cdata, 'lineData', res.data.rateList)
    this.$set(this.cdata, 'barData', res.data.volumeList)

  },

  updated() {
    this.initChart()
    this.stratDataUpdateInterval()

  },
  methods: {

    startAction() {
      this.isHovered = false
    },
    cancelAction() {
      this.isHovered = true
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
            fontSize:20
          },
          top: "0%"
        },
        grid: {
          x: "8%",
          width: "88%",
          y: "4%"
        },
        xAxis: {
          data: this.cdata.category,
          axisLine: {
            lineStyle: {
              color: "#B4B4B4"
            }
          },
          axisLabel: {
            show: true,
            interval: 0,
            fontSize: 18

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
                color: "#B4B4B4"
              }
            },

            axisLabel: {
              formatter: "{value} ",
              fontSize: 13
            }
          },
          {
            splitLine: {show: false},
            axisLine: {
              lineStyle: {
                color: "#B4B4B4"
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
                  {offset: 0, color: "#5C4033"},
                  {offset: 1, color: "#FAEBD7"}
                ])
              }
            },
            data: this.cdata.lineData
          },
          {
            name: "销售情况",
            type: "bar",
            barWidth: 10,
            itemStyle: {
              normal: {
                barBorderRadius: 5,
                color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  {offset: 0, color: "#082e53"},
                  {offset: 1, color: "white"}
                ])
              }
            },
            data: this.cdata.barData
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
      if (this.isHovered == true) {
        this.changeData(this.cdata.category)
        this.changeData(this.cdata.lineData)
        this.changeData(this.cdata.barData)
        // console.log(this.cdata.category)
        this.myChart.setOption({
          xAxis: {
            data: this.cdata.category
          },
          series: [
            {
              data: this.cdata.lineData
            },
            {
              data: this.cdata.barData
            }
          ],
        })

      } else {
        clearInterval(this.timer)

      }


    },
    stratDataUpdateInterval() {
      if (this.isHovered == true) {
        const interval = 2500
        clearInterval(this.timer)
        setInterval(this.updateBarChart, interval)
      }
    }

  }
};
</script>

<style lang="scss" scoped>
</style>
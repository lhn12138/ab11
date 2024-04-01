<template>
  <div>
    <div class="search-container">
      <input type="text" v-model="searchInput" placeholder="输入年月(如:2023-12)" @keyup.enter="searchData" />
      <button @click="searchData">搜索</button>
    </div>
    <div ref="chart" style="width: 100%;height: 430px" v-bind:key="cdata.lineData[0]"
         @mouseenter="startAction" @mouseleave="cancelAction"></div>
  </div>
</template>

<script>
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
      currentIndex: 0,
      searchInput: ""
    };
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
    searchData() {
      const searchYear = this.searchInput.split('-')[0];
      const searchMonth = this.searchInput.split('-')[1];
      const index = this.cdata.category.findIndex(item => {
        const year = parseInt(item.split('-')[0]);
        const month = parseInt(item.split('-')[1]);
        return year === parseInt(searchYear) && month === parseInt(searchMonth);
      });
      if (index !== -1) {
        this.currentIndex = index;
        this.initChart();
        this.highlightData();
      } else {
        alert('未找到该数据');
      }
    },
    highlightData() {
      this.myChart.dispatchAction({
        type: 'highlight',
        seriesIndex: 0,
        dataIndex: this.currentIndex
      });
      this.myChart.dispatchAction({
        type: 'highlight',
        seriesIndex: 1,
        dataIndex: this.currentIndex
      });
    },
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
              formatter: "{value} ",
              fontSize:13,
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
.search-container {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 20px;

  input {
    padding: 5px 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
    margin-right: 10px;
  }

  button {
    padding: 5px 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
}

::v-deep .echarts-for-vue {
  .echarts-tooltip-content {
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 4px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
    padding: 10px;
    font-size: 14px;
    color: #333;
  }

  .echarts-tooltip-item-list {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .echarts-tooltip-item {
    display: flex;
    align-items: center;
    margin-bottom: 5px;

    .echarts-tooltip-marker {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      margin-right: 5px;
    }

    .echarts-tooltip-value {
      font-weight: bold;
    }
  }

  .echarts-series-item-highlighted {
    opacity: 1 !important;
  }
}
</style>
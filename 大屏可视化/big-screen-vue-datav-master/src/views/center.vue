<template>
  <div id="center">
    <div class="up">
      <div
          class="bg-color-black item"

      >
        <p class="ml-3 colorBlue fw-b fs-xl">车辆总数据</p>
        <div style="text-align: center;line-height: 2">
          {{this.result.sumCar}}条

        </div>
      </div>
      <div
          class="bg-color-black item"

      >
        <p class="ml-3 colorBlue fw-b fs-xl">当月销售最多汽车</p>
        <div style="text-align: center;line-height: 2">
          {{this.result.topCar}}

        </div>
      </div>
      <div
          class="bg-color-black item"

      >
        <p class="ml-3 colorBlue fw-b fs-xl">当月车辆最高销售额</p>
        <div style="text-align: center;line-height: 2">
          {{this.result.highVolume}}辆

        </div>
      </div>
      <div
          class="bg-color-black item"

      >
        <p class="ml-3 colorBlue fw-b fs-xl">当月销售最多车型</p>
        <div style="text-align: center;line-height: 2">
          {{this.result.mostModel}}

        </div>
      </div>
      <div
          class="bg-color-black item"

      >
        <p class="ml-3 colorBlue fw-b fs-xl">当月车型最多品牌</p>
        <div style="text-align: center;line-height: 2">
          {{this.result.mostBrand}}

        </div>
      </div>
      <div
          class="bg-color-black item"

      >
        <p class="ml-3 colorBlue fw-b fs-xl">当月车辆平均价格</p>
        <div style="text-align: center;line-height: 2">
          {{this.result.averagePrice}}万

        </div>
      </div>
    </div>
    <div class="down">
      <div class="ranking bg-color-black">
        <span>
          <icon name="chart-pie" class="text-icon"></icon>
        </span>
        <span class="fs-xl text mx-2 mb-1 pl-3" style="font-size: 26px;">汽车品牌榜</span>
        <dv-scroll-ranking-board class="dv-scr-rank-board mt-1" :config="ranking" v-bind:key="ranking.data[0].value"/>
      </div>
      <div class="percent">
        <div class="item bg-color-black">
          <span style="font-size: 21px">油车占有率</span>
          <CenterChart
              :id="rate[0].id"
              :tips="rate[0].tips"
              :colorObj="rate[0].colorData"
          />
        </div>
        <div class="item bg-color-black">
          <span style="font-size: 21px">电车占有率</span>
          <CenterChart
              :id="rate[1].id"
              :tips="rate[1].tips"
              :colorObj="rate[1].colorData"
          />
        </div>
        <div class="water" style="text-align: center;font-size: 20px">
          <p style="font-size: 21px">油电混合比率</p>
          <dv-water-level-pond class="dv-wa-le-po" :config="water" v-bind:key="water.data[0]"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CenterChart from '@/components/echart/center/centerChartRate'

export default {
  data() {
    return {
      result:'',
      ranking: {
        data: [
          {
            name: '默认',
            value: 1
          },

        ],
        carousel: 'single',
        unit: '类'
      },
      water: {
        data: [24, 45],
        shape: 'round',
        formatter: '{value}%',
        waveNum: 3
      },
      // 通过率和达标率的组件复用数据
      rate: [
        {
          id: 'centerRate1',
          tips: 60,
          colorData: {
            textStyle: '#3fc0fb',
            series: {
              color: ['#00bcd44a', 'transparent'],
              dataColor: {
                normal: '#03a9f4',
                shadowColor: '#97e2f5'
              }
            }
          }
        },
        {
          id: 'centerRate2',
          tips: 40,
          colorData: {
            textStyle: '#67e0e3',
            series: {
              color: ['#faf3a378', 'transparent'],
              dataColor: {
                normal: '#ff9800',
                shadowColor: '#fcebad'
              }
            }
          }
        }
      ]
    }
  },
  components: {
    CenterChart
  },
  async mounted(){
    const res = await this.$http.get('myapp/center')
    this.result=res.data
    this.$set(this.ranking,'data',res.data.lastSortList)
    this.$set(this.rate[0],'tips',res.data.oilRate)
    this.$set(this.rate[1],'tips',res.data.electricRate)
    this.$set(this.water,'data',[res.data.mixRate])


    console.log(this.water.data)
  },


}
</script>

<style lang="scss" scoped>
#center {
  display: flex;
  flex-direction: column;

  .bg-color-black.item p {
    font-size: 20px; /* 设置为24像素 */
  }

  .up {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    font-size: 20px;

    .item {
      border-radius: 6px;
      padding-top: 8px;
      margin-top: 8px;
      width: 32%;
      height: 70px;
      font-size: 20px;

      .dv-dig-flop {
        width: 150px;
        height: 30px;
        font-size: 20px;
      }
    }
  }

  .down {
    padding: 6px 4px;
    padding-bottom: 0;
    width: 100%;
    display: flex;
    height: 255px;
    justify-content: space-between;
    font-size: 20px;

    .bg-color-black {
      border-radius: 5px;
    }

    .ranking {
      padding: 10px;
      width: 59%;
      font-size: 20px;

      .dv-scr-rank-board {
        height: 225px;
        font-size: 20px;
      }
    }

    .percent {
      width: 40%;
      display: flex;
      flex-wrap: wrap;
      font-size: 20px;

      .item {
        width: 50%;
        height: 120px;
        font-size: 20px;

        span {
          margin-top: 8px;
          font-size: 18px;
          display: flex;
          justify-content: center;
        }
      }

      .water {
        width: 85%;

        .dv-wa-le-po {
          height: 120px;
          font-size: 20px;
        }
      }
    }
  }
}
</style>

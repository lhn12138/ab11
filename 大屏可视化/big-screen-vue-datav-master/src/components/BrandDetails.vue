<template>
  <div class="brand-details">
    <div class="brand-info">
      <h2 class="brand-name">{{ brand.name }} 品牌详情</h2>
      <p class="brand-sales">销售总额: <span class="sales-amount">{{ brand.sales }}</span></p>
      <Echart ref="scoreChart" class="score-chart" :option="scoreChartOption" />
    </div>
    <div class="brand-sales">
      <h3 class="sales-chart-title">{{ brand.name }} 销量折线图</h3>
      <Echart ref="salesChart" class="sales-chart" :option="salesChartOption" />
    </div>
  </div>
</template>

<script>
import Echart from '@/common/echart'

export default {
  name: 'BrandDetails',
  components: {
    Echart
  },
  props: {
    brand: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      scoreChartOption: null,
      salesChartOption: null
    }
  },
  mounted() {
    this.initScoreChart()
    this.initSalesChart()
  },
  methods: {
    initScoreChart() {
      this.scoreChartOption = {
        tooltip: {
          trigger: 'item'
        },
        radar: {
          // 雷达图的各项指标
          indicator: [
            { name: '质量', max: 5 },
            { name: '价格', max: 5 },
            { name: '服务', max: 5 },
            { name: '创新', max: 5 },
            { name: '设计', max: 5 },
            { name: '声誉', max: 5 }
          ]
        },
        series: [
          {
            name: '品牌评分',
            type: 'radar',
            // 数据来自 brand.score 对象
            data: [
              {
                value: [
                  this.brand.score.quality,
                  this.brand.score.price,
                  this.brand.score.service,
                  this.brand.score.innovation,
                  this.brand.score.design,
                  this.brand.score.reputation
                ],
                name: this.brand.name
              }
            ]
          }
        ]
      }
    },
    initSalesChart() {
      this.salesChartOption = {
        xAxis: {
          type: 'category',
          data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            data: this.brand.salesData,
            type: 'line',
            smooth: true
          }
        ]
      }
    }
  }
}
</script>

<style scoped>
.brand-details {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-left: 20px;
}

.brand-info {
  flex: 1;
  margin-right: 40px;
}

.brand-name {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
}

.brand-sales {
  font-size: 16px;
  color: #666;
  margin-bottom: 20px;
}

.sales-amount {
  color: #0077b6;
  font-weight: bold;
}

.score-chart {
  width: 400px;
  height: 400px;
}

.brand-sales {
  flex: 1;
}

.sales-chart-title {
  font-size: 20px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
}

.sales-chart {
  width: 600px;
  height: 400px;
}
</style>
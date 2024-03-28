<template>
  <div class="brand-info-container">
    <div class="brand-sales-ranking">
      <div class="left-panel">
        <h3>品牌销量排行榜</h3>
        <ul>
          <li v-for="(brand, index) in brandSalesData" :key="index" @click="updateCurrentBrand(brand, index)" @mouseover="addShadow(index)" @mouseleave="removeShadow(index)">
            <span class="rank">{{ index + 1 }}.</span>
            <span class="brand-name">{{ brand.name }}</span>
            <span class="sales-volume">{{ brand.salesVolume }}</span>
          </li>
        </ul>
      </div>
      <div class="right-panel">
        <div class="brand-info">
          <div class="brand-details">
            <div class="brand-info-left">
              <h3>{{ brandDetails.name }}</h3>
              <p>厂商: {{ brandDetails.manufacturer }}</p>
              <p>车型: {{ brandDetails.model }}</p>
              <p>品牌: {{ brandDetails.brand }}</p>
              <p>价格: {{ brandDetails.price }}</p>
              <p>其他信息: {{ brandDetails.otherInfo }}</p>
            </div>
            <div class="hexagon-chart">
              <!-- Echarts 六边形图 -->
              <div id="hexagonChart" style="width: 100%; height: 300px;"></div>
            </div>
          </div>
        </div>
        <div class="sales-history">
          <h3>历史销量</h3>
          <div class="line-chart">
            <!-- Echarts 折线图 -->
            <div id="lineChart" style="width: 100%; height: 300px;"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  data() {
    return {
      brandSalesData: [
        {
          name: 'Brand A',
          salesVolume: 1000,
          radarData: [4300, 10000, 28000, 35000, 50000, 19000],
          lineChartData: [820, 932, 901, 934],
          manufacturer: 'ABC 公司',
          model: '轿车A型',
          brand: 'Brand A',
          price: '¥20,000',
          otherInfo: '该车型采用节能环保技术,操控性能优秀。'
        },
        {
          name: 'Brand B',
          salesVolume: 800,
          radarData: [3800, 12000, 25000, 32000, 48000, 22000],
          lineChartData: [780, 850, 920, 1000],
          manufacturer: 'XYZ 公司',
          model: '轿车B型',
          brand: 'Brand B',
          price: '¥25,000',
          otherInfo: '该车型配置豪华,适合家庭使用。'
        },
        {
          name: 'Brand C',
          salesVolume: 600,
          radarData: [3200, 9000, 24000, 30000, 45000, 20000],
          lineChartData: [650, 730, 800, 880],
          manufacturer: '123 公司',
          model: '轿车C型',
          brand: 'Brand C',
          price: '¥18,000',
          otherInfo: '该车型外观时尚,动力性能出色。'
        }
      ],
      currentBrand: {
        name: 'Brand A',
        radarData: [4300, 10000, 28000, 35000, 50000, 19000],
        lineChartData: [820, 932, 901, 934],
        manufacturer: 'ABC 公司',
        model: '轿车A型',
        brand: 'Brand A',
        price: '¥20,000',
        otherInfo: '该车型采用节能环保技术,操控性能优秀。'
      },
      currentIndex: 0,
      timer: null,
      brandDetails: {
        name: 'Brand A',
        manufacturer: 'ABC 公司',
        model: '轿车A型',
        brand: 'Brand A',
        price: '¥20,000',
        otherInfo: '该车型采用节能环保技术,操控性能优秀。'
      }
    }
  },
  mounted() {
    this.initHexagonChart()
    this.initLineChart()

  },
  methods: {
    updateCurrentBrand(brand, index) {
      this.currentBrand = brand
      this.currentIndex = index
      this.brandDetails = {
        name: brand.name,
        manufacturer: brand.manufacturer,
        model: brand.model,
        brand: brand.brand,
        price: brand.price,
        otherInfo: brand.otherInfo
      }
      this.initHexagonChart()
      this.initLineChart()
    },
    addShadow(index) {
      const li = document.querySelectorAll('.left-panel li')[index]
      li.style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.5)'
    },
    removeShadow(index) {
      const li = document.querySelectorAll('.left-panel li')[index]
      li.style.boxShadow = 'none'
    },
    initHexagonChart() {
      const hexagonChart = echarts.init(document.getElementById('hexagonChart'))
      hexagonChart.setOption({
        title: {
          text: '品牌指标',
          textStyle: {
            color: '#a09999'
          }
        },
        radar: {
          indicator: [
            {
              name: '销量',
              max: 6500,
              nameTextStyle: {
                fontSize: 16 // Increase the font size to 16
              }
            },
            {
              name: '市场占有率',
              max: 16000,
              nameTextStyle: {
                fontSize: 16
              }
            },
            {
              name: '客户满意度',
              max: 30000,
              nameTextStyle: {
                fontSize: 16
              }
            },
            {
              name: '品牌影响力',
              max: 38000,
              nameTextStyle: {
                fontSize: 16
              }
            },
            {
              name: '产品质量',
              max: 52000,
              nameTextStyle: {
                fontSize: 16
              }
            },
            {
              name: '服务水平',
              max: 25000,
              nameTextStyle: {
                fontSize: 16
              }
            }
          ],
        },
        series: [
          {
            name: this.currentBrand.name,
            type: 'radar',
            data: [
              {value: this.currentBrand.radarData, name: this.currentBrand.name}
            ]
          }
        ],
        tooltip: {
          trigger: 'item',
          formatter: (params) => {
            return `${params.name}<br>
          销量: ${params.value[0]}<br>
          市场占有率: ${params.value[1]}%<br>
          客户满意度: ${params.value[2]}<br>
          品牌影响力: ${params.value[3]}<br>
          产品质量: ${params.value[4]}<br>
          服务水平: ${params.value[5]}`;
          }
        },
        animationDuration: 2000,
        animationEasing: 'elasticOut',
        animationDelayUpdate: (idx) => idx * 100
      })
    },
    initLineChart() {
      const lineChart = echarts.init(document.getElementById('lineChart'))
      lineChart.setOption({

        xAxis: {
          type: 'category',
          data: ['2020', '2021', '2022', '2023'],
          axisLabel: {
            color: '#999999', // 设置 x 轴文字颜色为灰色
            fontSize: 18,
          }
        },
        yAxis: {
          type: 'value',
          axisLabel: {
            color: '#999999',// 设置 y 轴文字颜色为灰色
            fontSize: 18,

          }
        },
        series: [
          {
            data: this.currentBrand.lineChartData,
            type: 'line'
          }
        ],
        tooltip: {
          trigger: 'axis',
          formatter: (params) => {
            let str = `${params[0].name}<br>`;
            for (let i = 0; i < params.length; i++) {
              str += `销量: ${params[i].value}<br>`;
            }
            return str;
          }
        },
        animationDuration: 1000,
        animationEasing: 'linear',
        animationDelay: (idx) => idx * 100
      })
    }
  }
}
</script>

<style scoped>
.brand-info-container {
  position: relative;
  background-color: rgba(255, 255, 255, 0.18);
  padding: 20px;
}

.brand-sales-ranking {
  display: flex;
  justify-content: space-between;
  height: 150vh;
  padding: 20px;
  background-color: transparent;
}

.left-panel {
  flex: 0.5;
  background-color: transparent;
  padding: 20px;
  margin-right: 20px;
  border: 1px solid #ccc;
  transition: transform 0.3s ease;
}

.left-panel:hover {
  transform: translateY(-5px);
}

.left-panel ul {
  list-style-type: none;
  padding: 0;
}

.left-panel li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.left-panel li:hover {
  background-color: rgba(0, 0, 0, 1);
}

.right-panel {
  flex: 2;
  background-color: transparent;
  padding: 20px;
  border: 1px solid #ccc;
  transition: transform 0.3s ease;
}

.right-panel:hover {
  transform: translateY(-5px);
}

.brand-info,
.sales-history {
  margin-bottom: 20px;
}

.brand-details {
  display: flex;
  justify-content: space-between;
}

.brand-info-left {
  flex: 1;
  margin-right: 20px;
  font-size: 16px;
  line-height: 1.6;
}

.brand-info-left h3 {
  font-size: 20px;
  margin-bottom: 10px;
}

.brand-info-left p {
  margin-bottom: 10px;
}

.hexagon-chart {
  flex: 1;
}

.hexagon-chart,
.line-chart {
  border: 1px solid transparent;
  border-radius: 4px;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>
<template>
  <div class="brand-info-container">
    <div class="brand-sales-ranking">
      <div class="left-panel">
        <h3>品牌销量排行榜</h3>
        <ul>
          <li v-for="(car, index) in displayedCars" :key="index" @click="updateCurrentCar(car, index)"
              :class="{ 'active': currentIndex === index }">
            <span class="rank">{{ car.rank }}.</span>
            <span class="brand-name">{{ car.carName }}</span>
            <span class="sales-volume">{{ car.saleVolume }}</span>
          </li>
        </ul>
        <div class="pagination">
          <button @click="prevPage" :disabled="currentPage === 1">上一页</button>
          <span>第 {{ currentPage }} 页</span>
          <button @click="nextPage" :disabled="currentPage === totalPages">下一页</button>
        </div>
      </div>
      <div class="right-panel">
        <div class="brand-info">
          <div class="brand-details">
            <div class="brand-info-left">
              <h3>{{ currentCar.carName }}</h3>
              <div class="car-info-row">
                <p>制造商: {{ currentCar.manufacturer }}</p>
                <p>车型: {{ currentCar.carModel }}</p>
                <p>品牌: {{ currentCar.brand }}</p>
              </div>
              <div class="car-info-row">
                <p>价格: {{ currentCar.min_price }} - {{ currentCar.max_price }} 万元</p>
                <p>上市时间: {{ currentCar.marketTime }}</p>
                <p>综合评分: {{ currentCar.over_score }}</p>
              </div>
              <div class="car-image-container">
                <img :src="currentCar.carImg" :alt="currentCar.carName" class="car-image">
              </div>
            </div>
            <div class="hexagon-chart">
              <radar-chart :data="radarData"></radar-chart>
              <p>综合评价: {{ currentCar.comprehensive_evaluation }}</p>
            </div>

          </div>
          <div class="line-chart">
            <line-chart :data="historicalSalesData" :labels="historicalSalesLabels"></line-chart>
            <p>历史销量</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import RadarChart from '@/components/RadarChart.vue'
import LineChart from '@/components/LineChart.vue'

export default {
  components: {
    RadarChart,
    LineChart
  },
  data() {
    return {
      carData: [],
      currentCar: null,
      currentIndex: 0,
      radarData: [],
      currentPage: 1,
      pageSize: 17,
      historicalSales: [], // 新增历史销量数据属性

    }
  },
  computed: {
    totalPages() {
      return Math.ceil(this.carData.length / this.pageSize)
    },
    displayedCars() {
      const startIndex = (this.currentPage - 1) * this.pageSize
      const endIndex = startIndex + this.pageSize
      return this.carData.slice(startIndex, endIndex)
    }
  },
  mounted() {
    this.fetchCarData()
  },
  methods: {
    async fetchCarData() {
      const res = await this.$http.get('myapp/bottomRight')
      this.carData = res.data.carData

      const salesData = await this.$http.get('myapp/data4')
      this.historicalSales = salesData.data.carData4

      this.updateCurrentCar(this.carData[0], 0)
    },
    updateCurrentCar(car, index) {
      this.currentCar = car
      this.currentIndex = index
      this.radarData = [
        car.appearance_score,
        car.interior_score,
        car.configure_score,
        car.spatial_score,
        car.comfort_score,
        car.manipulating_score,
        car.motivation_score
      ]

      // 查找当前车型的历史销量数据
      this.currentCarHistoricalSales = this.historicalSales.filter(item => item.carName === car.carName)
      this.historicalSalesData = this.currentCarHistoricalSales.map(item => item.monthly_sales)
      this.historicalSalesLabels = this.currentCarHistoricalSales.map(item => item.years)
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++
      }
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

.left-panel li.active {
  background-color: rgba(0, 0, 0, 0.2);
}

.left-panel li:hover {
  background-color: rgba(0, 0, 0, 0.1);
}

.left-panel .brand-name {
  font-size: 16px;
}

.left-panel .sales-volume {
  font-size: 14px;
}

.pagination {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

.pagination button {
  padding: 5px 10px;
  margin: 0 5px;
  background-color: #f0f0f0;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.pagination button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
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

.brand-info {
  margin-bottom: 20px;
}

.brand-details {
  display: flex;
  justify-content: space-between;
}

.brand-info-left {
  flex: 1;
  margin-right: 20px;
  font-size: 20px;
  line-height: 1.6;
}

.brand-info-left h3 {
  font-size: 35px;
  margin-bottom: 10px;
}

.brand-info-left .car-info-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.brand-info-left .car-info-row p {
  flex: 1;
  margin-right: 10px;
}

.car-image-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.car-image {
  max-width: 100%;
  height: auto;
}

.hexagon-chart {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;

}

.hexagon-chart p {
  margin-top: 20px;
  font-size: 20px;
}

.left-panel ul {
  list-style-type: none;
  padding: 0;
}

.left-panel li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.left-panel li.active {
  background-color: rgba(0, 0, 0, 0.2);
}

.left-panel li:hover {
  background-color: rgba(0, 0, 0, 0.1);
}

.left-panel .brand-name {
  font-size: 16px;
  margin-right: 10px;
}

.left-panel .sales-volume {
  font-size: 14px;
}

</style>
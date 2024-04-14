<template>
  <div class="brand-info-container">
    <div class="brand-sales-ranking">
      <div class="left-panel">
        <h3>销量排行榜</h3>
        <div class="search-box">
          <input type="text" v-model="searchQuery" placeholder="搜索车型"/>
        </div>
        <ul>
          <li
              v-for="(car, index) in displayedCars"
              :key="index"
              @click="updateCurrentCar(car, index)"
              :class="{ 'active': currentIndex === index }"
          >
            <span class="rank" style="font-size: 26px">{{ car.rank }}.</span>
            <span class="brand-name">{{ car.carName }}</span>
            <span class="sales-volume">{{ car.brand }}</span>
          </li>
        </ul>
        <div class="pagination">
          <button @click="goToFirstPage" :disabled="currentPage === 1">首页</button>
          <button @click="prevPage" :disabled="currentPage === 1">上一页</button>
          <span>第 {{ currentPage }} 页 / 共 {{ totalPages }} 页</span>
          <button @click="nextPage" :disabled="currentPage === totalPages">下一页</button>
          <button @click="goToLastPage" :disabled="currentPage === totalPages">尾页</button>
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
                <p>价格: {{ currentCar.min_price }} - {{ currentCar.max_price }} 万</p>
                <p>上市时间: {{ currentCar.marketTime }}</p>
                <p>综合评分: {{ currentCar.over_score }}</p>
              </div>
              <div class="car-image-container">
                <img :src="currentCar.carImg" :alt="currentCar.carName" class="car-image"/>
              </div>
            </div>
            <div class="hexagon-chart">
              <radar-chart :data="radarData"></radar-chart>
              <div class="comprehensive-evaluation">
                <h2>综合评价</h2>
                <dv-scroll-ranking-board :config="config" style="width:400px;height:200px"/>
                <div class="evaluation-type-switch">
                  <button @click="showPositiveEvaluation = true" :class="{ 'active': showPositiveEvaluation }">
                    好评
                  </button>
                  <button @click="showPositiveEvaluation = false" :class="{ 'active': !showPositiveEvaluation }">
                    差评
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div class="line-chart">
            <line-chart :data="historicalSalesData.slice().reverse()"
                        :labels="historicalSalesLabels.slice().reverse()"></line-chart>
            <h2>历史销量</h2>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import RadarChart from '@/components/RadarChart.vue'
import LineChart from '@/components/LineChart.vue'
import DvScrollRankingBoard from '@/components/DvScrollRankingBoard.vue'

export default {
  components: {
    RadarChart,
    LineChart,
    DvScrollRankingBoard
  },
  data() {
    return {
      carData: [],
      currentCar: null,
      currentIndex: 0,
      radarData: [],
      currentPage: 1,
      pageSize: 16,
      historicalSales: [],
      searchQuery: '',
      showPositiveEvaluation: true,
      positiveEvaluations: [],
      negativeEvaluations: [],
      config: {
        data: [],
        waitTime: 1000
      },
      // 添加缓存
      carDataCache: null,
      historicalSalesCache: null
    }
  },
  computed: {
    totalPages() {
      return Math.ceil(this.filteredCars.length / this.pageSize)
    },
    filteredCars() {
      return this.carData.filter(car =>
          car.carName.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          car.brand.toLowerCase().includes(this.searchQuery.toLowerCase())
      )
    },
    displayedCars() {
      const startIndex = (this.currentPage - 1) * this.pageSize
      const endIndex = startIndex + this.pageSize
      return this.filteredCars.slice(startIndex, endIndex)
    },
    displayedEvaluations() {
      return this.showPositiveEvaluation ? this.positiveEvaluations : this.negativeEvaluations
    }
  },
  watch: {
    showPositiveEvaluation() {
      this.updateEvaluationConfig()
    }
  },
  mounted() {
    this.fetchCarData();
  },
  methods: {
    async fetchCarData() {
      // 先检查缓存
      if (this.carDataCache && this.historicalSalesCache) {
        this.carData = this.carDataCache;
        this.historicalSales = this.historicalSalesCache;
        this.parseComprehensiveEvaluation(this.carData[0].comprehensive_evaluation);
        this.updateCurrentCar(this.carData[0], 0);
      } else {
        const res = await this.$http.get('myapp/bottomRight')
        this.carData = res.data.carData;
        this.carDataCache = res.data.carData; // 缓存数据

        const salesData = await this.$http.get('myapp/data4')
        this.historicalSales = salesData.data.carData4;
        this.historicalSalesCache = salesData.data.carData4; // 缓存数据

        this.parseComprehensiveEvaluation(this.carData[0].comprehensive_evaluation);
        this.updateCurrentCar(this.carData[0], 0);
      }
    },
    updateCurrentCar(car, index) {
      this.currentCar = car;
      this.currentIndex = index;
      this.radarData = [
        car.appearance_score,
        car.interior_score,
        car.configure_score,
        car.spatial_score,
        car.comfort_score,
        car.manipulating_score,
        car.motivation_score
      ];

      // 查找当前车型的历史销量数据
      this.currentCarHistoricalSales = this.historicalSales.filter(item => item.carName === car.carName);
      this.historicalSalesData = this.currentCarHistoricalSales.map(item => item.monthly_sales);
      this.historicalSalesLabels = this.currentCarHistoricalSales.map(item => item.years);

      // 更新综合评价数据
      this.parseComprehensiveEvaluation(car.comprehensive_evaluation);
      this.updateEvaluationConfig();
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
    },
    goToFirstPage() {
      this.currentPage = 1
    },
    goToLastPage() {
      this.currentPage = this.totalPages
    },
    parseComprehensiveEvaluation(evaluationString) {
      const evaluations = evaluationString.slice(2, -2).split("', '");
      this.positiveEvaluations = evaluations.slice(0, 12).map((item, index) => {
        const [content, score] = item.split("（");
        return {rank: index + 1, content, score: score.slice(0, -1)};
      });
      this.negativeEvaluations = evaluations.slice(12).map((item, index) => {
        const [content, score] = item.split("（");
        return {rank: index + 1, content, score: score.slice(0, -1)};
      });

      this.updateEvaluationConfig();
    },
    updateEvaluationConfig() {
      this.config.data = this.displayedEvaluations;
    },

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
  flex: 0.6;
  background-color: transparent;
  padding: 20px;
  border: 1px solid #ccc;
  transition: transform 0.3s ease;
}

.left-panel:hover {
  transform: translateY(-5px);
}

.left-panel .search-box {
  margin-bottom: 20px;

}

.left-panel .search-box input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  background-color: #1c2138;
  color: white;
}
.left-panel .search-box input::placeholder {
  color: #faf7f7; /* 设置placeholder文字颜色为白色 */
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
  font-size: 20px;
  margin-right: 10px;
}

.left-panel .sales-volume {
  font-size: 20px;
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

.comprehensive-evaluation {
  margin-top: 20px;
  text-align: center;
}

.comprehensive-evaluation h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

.evaluation-type-switch {
  display: flex;
  justify-content: center;
  margin-bottom: 10px;
}

.evaluation-type-switch button {
  padding: 5px 10px;
  margin: 0 5px;
  background-color: #f0f0f0;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.evaluation-type-switch button.active {
  background-color: #ccc;
}

.evaluation-carousel {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  height: 150px;
  overflow: hidden;
}

.evaluation-item {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 150px;
  height: 75px;
  margin: 5px;
  background-color: #f0f0f0;
  border-radius: 5px;
  font-size: 14px;
  animation: carousel 10s linear infinite;
}

.evaluation-text {
  font-weight: bold;
  margin-bottom: 5px;
}

.evaluation-count {
  color: #888;
}

@keyframes carousel {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-100%);
  }
}
</style>
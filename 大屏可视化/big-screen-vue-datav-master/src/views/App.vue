<template>
  <div id="app">
    <div class="container">
      <div class="left-panel">
        <div
          v-for="(brand, index) in brands"
          :key="index"
          class="brand-item"
          :class="{ 'active': currentBrand === brand }"
          @click="showBrandDetails(brand)"
        >
          {{ brand.name }}
        </div>
      </div>
      <div class="right-panel">
        <div v-if="currentBrand">
          <div class="chart-container">
            <line-chart :data="currentBrand.sales"></line-chart>
          </div>
          <div class="brand-details">
            <h2>{{ currentBrand.name }}</h2>
            <p>{{ currentBrand.description }}</p>
            <p>Sales: {{ currentBrand.sales.reduce((total, sale) => total + sale, 0) }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LineChart from '../components/echart/app/LineChart.vue'

export default {
  name: 'App',
  components: {
    LineChart
  },
  data() {
    return {
      brands: [
        {name: 'Brand A', description: 'This is Brand A', sales: [100, 120, 150, 180, 200]},
        {name: 'Brand B', description: 'This is Brand B', sales: [80, 90, 110, 130, 150]},
        {name: 'Brand C', description: 'This is Brand C', sales: [60, 70, 80, 90, 100]}
      ],
      currentBrand: {name: '', description: '', sales: []}
    }
  },
  mounted() {
    if (this.brands.length > 0) {
      this.showBrandDetails(this.brands[0])
    }
  },
  methods: {
    showBrandDetails(brand) {
      this.currentBrand = brand
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  height: 100vh;
}

.left-panel {
  flex: 1;
  background-color: #f1f1f1;
  padding: 20px;
}

.brand-item {
  padding: 10px;
  cursor: pointer;
}

.brand-item.active {
  background-color: #ddd;
}

.right-panel {
  flex: 2;
  padding: 20px;
}

.chart-container {
  height: 300px;
}

.brand-details {
  margin-top: 20px;
}
</style>
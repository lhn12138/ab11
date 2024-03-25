<template>
  <div id="app">
    <div class="app-container">
      <div class="brand-ranking-container">
        <BrandRanking :brands="brands" @brand-selected="handleBrandSelected" />
      </div>
      <div class="brand-details-container">
        <BrandDetails v-if="selectedBrand" :brand="selectedBrand" />
        <div v-else class="no-brand-selected">请选择一个品牌查看详情</div>
      </div>
    </div>
  </div>
</template>

<script>
import BrandRanking from '../components/BrandRanking.vue';
import BrandDetails from '../components/BrandDetails.vue';

export default {
  name: 'App',
  components: {
    BrandRanking,
    BrandDetails
  },
  data() {
    return {
      selectedBrand: null,
      brands: [
        {
          name: 'Brand A',
          sales: 1000,
          score: {
            quality: 4.5,
            price: 4.2,
            service: 4.8,
            innovation: 4.3,
            design: 4.6,
            reputation: 4.7
          },
          salesData: [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        },
        {
          name: 'Brand B',
          sales: 800,
          score: {
            quality: 4.2,
            price: 4.5,
            service: 4.1,
            innovation: 4.0,
            design: 4.3,
            reputation: 4.4
          },
          salesData: [80, 160, 240, 320, 400, 480, 560, 640, 720, 800]
        },
        {
          name: 'Brand C',
          sales: 600,
          score: {
            quality: 4.0,
            price: 4.1,
            service: 3.9,
            innovation: 4.2,
            design: 4.0,
            reputation: 4.1
          },
          salesData: [60, 120, 180, 240, 300, 360, 420, 480, 540, 600]
        }
      ]
    };
  },
  methods: {
    handleBrandSelected(brand) {
      this.selectedBrand = brand;
    }
  }
};
</script>

<style>
.app-container {
  display: flex;
  justify-content: space-between;
  background-color: #f5f5f5;
  padding: 40px;
}

.brand-ranking-container {
  width: 25%;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.brand-details-container {
  width: 70%;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.no-brand-selected {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  font-size: 18px;
  color: #666;
}
</style>
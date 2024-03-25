<template>
  <div class="brand-ranking-container">
    <div class="brand-ranking">
      <h2 class="ranking-title">品牌销量排行榜</h2>
      <ul class="brand-list">
        <li
          v-for="brand in brands"
          :key="brand.name"
          class="brand-item"
          @click="selectBrand(brand)"
        >
          <div class="brand-name">{{ brand.name }}</div>
          <div class="brand-sales">销量: {{ brand.sales }}</div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BrandRanking',
  props: {
    brands: {
      type: Array,
      required: true
    }
  },
  methods: {
    selectBrand(brand) {
      this.$emit('brand-selected', brand);
    }
  }
};
</script>

<style scoped>
.brand-ranking-container {
  background-color: #f5f5f5;
  padding: 40px;
}

.brand-ranking {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.ranking-title {
  font-size: 20px;
  font-weight: bold;
  color: #333;
  margin-bottom: 20px;
}

.brand-list {
  list-style: none;
  padding: 0;
}

.brand-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  padding: 10px 0;
  border-bottom: 1px solid #f0f0f0;
}

.brand-item:last-child {
  border-bottom: none;
}

.brand-name {
  font-size: 16px;
  color: #333;
}

.brand-sales {
  font-size: 14px;
  color: #666;
}
</style>
<template>
  <div class="brand-ranking">
    <h2>品牌销量排行榜</h2>
    <ul>
      <li v-for="brand in brands" :key="brand.name" @click="selectBrand(brand)">
        {{ brand.name }} - 销量: {{ brand.sales }}
      </li>
    </ul>
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
.brand-ranking {
  width: 200px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  cursor: pointer;
  margin-bottom: 10px;
}
</style>
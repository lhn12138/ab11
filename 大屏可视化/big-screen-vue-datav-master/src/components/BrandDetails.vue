<template>
  <div class="brand-details">
    <div class="brand-info">
      <h2>{{ brand.name }} 品牌详情</h2>
      <p>销售总额: {{ brand.sales }}</p>
      <!-- 使用 brand.score 渲染六边形评分图 -->
      <div ref="scoreChart" style="width: 400px; height: 400px;"></div>
    </div>
    <div class="brand-sales">
      <h3>{{ brand.name }} 销量折线图</h3>
      <!-- 使用 brand.salesData 渲染销量折线图 -->
      <div ref="salesChart" style="width: 600px; height: 400px;"></div>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts';


export default {
  name: 'BrandDetails',
  props: {
    brand: {
      type: Object,
      required: true
    }
  },
  mounted() {
    this.initScoreChart();
    this.initSalesChart();
  },
  methods: {
    initScoreChart() {
      const chart = echarts.init(this.$refs.scoreChart);
      const option = {
        // 配置六边形评分图的选项
        // ...
      };
      chart.setOption(option);
    },
    initSalesChart() {
      const chart = echarts.init(this.$refs.salesChart);
      const option = {
        // 配置销量折线图的选项
        // ...
      };
      chart.setOption(option);
    }
  }
};
</script>

<style scoped>
.brand-details {
  flex: 1;
  margin-left: 20px;
}

.brand-info {
  margin-bottom: 20px;
}

.brand-sales {
  margin-top: 20px;
}
</style>
<template>
  <div id="app1">
    <div class="container">
      <h1>对品牌未上市的车进行周销量预测</h1>
      <div class="form-group">
        <label>品牌:</label>
        <select v-model="selectedBrand" @change="onBrandChange" class="form-control">
          <option v-for="brand in brands" :value="brand" :key="brand">{{ brand }}</option>
        </select>
      </div>
      <div class="form-group">
        <label>车型:</label>
        <select v-model="selectedModel" @change="onModelChange" class="form-control">
          <option v-for="model in models" :value="model" :key="model">{{ model }}</option>
        </select>
      </div>
      <div class="form-group">
        <label>价格区间:</label>
        <select v-model="selectedPriceRange" class="form-control">
          <option v-for="priceRange in priceRanges" :value="priceRange" :key="priceRange">{{ priceRange }}</option>
        </select>
      </div>
      <div class="form-group">
        <label>能源类型:</label>
        <select v-model="selectedEnergyType" class="form-control">
          <option v-for="energyType in energyTypes" :value="energyType" :key="energyType">{{ energyType }}</option>
        </select>
      </div>
      <button @click="predictSales" class="btn btn-primary">销量预测</button>
      <div v-if="showPredictedSales" class="result">
        预测销量: {{ predictedSales }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App1",
  data() {
    return {
      brands: [],
      models: [],
      priceRanges: [],
      energyTypes: [],
      selectedBrand: null,
      selectedModel: null,
      selectedPriceRange: null,
      selectedEnergyType: null,
      predictedSales: null,
      showPredictedSales: false
    }
  },
  async created() {
    // 从后端获取初始数据
    const res = await this.$http.get("myapp/predict22/");
    this.initData(res.data);
  },
  methods: {
    initData(data) {
      // 初始化下拉框选项
      this.brands = [...new Set(data.map(item => item.brand))];
      this.models = [...new Set(data.map(item => item.car_model))];
      this.priceRanges = [...new Set(data.map(item => item.price_range))];
      this.energyTypes = [...new Set(data.map(item => item.energy_type))];
    },
    onBrandChange() {
      // 根据选择的品牌更新车型下拉框
      this.models = [...new Set(this.data.filter(item => item.brand === this.selectedBrand).map(item => item.car_model))];
    },
    onModelChange() {
      // 根据选择的车型更新其他下拉框
      this.priceRanges = [...new Set(this.data.filter(item => item.car_model === this.selectedModel).map(item => item.price_range))];
      this.energyTypes = [...new Set(this.data.filter(item => item.car_model === this.selectedModel).map(item => item.energy_type))];
    },
    async predictSales() {
      // 根据选择的条件从后端获取预测结果
      const res = await this.$http.get("myapp/predict22/")
      this.cars = res.data.List;
    }

  }
}
</script>
<style>
.container {
  max-width: 800px;
  margin: 5px auto;
  padding: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-control {
  display: block;
  width: 100%;
  padding: 0.5rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  color: #495057;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ced4da;
  border-radius: 0.25rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

.btn {
  display: inline-block;
  font-weight: 400;
  color: #fff;
  text-align: center;
  vertical-align: middle;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  background-color: #007bff;
  border: 1px solid #007bff;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: 0.25rem;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

.btn:hover {
  color: #fff;
  background-color: #0056b3;
  border-color: #004a9b;
}

.result {
  margin-top: 2rem;
  font-size: 1.2rem;
  font-weight: bold;
}
</style>
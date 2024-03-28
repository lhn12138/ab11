<template>
  <div id="app">
    <div class="container">
      <h1 class="title">车型销量预测</h1>
      <div class="search-container">
        <div class="search-box">
          <input type="text" v-model="searchText" placeholder="搜索车型" class="search-input" />
          <button @click="predictSales" class="search-button">
            <i class="fas fa-search"></i>
            销量预测
          </button>
        </div>
        <select v-model="selectedCar" class="select-box">
          <option v-for="car in filteredCars" :value="car[0]" :key="car[0]">{{ car[0] }}</option>
        </select>
      </div>
      <div v-if="predictedSales" class="result-container">
        <div class="result-box">
          <p class="result-text">
            基于前 {{ predictedSales[2] }} 个月的销量进行预测,预测下个月销量为
            {{ predictedSales[1] }}。
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      cars: [],
      searchText: "",
      selectedCar: null,
      predictedSales: null,
    };
  },
  async mounted() {
    const res = await this.$http.get("myapp/predict2");
    this.cars = res.data.List;
  },
  computed: {
    filteredCars() {
      return this.cars.filter((car) =>
        car[0].toLowerCase().includes(this.searchText.toLowerCase())
      );
    },
  },
  methods: {
    predictSales() {
      this.predictedSales = this.cars.find(
        (car) => car[0] === this.selectedCar
      );
    },
  },
};
</script>

<style>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  background-color: #f5f5f5;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.title {
  text-align: center;
  margin-bottom: 2rem;
  color: #333;
  font-size: 2.5rem;
  font-weight: bold;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
}

.search-container {
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
}

.search-box {
  display: flex;
  align-items: center;
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  margin-right: 1rem;
  flex-grow: 1;
}

.search-input {
  padding: 0.75rem 1rem;
  border: none;
  border-radius: 4px 0 0 4px;
  font-size: 1rem;
  flex-grow: 1;
  background-color: #f5f5f5;
  transition: background-color 0.3s;
}

.search-input:focus {
  background-color: #fff;
  outline: none;
}

.search-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0 4px 4px 0;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.search-button:hover {
  background-color: #0056b3;
}

.select-box {
  padding: 0.75rem 1rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #fff;
  cursor: pointer;
  transition: border-color 0.3s;
}

.select-box:focus {
  outline: none;
  border-color: #007bff;
}

.result-container {
  margin-top: 2rem;
}

.result-box {
  background-color: #fff;
  padding: 1.5rem;
  border-radius: 4px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.result-text {
  font-size: 1.2rem;
  color: #333;
  line-height: 1.5;
}
</style>
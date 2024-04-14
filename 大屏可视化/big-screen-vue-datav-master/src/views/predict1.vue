<template>
  <div id="app">
    <div class="container">
      <h1 class="title">车型销量预测</h1>
      <div class="search-container">
        <div class="search-box">
          <input type="text" v-model="searchText" placeholder="搜索车型" style="color: white" class="search-input"/>
          <div class="suggestion-box" v-if="suggestedCars.length > 0">
            <div
                class="suggestion-item"
                v-for="car in suggestedCars"
                :key="car[0]"
                @click="selectCar(car[0])"
            >
              {{ car[0] }}
            </div>
          </div>
          <div class="button-container">
            <div class="button-row">
              <button @click="predictSales" class="search-button">
                <i class="fas fa-search"></i>
                销量预测
              </button>
              <button @click="clearSearchText" class="clear-button" v-if="predictedSales">
                清空
              </button>
            </div>
          </div>
        </div>
      </div>
      <div v-if="predictedSales" class="result-container">
        <div class="result-box">
          <p class="result-text">
            基于前 {{ predictedSales[2] }} 个月的新车销量进行预测,预测下个月新车销量为
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
      predictedSales: null,
      carsCache: []
    };
  },
  async mounted() {
    await this.fetchCars();
  },
  computed: {
    suggestedCars() {
      return this.cars.filter((car) =>
          car[0].toLowerCase().includes(this.searchText.toLowerCase())
      );
    },
  },
  methods: {
    async fetchCars() {
      if (this.carsCache.length === 0) {
        const res = await this.$http.get("myapp/predict2");
        this.cars = res.data.List;
        this.carsCache = res.data.List;
      } else {
        this.cars = this.carsCache;
      }
    },
    selectCar(carName) {
      this.searchText = carName;
    },
    predictSales() {
      if (!this.searchText) {
        // 弹出提示
        alert("请选择要预测的车型");
        return;
      }
      this.predictedSales = this.cars.find(
          (car) => car[0] === this.searchText
      );
    },
    clearSearchText() {
      this.searchText = "";
      this.predictedSales = null;
    },
  },
};
</script>

<style>
.container {
  max-width: 400px;
  max-height: 500px;
  margin: 0px auto;
  border-radius: 5px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  background-color: rgba(19, 25, 47, 0.6);
  padding: 16px;
  padding-top: 20px;
}

.title {
  text-align: center;
  margin-bottom: 2rem;
  color: #fcf8f8;
  font-size: 2.0rem;
  font-weight: bold;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
}

.search-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 2rem;
}

.search-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}

.search-input {
  padding: 0.75rem 1rem;
  border: none;
  border-radius: 4px 4px 0 0;
  font-size: 1rem;
  flex-grow: 1;
  background-color: #1c2138;
  transition: background-color 0.3s;
  width: 100%;
}

.search-input:focus {
  background-color: #1c2138;
  outline: none;
}

.suggestion-box {
  background-color: #1c2138;
  border: 1px solid #ccc;
  border-top: none;
  border-radius: 0 0 4px 4px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-height: 200px;
  overflow-y: auto;
}

.suggestion-item {
  padding: 0.75rem 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
  font-size: 1.1rem;
  color: #fffdfd;
}

.suggestion-item:hover {
  background-color: #2a2e46;
}

.button-container {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.button-row {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.search-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0 0 0 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
  flex-grow: 1;
}

.search-button:hover {
  background-color: #0056b3;
}

.clear-button {
  background-color: #dc3545;
  color: #fff;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0 0 4px 0;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
  flex-grow: 1;
}

.clear-button:hover {
  background-color: #c82333;
}

.result-container {
  margin-top: 2rem;
  display: flex;
  justify-content: center;
  position: absolute;
  bottom: 0;
  width: 85%;
}

.result-box {
  background-color: #494c59;
  padding: 1.5rem;
  border-radius: 4px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}

.result-text {
  font-size: 1.2rem;
  color: #ffffff;
  line-height: 1.5;
}

.search-container input::placeholder {
  color: #fff; /* 设置placeholder文字颜色为白色 */
}
</style>
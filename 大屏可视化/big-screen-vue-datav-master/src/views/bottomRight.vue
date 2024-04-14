<template>
  <div id="bottomRight">
    <div class="bg-color-black">
      <div class="d-flex pt-2 pl-2">
        <span>
          <icon name="chart-area" class="text-icon"></icon>
        </span>
        <div class="d-flex">
          <span class="fs-xl text mx-2"><h1 style="font-size: 27px;">品牌年份排行榜</h1></span>
          <div class="decoration2">
            <dv-decoration-2 :reverse="true" style="width:5px;height:6rem;"/>
          </div>

          <div class="search-box ml-auto mr-2">
            <input type="text" v-model="searchKeyword" placeholder="请输入年份、国家或品牌搜索"
                   class="large-input">
          </div>
        </div>
      </div>
      <div class="row_list">
        <ul class="car_rank" :style="{maxHeight: '450px', overflowY: 'auto'}">
          <li class="header">
            <div style="font-size: 20px">销售排名</div>
            <div style="font-size: 20px">年份</div>
            <div style="font-size: 20px">Logo</div>
            <div style="font-size: 20px">品牌信息</div>
            <div style="font-size: 20px">销量</div>
          </li>
          <li v-for="(car, index) in sortedFilteredCarData" :key="index">
            <div class="list_index1" style="font-size: 25px">{{ car.rank }}</div>
            <div class="list_index" style="font-size: 25px">{{ car.year }}</div>
            <div class="list_img"><img :src="car.logo" alt=""></div>
            <div class="list_info" style="font-size: 25px">
              <p>{{ car.country }}/{{ car.brand }}</p>
            </div>
            <div class="list_saleVolume" style="font-size: 25px">{{ car.sales }}辆</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      CarData: [],
      searchKeyword: '',
      sortedFilteredCarData: [],
      carDataCache: []
    }
  },
  computed: {
    filteredCarData() {
      const keyword = this.searchKeyword.toLowerCase();
      return this.CarData.filter(car =>
        car.year.toString().includes(keyword) ||
        car.country.toLowerCase().includes(keyword) ||
        car.brand.toLowerCase().includes(keyword)
      );
    }
  },
  watch: {
    filteredCarData() {
      this.sortCarData();
    }
  },
  async mounted() {
    await this.fetchCarData();
    this.sortCarData();
  },
  methods: {
    async fetchCarData() {
      if (this.carDataCache.length === 0) {
        const res = await this.$http.get('myapp/getData');
        this.CarData = res.data.carData1;
        this.carDataCache = res.data.carData1;
      } else {
        this.CarData = this.carDataCache;
      }
    },
    sortCarData() {
      this.sortedFilteredCarData = this.filteredCarData.slice().sort((a, b) => {
        if (a.year !== b.year) {
          return b.year - a.year;
        } else {
          return a.rank - b.rank;
        }
      });
    }
  }
};
</script>

<style lang="scss" class>
$box-height: 520px;
$box-width: 100%;
#bottomRight {
  padding: 14px 16px;
  height: $box-height;
  width: $box-width;
  border-radius: 5px;

  .bg-color-black {
    height: $box-height - 30px;
    border-radius: 10px;
    position: relative; // 添加这一行
  }

  .text {
    color: #c3cbde;
  }

  //下滑线动态
  .decoration2 {
    position: absolute;
    right: 0.125rem;
  }

  .chart-box {
    margin-top: 16px;
    width: 170px;
    height: 170px;

    .active-ring-name {
      padding-top: 10px;
    }
  }

  //列表
}

.search-box {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  position: absolute;
  top: 10px;
  right: 10px;
  z-index: 1; // 添加这一行
  background-color: #1c2138;
}

.large-input {
  padding: 10px;
  width: 200px; /* 调整宽度 */
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #1c2138;
  color: white;
}
.search-box input::placeholder {
  color: #fff; /* 设置placeholder文字颜色为白色 */
}
.row_list {
  list-style: none;
  padding-top: 5px; // 添加这一行

  .car_rank::-webkit-scrollbar {
    width: 13px; /* 滚动条宽度 */
  }

  .car_rank::-webkit-scrollbar-track {
    background-color: #655b5b; /* 滚动条轨道颜色 */
  }

  .car_rank::-webkit-scrollbar-thumb {
    background-color: #888; /* 滚动条滑块颜色 */
    border-radius: 5px; /* 滚动条滑块圆角 */
    height: 50px; /* 滚动条滑块长度 */
  }

  .car_rank::-webkit-scrollbar-thumb:hover {
    background-color: #555; /* 滚动条滑块悬停颜色 */
  }

  .car_rank li {
    display: grid;
    grid-template-columns: 100px 100px 160px 160px 160px 110px 100px;
    cursor: pointer;
    margin-left: 23px;
    margin-bottom: 10px;
    text-align: center;
    line-height: 30px;
  }

  .car_rank .list_index {
    font-size: 18px;
    line-height: 70px;
    font-weight: bold;
  }

  .car_rank .list_index1 {
    font-size: 18px;
    line-height: 70px;
    font-weight: bold;
  }

  .car_rank .list_img {
    width: 170px;
    height: 80px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .car_rank .list_img img {
    max-width: 100%;
    max-height: 100%;
  }

  .car_rank.list_price {
    line-height: 60px;
  }

  .car_rank.list_saleVolume {
    line-height: 60px;
  }

  .car_rank.list_over_score {
    line-height: 60px;
  }

  .car_rank.list_marketTime {
    line-height: 60px;
  }
}

</style>
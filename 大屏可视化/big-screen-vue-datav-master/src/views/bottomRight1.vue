<template>
  <div id="bottomRight1">
    <div class="bg-color-black">
      <div class="d-flex pt-2 pl-2">
        <span>
          <icon name="chart-area" class="text-icon"></icon>
        </span>
        <div class="d-flex">
          <span class="fs-xl text mx-2"><h1 style="font-size: 27px;">品牌月份排行榜</h1></span>
          <div class="decoration2">
            <dv-decoration-2 :reverse="true" style="width:5px;height:6rem;"/>
          </div>
          <div class="search-box ml-auto mr-2">
            <input type="text" v-model="searchKeyword" placeholder="请输入年月、国家或品牌搜索"
                   class="large-input">
          </div>
        </div>
      </div>
      <div class="row_list">
        <ul class="car_rank" :style="{maxHeight: '450px', overflowY: 'auto'}">
          <li class="header">
            <div style="font-size: 20px">销售排名</div>
            <div style="font-size: 20px">年月</div>
            <div style="font-size: 20px">Logo</div>
            <div style="font-size: 20px">品牌信息</div>
            <div style="font-size: 20px">销量</div>
          </li>
          <li v-for="car in sortedFilteredCarData" :key="`${car.years}-${car.brand}`">
            <div class="list_index1" style="font-size: 25px">{{ car.rank }}</div>
            <div class="list_index" style="font-size: 25px">{{ car.years }}</div>
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
      carDataCache: [],
      currentPage: 1,
      pageSize: 10,
      totalPages: 0
    }
  },
  computed: {
    filteredCarData() {
      const keyword = this.searchKeyword.toLowerCase();
      return this.CarData.filter(car =>
        car.years.toString().includes(keyword) ||
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
    await this.fetchCarData(1);
    this.sortCarData();
  },
  methods: {
    async fetchCarData(page) {
      const res = await this.$http.get(`myapp/data1?page=${page}&pageSize=${this.pageSize}`);
      this.CarData = res.data.carData2.sort((a, b) => {
        const [yearA, monthA] = a.years.split('-').map(Number);
        const [yearB, monthB] = b.years.split('-').map(Number);
        if (yearA !== yearB) {
          return yearB - yearA;
        } else if (monthA !== monthB) {
          return monthB - monthA;
        } else {
          return a.rank - b.rank;
        }
      });
      this.carDataCache = this.CarData;
      this.currentPage = page;
      this.totalPages = Math.ceil(res.data.totalCount / this.pageSize);
    },
    sortCarData() {
      this.sortedFilteredCarData = this.filteredCarData.slice();
    },
    async changePage(page) {
      await this.fetchCarData(page);
      this.sortCarData();
    }
  }
};
</script>

<style lang="scss" class>
$box-height: 520px;
$box-width: 100%;
#bottomRight1 {
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
}

.large-input {
  padding: 10px;
  width: 200px; /* 调整宽度 */
  border: 1px solid #ccc;
  border-radius: 5px;
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

  .car_rank .list_img {
    width: 170px;
    height: 80px;
    display: flex;
    justify-content: center;
    align-items: center;
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
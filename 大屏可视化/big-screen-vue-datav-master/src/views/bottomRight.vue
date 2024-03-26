<template>
  <div id="bottomRight">
    <div class="bg-color-black">
      <div class="d-flex pt-2 pl-2">
        <span>
          <icon name="chart-area" class="text-icon"></icon>
        </span>
        <div class="d-flex">
          <span class="fs-xl text mx-2"><h1 style="font-size: 27px;">汽车排行榜</h1></span>
          <div class="decoration2">
            <dv-decoration-2 :reverse="true" style="width:5px;height:6rem;"/>
          </div>
          <div class="search-box ml-auto mt-2 mr-2">
            <input type="text" v-model="searchKeyword" placeholder="请输入车名、制造商或品牌进行搜索" class="large-input">
          </div>
        </div>
      </div>
      <div class="row_list">
        <ul class="car_rank" :style="{maxHeight: '450px', overflowY: 'auto'}">
          <li class="header">
            <div>销售排名</div>
            <div>图片</div>
            <div>汽车信息</div>
            <div>销售价格</div>
            <div>销售趋势</div>
            <div>综合评分</div>
            <div>上市时间</div>
          </li>
          <li v-for="car in filteredCarData" :key="car.rank">
            <div class="list_index">{{ car.rank }}</div>
            <div class="list_img"><img :src="car.carImg" alt=""></div>
            <div class="list_info">
              <p>{{ car.carName }}</p>
              <p>{{ car.manufacturer }}/{{ car.brand }}</p>
            </div>
            <div class="list_price">{{ car.price }}万元</div>
            <div class="list_saleVolume">{{ car.saleVolume }}辆</div>
            <div class="list_over_score">{{ car.over_score }}</div>
            <div class="list_marketTime">{{ car.marketTime }}</div>
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
      carData: [],
      searchKeyword: ''
    }
  },
  computed: {
    filteredCarData() {
      if (!this.searchKeyword) {
        return this.carData;
      } else {
        const keyword = this.searchKeyword.toLowerCase();
        return this.carData.filter(car =>
          car.carName.toLowerCase().includes(keyword) ||
          car.manufacturer.toLowerCase().includes(keyword) ||
          car.brand.toLowerCase().includes(keyword)
        );
      }
    }
  },
  async mounted() {
    const res = await this.$http.get('myapp/bottomRight');
    this.carData = res.data.carData;
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
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  position: absolute;
  top: 10px;
  right: 10px;
  z-index: 1; // 添加这一行
}

.large-input {
  padding: 10px;
  width: 300px; /* 调整宽度 */
  border: 1px solid #ccc;
  border-radius: 5px;
}

.row_list {
  list-style: none;
  padding-top: 50px; // 添加这一行

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
    -ms-grid-columns: 100px 100px 180px 120px 120px 110px 100px;
    grid-template-columns: 100px 100px 180px 120px 120px 110px 100px;
    cursor: pointer;
    margin-left: 23px;
    text-align: center;
    line-height: 30px;
  }

  .car_rank .list_index {
    font-size: 21px;
    line-height: 70px;
    font-weight: bold;
  }

  .car_rank .list_img {
    width: 100px;
    height:70px;

    img {
      max-width: 140%;
      max-height: 140%;
    }
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
<template>
  <div id="centerRight2">
    <div class="bg-color-black">
      <div class="d-flex pt-2 pl-2">
        <span>
          <icon name="align-left" class="text-icon"></icon>
        </span>
        <span class="fs-xl text mx-2" style="font-size: 28px;">汽车销售价格分布</span>
      </div>
      <div class="d-flex ai-center flex-column body-box">
        <dv-capsule-chart class="dv-cap-chart" :config="config" v-bind:key="config.data[1].value"
                          style="height: 300px" />
        <dv-active-ring-chart :config="configTwo" style="width:280px;height:180px;"
                              v-bind:key="configTwo.data[0].value" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      config: {
        data: [
          {
            name: '南阳',
            value: 167
          },
          {
            name: '周口',
            value: 67
          },
          {
            name: '漯河',
            value: 123
          },
          {
            name: '郑州',
            value: 55
          },
          {
            name: '西峡',
            value: 98
          }
        ],
        unit: '台',
        titleStyle: {
          fontSize: 14
        }
      },
      configTwo: {
        data: [
          {
            name: '南阳',
            value: 167
          }
        ],
        radius: '70%',
        activeRadius: '90%'
      }
    }
  },
  async mounted() {
    const res = await this.$http.get('myapp/centerRight')
    this.$set(this.config, 'data', res.data.realData)
    this.$set(this.configTwo, 'data', res.data.realData)
  }
}
</script>

<style lang="scss" scoped>
#centerRight2 {
  $box-height: 650px;
  $box-width: 100%;
padding: 20px 16px;
  height: $box-height;
  width: $box-width;
  border-radius: 5px;
  .bg-color-black {
    height: $box-height  35px;
    border-radius: 10px;
    //height: $box-height;
    width: $box-width;
    //border-radius: 5px;
  }
  //.bg-color-black {
  //  height: $box-height - 35px;
  //
  //  padding: 5px;
  //  //height: $box-height;
  //  width: $box-width;
  //  border-radius: 10px;
  //}

  .text {
    color: #c3cbde;

  }

  .body-box {
    border-radius: 10px;
    overflow: hidden;

    .dv-cap-chart {
      width: 100%;
      height: 600px;
    }
  }
}
</style>
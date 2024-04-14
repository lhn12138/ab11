<script>
import centerLeft1 from "@/views/centerLeft1.vue";
import centerLeft2 from "@/views/centerLeft2.vue";
import center from "@/views/center.vue";
// import bottomRight from "@/views/bottomRight.vue";
// import bottomLeft from "@/views/bottomLeft.vue";
import centerRight2 from "@/views/centerRight2.vue";
// import centerRight1 from "@/views/centerRight1.vue";
import app from "@/views/predict1.vue";
import app1 from "@/views/predict22.vue";

export default {
  data() {
    return {
      timing: null,
      loading: true,
      dateDay: null,
      dateYear: null,
      dateWeek: null,
      weekday: ['周日', '周一', '周二', '周三', '周四', '周五', '周六'],
      decorationColor: ['#568aea', '#000000']
    }
  },
  components: {
    centerLeft1,
    centerLeft2,
    // centerRight1,
    centerRight2,
    center,
    // bottomLeft,
    // bottomRight,
    app,
    app1,
  },
}
</script>
<template>
  <div class="body-box">
    <!-- 第三行数据 -->
    <div class="content-box">

      <div>
        <dv-border-box-1>
          <centerLeft2/>
        </dv-border-box-1>
      </div>
      <div>
        <dv-border-box-11>
          <app/>
        </dv-border-box-11>
      </div>
      <!-- 中间 -->
      <div>
        <center/>
      </div>
      <!-- 中间 -->
      <div>
        <dv-border-box-10>
          <centerLeft1/>
        </dv-border-box-10>
      </div>
      <!--      <div>-->
      <!--        <dv-border-box-9>-->
      <!--          <centerLeft1/>-->
      <!--&lt;!&ndash;                    <centerRight2/>&ndash;&gt;-->
      <!--        </dv-border-box-9>-->

      <!--      </div>-->
    </div>

    <!-- 第四行数据 -->
    <div class="bottom-box">
      <dv-border-box-13>
        <!--        <app/>-->
        <app1/>
<!--        <bottom-left/>-->
      </dv-border-box-13>
      <dv-border-box-9>
        <centerRight2/>
      </dv-border-box-9>
    </div>
  </div>
</template>
<style lang="scss" scoped>
@import '../assets/scss/index.scss';
</style>
<script>

import {defineComponent} from "vue";
import centerLeft1 from "@/views/centerLeft1.vue";
import centerLeft2 from "@/views/centerLeft2.vue";
import center from "@/views/center.vue";
import centerRight2 from "@/views/centerRight2.vue";
import centerRight1 from "@/views/centerRight1.vue";

export default defineComponent({
  components: {centerRight1, centerRight2, center, centerLeft2, centerLeft1}
})
</script>
<template>
<div class="body-box">
          <!-- 第三行数据 -->
          <div class="content-box">
            <div>
              <dv-border-box-6>
                <centerRight1/>

              </dv-border-box-6>
            </div>
            <div>
              <dv-border-box-12>
                <centerLeft2/>
              </dv-border-box-12>
            </div>
            <!-- 中间 -->
            <div>
              <center/>
            </div>
            <!-- 中间 -->
            <div>
              <dv-border-box-12>
                <centerLeft1/>
              </dv-border-box-12>
            </div>
            <div>

                <centerRight2/>
            </div>
            </div>
</div>
</template>
<style lang="scss" scoped>
@import '../assets/scss/index.scss';
</style>
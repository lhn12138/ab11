<script>

import {defineComponent} from "vue";
import bottomLeft from "@/views/bottomLeft.vue";
import bottomLeft1 from "@/views/bottomLeft1.vue";
import centerRight2 from "@/views/centerRight2.vue";
// import centerLeft1 from "@/views/centerLeft1.vue";
// import centerLeft2 from "@/views/centerLeft2.vue";
// import center from "@/views/center.vue";
// import centerRight2 from "@/views/centerRight2.vue";
// import centerRight1 from "@/views/centerRight1.vue";
// import app from "@/views/predict1.vue";
import bottomRight from "@/views/bottomRight.vue";
import bottomRight1 from "@/views/bottomRight1.vue";

export default defineComponent({
  components: {centerRight2, bottomLeft, bottomLeft1, bottomRight, bottomRight1}
  // components: {centerRight1, centerRight2, center, centerLeft2, centerLeft1}
  // components: { app }
})
</script>
<template>
  <div class="body-box">
    <div class="bottom-box">
      <dv-border-box-13>

        <bottom-left/>
      </dv-border-box-13>
      <dv-border-box-9>
        <bottom-left1/>
      </dv-border-box-9>

    </div>
    <div class="bottom-box">
      <dv-border-box-1>

        <bottomRight/>
      </dv-border-box-1>
      <dv-border-box-4>
        <bottomRight1/>
      </dv-border-box-4>

    </div>
  </div>
</template>
<style lang="scss" scoped>
@import '../assets/scss/index.scss';
</style>
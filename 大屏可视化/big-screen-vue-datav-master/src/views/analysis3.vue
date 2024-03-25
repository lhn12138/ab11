<script>

import {defineComponent} from "vue";
// import centerLeft1 from "@/views/centerLeft1.vue";
// import centerLeft2 from "@/views/centerLeft2.vue";
// import center from "@/views/center.vue";
// import centerRight2 from "@/views/centerRight2.vue";
// import centerRight1 from "@/views/centerRight1.vue";
// import bottomRight from "@/views/bottomRight.vue";
// import bottomLeft from "@/views/bottomLeft.vue";
import App from "@/views/App.vue";

export default defineComponent({
  // components: {bottomLeft, bottomRight, centerRight1, centerRight2, center, centerLeft2, centerLeft1}
  components:{App}
})
</script>
<template>

<div>
  <app />
</div>


</template>
<!--<style lang="scss" scoped>-->
<!--@import '../assets/scss/index.scss';-->
<!--</style>-->
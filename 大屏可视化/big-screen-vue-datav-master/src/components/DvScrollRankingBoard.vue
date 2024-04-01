<template>
  <div class="dv-scroll-ranking-board">
    <div class="ranking-list" :style="{ transform: `translateY(-${currentIndex * rowHeight}px)` }">
      <div class="ranking-item" v-for="(item, index) in displayedData" :key="index">
        <span class="rank">{{ item.rank }}</span>
        <span class="content">{{ item.content }}</span>
        <span class="score">{{ item.score }}</span>
      </div>
      <div class="ranking-item" v-for="(item, index) in displayedData.slice(0, rowNum)" :key="`repeat-${index}`">
        <span class="rank">{{ item.rank }}</span>
        <span class="content">{{ item.content }}</span>
        <span class="score">{{ item.score }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DvScrollRankingBoard',
  props: {
    config: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      timer: null,
      currentIndex: 0
    }
  },
  computed: {
    data() {
      return this.config.data
    },
    rowNum() {
      return this.config.rowNum || 12
    },
    waitTime() {
      return this.config.waitTime || 1000
    },
    rowHeight() {
      return 40 // 每行的高度
    },
    totalHeight() {
      return this.data.length * this.rowHeight
    },
    displayedData() {
      return [...this.data, ...this.data.slice(0, this.rowNum)]
    }
  },
  mounted() {
    this.startScroll()
  },
  beforeDestroy() {
    this.stopScroll()
  },
  methods: {
    startScroll() {
      this.timer = setInterval(() => {
        this.currentIndex++
        if (this.currentIndex >= this.displayedData.length) {
          this.currentIndex = 0
        }
        this.$refs.rankingList.style.transform = `translateY(-${this.currentIndex * this.rowHeight}px)`
      }, this.waitTime)
    },
    stopScroll() {
      clearInterval(this.timer)
    }
  }
}
</script>

<style scoped>
.dv-scroll-ranking-board {
  width: 100%;
  height: 100%;
  overflow: hidden;
  position: relative;
}

.ranking-list {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  transition: transform 0.5s ease-in-out;
}

.ranking-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 18px;
  padding: 10px 0;
}

.ranking-item .rank {
  width: 50px;
  text-align: right;
  margin-right: 10px;
}

.ranking-item .content {
  flex: 1;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.ranking-item .score {
  width: 100px;
  text-align: right;
}
</style>
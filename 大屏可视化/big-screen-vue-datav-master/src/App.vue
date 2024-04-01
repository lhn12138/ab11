<template>
  <div id="app">
    <nav>
      <router-link to="/">主页</router-link>
      <button v-if="isLoggedIn" @click="handleLogout">登出</button>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  computed: {
    isLoggedIn() {
      return this.$store.state.isLoggedIn;
    }
  },
  methods: {
    handleLogout() {
      // 清除 localStorage 中的 token
      localStorage.removeItem('token');
      // 将 store 中的 isLoggedIn 设为 false
      this.$store.commit('setIsLoggedIn', false);
      // 跳转到登录页面
      this.$router.push('/login');
    }
  }
};
</script>

<style lang="scss" scoped>
#app {
  width: 100vw;
  height: 100vh;
  background-color: #020308;
  overflow: hidden;
}
</style>

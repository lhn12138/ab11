<template>
  <div class="home">
    <div class="logout-container">
      <span class="logout" @click="logout">退出</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  methods: {
    logout() {
      localStorage.removeItem('isAuthenticated')
      this.$router.push('/login'); // 跳转回登录页面
    }
  }
}
</script>

<style scoped>
.logout-container {
  position: absolute;
  top: 20px;
  right: 20px;
  display: flex;
  align-items: center;
  z-index: 999;
  padding: 10px;
  border-radius: 4px;
  background-color: rgba(0, 0, 0, 0.5);
}

.logout {
  color: #ff4d4f;
  font-size: 23px;
  font-weight: bold;
  cursor: pointer;
}
</style>
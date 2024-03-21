<template>
  <div class="login-container">
    <div class="message-container" v-if="showMessage">
      <div :class="['message', messageType]">
        {{ message }}
      </div>
    </div>
    <h2>登录</h2>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username">用户名:</label>
        <input type="text" id="username" v-model="username" required>
      </div>
      <div class="form-group">
        <label for="password">密码:</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button type="submit">登录</button>
    </form>
    <p>还没有账号?
      <router-link to="/register">注册</router-link>
    </p>
  </div>
</template>

<script>
import {login} from '@/api/user'
import router from "@/router";

export default {
  data() {
    return {
      username: '',
      password: '',
      showMessage: false,
      message: '',
      messageType: ''
    }
  },
  methods: {
    login() {
      login(this.username, this.password).then(resp => {
        if (resp.status === 200) {
          this.showMessage = true;
          this.message = '登录成功';
          this.messageType = 'success';
          setTimeout(() => {
            router.push('/analysis1');
          }, 1000);
        } else {
          this.showMessage = true;
          this.message = resp.data.message;
          this.messageType = 'error';
        }
      }).catch(err => {
        console.log(err)
        this.showMessage = true;
        this.message = '登录失败,用户名或密码错误,请重试';
        this.messageType = 'error';
      });
    }
  }
}
</script>

<style scoped>
body {
  background-image: url("../assets/abc.png"); /* 替换为你的背景图路径 */
  background-size: cover;
  background-position: center;
  background-attachment: fixed; /* 固定背景图 */
}
.login-container {
  width: 300px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-image: url("../assets/abc.png");
}
.form-group {
  margin-bottom: 15px;
  background-color: rgba(255, 255, 255, 0.8); /* 调整透明度或者使用其他颜色 */
  padding: 15px;
  border-radius: 5px;
}


label {
  display: block;
  margin-bottom: 5px;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

button[type="submit"] {
  padding: 8px 15px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

.message-container {
  position: fixed;
  top: 50px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 9999;
}

.message {
  padding: 10px;
  border-radius: 5px;
  color: #fff;
  font-weight: bold;
  margin-bottom: 10px;
}

.success {
  background-color: #28a745;
}

.error {
  background-color: #dc3545;
}
</style>
<template>
  <div class="login-container" :style="loginContainerStyles">
    <div class="message-container" v-if="showMessage">
      <div :class="['message', messageType]">
        {{ message }}
      </div>
    </div>
    <h2>登录</h2>
    <form @submit.prevent="login">
      <div class="form-group" :style="formGroupStyles">
        <label for="username" :style="labelStyles">用户名:</label>
        <input type="text" id="username" v-model="username" required :style="inputStyles">
      </div>
      <div class="form-group" :style="formGroupStyles">
        <label for="password" :style="labelStyles">密码:</label>
        <input type="password" id="password" v-model="password" required :style="inputStyles">
      </div>
      <button type="submit" :style="buttonStyles">登录</button>
    </form>
    <p>
      <router-link to="/register" :style="linkStyles">注册</router-link>
    </p>
  </div>
</template>

<script>
import { login } from '@/api/user'
import router from "@/router";

export default {
  data() {
    return {
      username: '',
      password: '',
      showMessage: false,
      message: '',
      messageType: '',
      loginContainerStyles: null,
      formGroupStyles: null,
      labelStyles: null,
      inputStyles: null,
      buttonStyles: null,
      linkStyles: null
    }
  },
  methods: {
    login() {
      login(this.username, this.password).then(resp => {
        if (resp.status === 200) {
          this.showMessage = true;
          this.message = '登录成功';
          this.messageType = 'success';
          localStorage.setItem('isAuthenticated', true)
          this.saveLoginStyles(); // 保存样式
          setTimeout(() => {
            // 登录成功的逻辑

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
    },
    saveLoginStyles() {
      // 保存登录页面的样式状态
      localStorage.setItem('loginContainerStyles', JSON.stringify(getComputedStyle(this.$el)));
      localStorage.setItem('formGroupStyles', JSON.stringify(getComputedStyle(this.$el.querySelector('.form-group'))));
      localStorage.setItem('labelStyles', JSON.stringify(getComputedStyle(this.$el.querySelector('label'))));
      localStorage.setItem('inputStyles', JSON.stringify(getComputedStyle(this.$el.querySelector('input'))));
      localStorage.setItem('buttonStyles', JSON.stringify(getComputedStyle(this.$el.querySelector('button'))));
      localStorage.setItem('linkStyles', JSON.stringify(getComputedStyle(this.$el.querySelector('a'))));
    },
    restoreLoginStyles() {
      // 在返回登录页面时恢复样式
      this.loginContainerStyles = JSON.parse(localStorage.getItem('loginContainerStyles'));
      this.formGroupStyles = JSON.parse(localStorage.getItem('formGroupStyles'));
      this.labelStyles = JSON.parse(localStorage.getItem('labelStyles'));
      this.inputStyles = JSON.parse(localStorage.getItem('inputStyles'));
      this.buttonStyles = JSON.parse(localStorage.getItem('buttonStyles'));
      this.linkStyles = JSON.parse(localStorage.getItem('linkStyles'));
    }
  },
  mounted() {
    this.restoreLoginStyles();
  },
  beforeRouteEnter(to, from, next) {
    next(vm => {
      // 在进入登录页面时恢复样式
      vm.restoreLoginStyles();
    });
  }
}
</script>

<style scoped>

body {
  background-image: url("../assets/11.jpeg");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  margin: 0;
  padding: 0;
  font-family: 'Montserrat', sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: rgba(240, 240, 240, 0.8);
}

.login-container {
  width: 400px;
  padding: 40px;
  border-radius: 10px;
  background-color: #fff;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.login-container h2 {
  text-align: center;
  color: #333;
  margin-bottom: 30px;
}

.form-group {
  width: 100%;
  margin-bottom: 20px;
  padding: 15px;
  border-radius: 5px;
  background-color: rgba(245, 245, 245, 0.8);
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: 600;
  color: #333;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: rgba(255, 255, 255, 0.8);
  font-size: 16px;
  color: #333;
  transition: box-shadow 0.3s ease;
}

input[type="text"]:focus,
input[type="password"]:focus {
  outline: none;
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}

button[type="submit"] {
  width: 100%;
  padding: 12px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 600;
  transition: background-color 0.3s ease;
}

button[type="submit"]:hover {
  background-color: #0056b3;
}

.message-container {
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 9999;
}

.message {
  padding: 15px 20px;
  border-radius: 5px;
  color: #fff;
  font-weight: 600;
  margin-bottom: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.success {
  background-color: #28a745;
}

.error {
  background-color: #dc3545;
}

.login-footer {
  text-align: center;
  margin-top: 20px;
  color: #666;
}

.login-footer a {
  color: #007bff;
  text-decoration: none;
  transition: color 0.3s ease;
}

.login-footer a:hover {
  color: #0056b3;
}
</style>
<template>
  <div class="register-container">
    <h2>注册</h2>
    <form :model="form" @submit.prevent="register">
      <div class="form-group">
        <label for="username">用户名:</label>
        <input type="text" id="username" v-model="form.username" required>
        <div v-if="!usernameValid" class="error">{{ usernameError }}</div>
      </div>
      <div class="form-group">
        <label for="password">密码:</label>
        <input type="password" id="password" v-model="form.password" required>
        <div v-if="!passwordValid" class="error">{{ passwordError }}</div>
      </div>
      <div class="form-group">
        <label for="confirmPassword">确认密码:</label>
        <input type="password" id="confirmPassword" v-model="form.confirmPassword" required>
        <div v-if="!confirmPasswordValid" class="error">{{ confirmPasswordError }}</div>
      </div>
      <button type="submit">注册</button>
    </form>
    <p>已有账号?
      <router-link to="/login">登录</router-link>
    </p>
  </div>
</template>

<script>
// import {postRequest} from "@/utils/request";
import {register} from "@/api/user";
import router from "@/router";

export default {
  data() {
    return {
      form: {
        username: '',
        password: '',
        confirmPassword: ''
      },
      usernameValid: true,
      usernameError: '',
      passwordValid: true,
      passwordError: '',
      confirmPasswordValid: true,
      confirmPasswordError: ''
    }
  },
  methods: {
    register() {
      // 1. 验证用户名
      this.usernameValid = this.form.username.trim().length > 0;
      this.usernameError = this.usernameValid ? '' : '用户名不能为空';

      // 2. 验证密码
      this.passwordValid = this.form.password.length >= 6;
      this.passwordError = this.passwordValid ? '' : '密码长度至少6位';

      // 3. 验证确认密码
      this.confirmPasswordValid = this.form.password === this.form.confirmPassword;
      this.confirmPasswordError = this.confirmPasswordValid ? '' : '两次输入的密码不一致';

      // 4. 如果所有验证都通过,发送注册请求
      if (this.usernameValid && this.passwordValid && this.confirmPasswordValid) {
        register(this.form.username,this.form.password).then(resp =>{
          console.log(resp.status);
          if (resp.status === 200){
            router.push("/login")
          }else {
            alert("注册失败， 请重试")
          }
        }).catch(err =>{
          console.log(err);
        })
        // postRequest('/user/register', this.form)
        //   .then(response => {
        //     console.log('注册成功:', response);
        //     // 可以在这里添加注册成功后的逻辑,如跳转到登录页面
        //   })
        //   .catch(error => {
        //     console.error('注册失败:', error);
        //     // 可以在这里添加注册失败后的逻辑,如显示错误信息
        //   });
      }
    }
  }
}
</script>

<style scoped>
/* 样式省略 */
.error {
  color: red;
}
</style>
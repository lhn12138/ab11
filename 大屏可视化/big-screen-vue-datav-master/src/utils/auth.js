// src/utils/auth.js
export function isLoggedIn() {
  // 根据你的实际登录逻辑来检查用户是否已经登录
  // 例如,检查 localStorage 或 Vuex 中是否有登录状态
  return localStorage.getItem('token') !== null;
}
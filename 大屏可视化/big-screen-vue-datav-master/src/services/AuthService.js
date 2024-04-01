import axios from 'axios';

export async function login(username, password) {
  try {
    const response = await axios.post('/api/login', { username, password });
    // 登录成功后保存 token
    localStorage.setItem('token', response.data.token);
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
}
import axios from 'axios'

export function postRequest(url, data) {
  return axios({
    method: 'post', // 修改为正确的请求方法
    url: url,
    data: data,
    headers: {
      'Content-Type': 'application/json' // 添加请求头
    }
  })
  .then(response => {
    // 处理成功响应
    console.log('注册成功:', response.data)
    return response.data
  })
  .catch(error => {
    // 处理错误响应
    console.error('注册失败:', error)
    throw error
  })
}
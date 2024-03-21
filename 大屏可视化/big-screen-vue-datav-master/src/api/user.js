// import request from '@/utils/request'
import axios from "axios";

export function login(username, password) {
  return axios({
    url: '/user/login',
    method: 'post',
    data: { username, password }
  })
}

export function register(username, password) {
  return axios({
    url: '/user/register',
    method: 'post',
    data: { username, password }
  })
}
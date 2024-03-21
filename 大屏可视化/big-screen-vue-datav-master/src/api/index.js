import axios from 'axios'

const service = axios.create({
    baseURL:'http://localhost:8000',
    timeout:40000

})


export default service



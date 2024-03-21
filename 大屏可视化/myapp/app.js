const express = require('express')
const bodyParser = require('body-parser')
const userRouter = require('./routes/user')

const app = express()

app.use(bodyParser.json())
app.use('/user', userRouter)

const port = process.env.PORT || 3000
app.listen(port, () => {
  console.log(`Server is running on port ${port}`)
})
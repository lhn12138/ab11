const path = require('path')
const resolve = dir => {
    return path.join(__dirname, dir)
}

module.exports = {
    configureWebpack: {
        module: {
            rules: [
                {
                    test: /\.js$/,
                    loader: 'babel-loader',
                    include: [
                        /node_modules\/chart\.js/
                    ]
                }
            ]
        }
    },
    transpileDependencies: [
        'portal-vue',
        'chart.js'
    ],
    publicPath: './',
    chainWebpack: config => {
        config.resolve.alias
            .set('_c', resolve('src/components')) // key,value自行定义，比如.set('@@', resolve('src/components'))
    },
    devServer: {
        open: false,
        overlay: {
            warning: false,
            error: true
        },
        proxy: 'http://127.0.0.1:8000'
    }
}
//vue.config.js


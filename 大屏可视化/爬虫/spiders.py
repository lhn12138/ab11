import random
import requests
from lxml import etree
import csv
import os
import time
import pandas as pd
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '大屏可视化.settings')
django.setup()
from myapp.models import CarInfo


# 23年12月详细车型数据

class spiders(object):
    def __init__(self):
        self.spiderUrl = ('https://www.dongchedi.com/motor/pc/car/rank_data?aid=1839&app_name=auto_web_pc&city_name'
                          '=%E5%B9%BF%E5%B7%9E&count=10&month=&new_energy_type=&rank_data_type=11&brand_id'
                          '=&price=&manufacturer=&outter_detail_type=&nation=0')
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
        }

    def init(self):
        if not os.path.exists('./temp.csv'):
            with open('./temp.csv', 'a', newline='', encoding='utf-8') as wf:
                writer = csv.writer(wf)
                writer.writerow(["brand", "carName", "carImg", "saleVolume", "min_price", "max_price", "manufacturer",
                                 "rank", "carModel", "energyType", "marketTime", "over_score", "appearance_score"
                                    , "interior_score", "configure_score", "spatial_score", "comfort_score",
                                 "manipulating_score", "motivation_score", "comprehensive_evaluation"])

    def get_page(self):
        with open('./spiderPage.txt', 'r') as r_f:
            return r_f.readlines()[-1].strip()

    def set_page(self, newPage):
        with open('./spiderPage.txt', 'a') as a_f:
            a_f.write('\n' + str(newPage))

    def main(self):
        count = self.get_page()
        params = {
            'offset': int(count)
        }
        print("数据从{}开始爬取".format(int(count) + 1))
        time.sleep(random.randint(1, 3))
        pageJson = requests.get(self.spiderUrl, headers=self.headers, params=params).json()
        pageJson = pageJson['data']['list']
        try:

            for index, car in enumerate(pageJson):
                carData = []
                print("正在爬取第%d" % (index + 1) + "数据")
                # print(car["brand_name"])
                # 品牌名
                carData.append(car["brand_name"])
                # 车名
                carData.append(car["series_name"])
                # 图片链接
                carData.append(car["image"])
                # 销量
                carData.append(car["count"])
                # 价格
                carData.append(car["min_price"])
                carData.append(car["max_price"])
                # 厂商
                carData.append(car["sub_brand_name"])
                # 排名
                carData.append(car["rank"])

                carNumber = car["series_id"]
                # 获取详细参数页面
                infoHTML1 = requests.get("https://www.dongchedi.com/auto/params-carIds-x-%s" % carNumber,
                                         headers=self.headers)
                infoHTML1path = etree.HTML(infoHTML1.text)
                # 车型
                carModel = infoHTML1path.xpath("//div[@data-row-anchor='jb']/div[2]/div/text()")[0]
                carData.append(carModel)
                # 能源类型
                energyType = infoHTML1path.xpath("//div[@data-row-anchor='fuel_form']/div[2]/div/text()")[0]
                carData.append(energyType)
                # 上市时间
                marketTime = infoHTML1path.xpath("//div[@data-row-anchor='market_time']/div[2]/div/text()")[0]
                carData.append(marketTime)

                # 获取评分页面
                infoHTML2 = requests.get("https://www.dongchedi.com/auto/series/score/%s" % carNumber,
                                         headers=self.headers)
                infoHTML2path = etree.HTML(infoHTML2.text)
                # 综合评分
                over_score = \
                    infoHTML2path.xpath("//div[@class='jsx-2173306956 style_scoreContentRight__3F_2e tw-flex-1 "
                                        "tw-flex tw-items-center tw-justify-between']/ul[1]/li[2]/text()")[0]
                carData.append(over_score)
                # 外观评分
                appearance_score = infoHTML2path.xpath("//div[@class='jsx-2173306956 style_scoreContentRight__3F_2e "
                                                       "tw-flex-1 tw-flex tw-items-center tw-justify-between']/ul[2]/li["
                                                       "2]/text()")[0]
                carData.append(appearance_score)

                # 内饰评分
                interior_score = infoHTML2path.xpath(
                    "//div[@class='jsx-2173306956 style_scoreContentRight__3F_2e tw-flex-1 tw-flex tw-items-center "
                    "tw-justify-between']/ul[3]/li[2]/text()")[
                    0]
                carData.append(interior_score)
                # 配置评分
                configure_score = infoHTML2path.xpath(
                    "//div[@class='jsx-2173306956 style_scoreContentRight__3F_2e tw-flex-1 tw-flex tw-items-center "
                    "tw-justify-between']/ul[4]/li[2]/text()")[
                    0]
                carData.append(configure_score)
                # 空间评分
                spatial_score = infoHTML2path.xpath(
                    "//div[@class='jsx-2173306956 style_scoreContentRight__3F_2e tw-flex-1 tw-flex tw-items-center "
                    "tw-justify-between']/ul[5]/li[2]/text()")[
                    0]
                carData.append(spatial_score)
                # 舒适性评分
                comfort_score = infoHTML2path.xpath(
                    "//div[@class='jsx-2173306956 style_scoreContentRight__3F_2e tw-flex-1 tw-flex tw-items-center "
                    "tw-justify-between']/ul[6]/li[2]/text()")[
                    0]
                carData.append(comfort_score)
                # 操控评分
                manipulating_score = infoHTML2path.xpath(
                    "//div[@class='jsx-2173306956 style_scoreContentRight__3F_2e tw-flex-1 tw-flex tw-items-center "
                    "tw-justify-between']/ul[7]/li[2]/text()")[
                    0]
                carData.append(manipulating_score)
                # 动力评分
                motivation_score = infoHTML2path.xpath(
                    "//div[@class='jsx-2173306956 style_scoreContentRight__3F_2e tw-flex-1 tw-flex tw-items-center "
                    "tw-justify-between']/ul[8]/li[2]/text()")[
                    0]
                carData.append(motivation_score)

                # 综合评价
                comprehensive_evaluation = infoHTML2path.xpath(
                    "//div[@class='content-right']//a/@title")
                carData.append(comprehensive_evaluation)

                print(carData)
                self.save_to_csv(carData)
        except:
            pass

        self.set_page(int(count) + 10)
        self.main()

    def save_to_csv(self, resultData):
        with open('./temp.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(resultData)

    def clear_csv(self):
        df = pd.read_csv('./temp.csv')
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        print("总数量为%d" % df.shape[0])
        return df.values

    def save_to_sql(self):
        data = self.clear_csv()
        for car in data:
            CarInfo.objects.create(
                brand=car[0],
                carName=car[1],
                carImg=car[2],
                saleVolume=car[3],
                min_price=car[4],
                max_price=car[5],
                manufacturer=car[6],
                rank=car[7],
                carModel=car[8],
                energyType=car[9],
                marketTime=car[10],
                over_score=car[11],
                appearance_score=car[12],
                interior_score=car[13],
                configure_score=car[14],
                spatial_score=car[15],
                comfort_score=car[16],
                manipulating_score=car[17],
                motivation_score=car[18],
                comprehensive_evaluation=car[19]
            )


if __name__ == '__main__':
    spiderObj = spiders()
    # spiderObj.init()
    # spiderObj.main()
    spiderObj.save_to_sql()

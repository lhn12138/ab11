import requests
from lxml import etree
import csv
import os


# 全国每月汽车销量（11.07-23.12）
class spiders1(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
        }

    def init(self):
        if not os.path.exists('./temp1.csv'):
            with open('./temp1.csv', 'a', newline='', encoding='utf-8') as wf:
                writer = csv.writer(wf)
                writer.writerow(["日期", "销量", "同比"])

    def main(self):
        for i in range(0, 4):
            self.spiderUrl = ('https://xl.16888.com/month-{}.html'.format(i + 1))
            infoHTML = requests.get(url=self.spiderUrl,
                                    headers=self.headers)
            infoHTMLpath = etree.HTML(infoHTML.text)
            # 日期
            td_elements = infoHTMLpath.xpath('//td[@class="xl-td-t4"][1]')
            # 销量
            td_elements1 = infoHTMLpath.xpath('//td[@class="xl-td-t4"][2]')
            # 同比
            td_elements2 = infoHTMLpath.xpath('//td[@class="xl-td-t4"][3]')

            for td1, td2, td3 in zip(td_elements, td_elements1, td_elements2):
                car = []
                # 日期
                text_content = td1.text.strip()
                car.append(text_content)
                # 销量
                text_content1 = td2.text.strip()
                car.append(text_content1)
                # 同比
                text_content2 = td3.text.strip()
                car.append(text_content2)

                print(car)
                self.save_to_csv(car)

    def save_to_csv(self, resultData):
        with open('./temp1.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(resultData)


if __name__ == '__main__':
    spiderObj = spiders1()
    spiderObj.init()
    spiderObj.main()

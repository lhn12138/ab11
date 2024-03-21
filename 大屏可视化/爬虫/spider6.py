import os
import requests
from lxml import etree
import csv



# 全国每月汽车销量（11.07-23.12）
class spider6(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
        }

    def save_to_csv(self, car_name, resultData):
        filename = f"{car_name}.csv"

        # 添加表头只应在首次写入时执行，因此检查文件是否存在并追加模式下写入表头
        if not os.path.exists(filename):
            with open(filename, 'w', newline='',encoding='utf-8') as wf:
                writer = csv.writer(wf)
                writer.writerow(["时间", "月销量(辆)","当月销量排名","占厂商份额", "在厂商排名", "在SUV排名"])
        else:
            # 如果文件已存在，则直接追加数据
            pass

        # 写入数据（无论是否为第一次写入）
        with open(filename, 'a', newline='') as wf:
            writer = csv.writer(wf)
            writer.writerow(resultData)

    def main(self):
        for i in range(1, 13):
            self.spiderUrl = ('https://xl.16888.com/style-{}.html'.format(i))
            infoHTML = requests.get(url=self.spiderUrl,
                                    headers=self.headers)
            infoHTMLpath = etree.HTML(infoHTML.text)

            # 车型与厂商信息
            td_elements = infoHTMLpath.xpath('//td[@class="xl-td-t2"]//a[contains(@href, "s")]')
            td_elements1 = infoHTMLpath.xpath('//td[@class="xl-td-t2"]//a[contains(@href, "f")]')

            for td1, td2 in zip(td_elements, td_elements1):
                car_name = td2.text.strip() + '-' + td1.text.strip()

                print(car_name)

                for j in range(1, 6):
                    text2 = td1.attrib['href'].rstrip('/')
                    infoHTML2 = requests.get("https://xl.16888.com{}-{}.html".format(text2, j),
                                             headers=self.headers)
                    infoHTML2path = etree.HTML(infoHTML2.text)

                    ttd_elements = infoHTML2path.xpath('//td[@class="xl-td-t4"][1]')
                    ttd_elements1 = infoHTML2path.xpath('//td[@class="xl-td-t4"][2]')
                    ttd_elements2 = infoHTML2path.xpath('//td[@class="xl-td-t5"]//a[contains(@href, "style")]')
                    ttd_elements3 = infoHTML2path.xpath('//td[@class="xl-td-t4"][3]')
                    ttd_elements4 = infoHTML2path.xpath('//td[@class="xl-td-t5"]//a[contains(@href, "history")]')
                    ttd_elements5 = infoHTML2path.xpath('//td[@class="xl-td-t5"]//a[contains(@href, "level")]')

                    car_data = []
                    try:
                        for ttd1, ttd2, ttd3, ttd4, ttd5, ttd6 in zip(ttd_elements, ttd_elements1, ttd_elements2,
                                                                      ttd_elements3, ttd_elements4, ttd_elements5):
                            ttext1 = ttd1.text.strip()

                            ttext2 = ttd2.text.strip()

                            ttext3 = ttd3.text.strip()

                            ttext4 = ttd4.text.strip()

                            ttext5 = ttd5.text.strip()

                            ttext6 = ttd6.text.strip()

                            car_data = [ttext1, ttext2, ttext3, ttext4, ttext5, ttext6]

                            self.save_to_csv(car_name, car_data)
                    except:
                        pass



if __name__ == '__main__':
    spiderObj = spider6()
    spiderObj.main()
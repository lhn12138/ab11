import requests
from lxml import etree
import csv
import os

#每年汽车厂商排名（15-23）
class Spider4:
    def __init__(self, start_year=2015, end_year=2023):
        self.start_year = start_year
        self.end_year = end_year
        self.base_url_template = "https://xl.16888.com/factory-{year}01-{year}12-{page_num}.html"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
        }
        self.init()

    def init(self):
        if not os.path.exists('./temp4.csv'):
            with open('./temp4.csv', 'w', newline='', encoding='utf-8') as wf:
                writer = csv.writer(wf)
                writer.writerow(["年份","排名", "品牌LOGO",  "厂商", "销量", "占销量份额"])

    def crawl_pages_for_years(self):
        for year in range(self.start_year, self.end_year + 1):
            for page_num in range(1, 5):
                url = self.base_url_template.format(year=year, page_num=str(page_num))
                response = requests.get(url, headers=self.headers)

                if response.ok:
                    infoHTMLpath = etree.HTML(response.text)
                    self.parse_response(infoHTMLpath, year)
                else:
                    print(f"无法获取{year}年的第{page_num}页数据，跳过该页面...")

    def parse_response(self, infoHTMLpath, year):
        try:
            # 排名
            td_elements = infoHTMLpath.xpath('//td[@class="xl-td-t1"][1]')
            # 占销量份额
            td_elements2 = infoHTMLpath.xpath('//td[@class="xl-td-t3"][2]')
            # 销量
            td_elements3 = infoHTMLpath.xpath('//td[@class="xl-td-t3"][1]')
            # 厂商
            td_elements4 = infoHTMLpath.xpath('//td[@class="xl-td-t2"]/a')
            # Logo
            img_elements = infoHTMLpath.xpath('//td//a/img[contains(@src, "flogo")]')

            for td1, td2, td3, td4, td5,in zip(td_elements,td_elements4, td_elements3, td_elements2,img_elements):
                # 年份
                car = [year]
                # 排名
                text_content = td1.text.strip()
                car.append(text_content)
                # Logo
                img =td5.get('src')
                car.append(img)
                # 厂商
                text_content1 = td2.text.strip()
                car.append(text_content1)
                # 销量
                text_content4 = td3.text
                car.append(text_content4)
                # 占销量份额
                text_content3 = td4.text.strip()
                car.append(text_content3)

                print(car)
                self.save_to_csv(car)
        except:
            pass

    def save_to_csv(self, resultData):
        with open('./temp4.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(resultData)


if __name__ == '__main__':
    spiderObj = Spider4()
    spiderObj.crawl_pages_for_years()

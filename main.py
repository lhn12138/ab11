import re
import requests
from bs4 import BeautifulSoup
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}
url = 'https://xl.16888.com/ev.html'
start_html = requests.get(url, headers=headers)
start_html.encoding = 'utf-8'  # 防止中文乱码
print("第1页响应状态码：", start_html.status_code)
soup = BeautifulSoup(start_html.text, 'lxml')
product = soup.find_all('tr')[1:51]  # soup中find_all方法寻找源代码中的“tr”，目标网页有两个表格，只需定位到第二个表格即可，故选取第6-26
# print(product)
product_list = []
for row in product:  # 在每个“tr”中循环找寻“td”
    res = r'<a .*?>(.*?)</a>'
    top = row.find_all('td')[0].text
    style = str(row.find_all('td')[1].contents)
    aa = re.findall(res, style, re.S | re.M)
    for a in aa:
        style = a
    num = row.find_all('td')[2].text
    rate = str(row.find_all('td')[3].contents)
    bb = re.findall(res, rate, re.S | re.M)
    for b in bb:
        rate = b
    price = str(row.find_all('td')[4].contents)
    cc = re.findall(res, price, re.S | re.M)
    for c in cc:
        price=c
    product_list.append({'排名': top, '车型': style, '销量': num, '厂商': rate, '价格': price})
print(product_list)
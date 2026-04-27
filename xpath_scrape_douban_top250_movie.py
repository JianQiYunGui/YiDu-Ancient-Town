from lxml import etree
import requests
import time
url = "https://movie.douban.com/top250"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"}
try:
    for start_num in range(0, 250,25):
        response = requests.get(f"{url}?start={start_num}", headers = headers)
        response.raise_for_status()
        html = response.text
        tree = etree.HTML(html)
        item_list = tree.xpath("//div[@class='item']")
        for item in item_list:
            title_elements = item.xpath(".//div[@class='hd']/a/span[1]/text()")
            title = title_elements[0] if title_elements else None
            rating_nums = item.xpath(".//span[@class='rating_num']/text()")
            rating_num = rating_nums[0] if rating_nums else None
            print(f"电影名：{title},评分：{rating_num}")
        time.sleep(2)
except requests.RequestException as e:
    print(f"请求失败：{e}")
except Exception as e:
    print(f"发生错误：{e}")

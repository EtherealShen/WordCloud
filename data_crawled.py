"""
@Description: 
@Author: Shen Du
@Date: 2024-04-18 12:34:15
@LastEditTime: 2024-04-21 23:14:16
@LastEditors: Ambrose
"""

import os
import re
import requests
from lxml import etree
from setting import setting as st


class data_crawled(object):
    def __init__(self) -> None:
        self.url = st.file_info
        self.etree = etree
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Referer": "http://www.baidu.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",
        }
        self.response = ""
        self.content = ""

    # 爬取文本
    def data_scraping(self, url):
        self.response = ""
        self.content = ""
        response = requests.get(url, headers=self.headers)
        response.encoding = "utf-8"
        self.response = response.text

    # 提取文本
    def data_extract(self):
        result = self.etree.HTML(self.response)
        title = result.xpath("//head/title/text()")[0]
        content = result.xpath("//div[@class='pages_content']//text()")
        content = " ".join(content)
        content = re.sub(r"\n\s*\n", "\n", content)
        self.content += title + "\n"
        self.content += content.strip()

    # 文本存储
    def data_storage(self, year):
        if os.path.exists("./resource/{}".format(year)):
            os.remove("./resource/{}".format(year))
        with open("./resource/{}".format(year), "w", encoding="utf-8") as f:
            f.write(self.content)
        f.close()

    # 爬虫入口
    def run(self):
        for year, url in self.url.items():
            self.data_scraping(url)
            self.data_extract()
            self.data_storage(year)


if __name__ == "__main__":
    crawled = data_crawled()
    crawled.run()

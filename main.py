#encoding=gbk
import requests
from bs4 import BeautifulSoup

#blog.sufunspace.org

while True:
    # 定义要爬取的URL
    url = input("你想爬取的网站：")

    original_string = url
    prefix = "http://"

    if "http://" in url or "https://" in url:
        print(f"url:{url}")
    else:
        # 使用百分号格式化
        url = "%s%s" % (prefix, original_string)
        print(f"url:{url}")

    # 发送HTTP GET请求
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 打印网页标题
        title = soup.title.string
        print(f"网页标题: {title}")

        # 提取所有链接
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            text = link.string
            print(f"链接: {href} - 文本: {text}")
    else:
        print(f"请求失败，状态码: {response.status_code}")

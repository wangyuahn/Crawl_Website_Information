#encoding=gbk
import requests
from bs4 import BeautifulSoup

#blog.sufunspace.org

while True:
    # ����Ҫ��ȡ��URL
    url = input("������ȡ����վ��")

    original_string = url
    prefix = "http://"

    if "http://" in url or "https://" in url:
        print(f"url:{url}")
    else:
        # ʹ�ðٷֺŸ�ʽ��
        url = "%s%s" % (prefix, original_string)
        print(f"url:{url}")

    # ����HTTP GET����
    response = requests.get(url)

    # ��������Ƿ�ɹ�
    if response.status_code == 200:
        # ����HTML����
        soup = BeautifulSoup(response.text, 'html.parser')

        # ��ӡ��ҳ����
        title = soup.title.string
        print(f"��ҳ����: {title}")

        # ��ȡ��������
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            text = link.string
            print(f"����: {href} - �ı�: {text}")
    else:
        print(f"����ʧ�ܣ�״̬��: {response.status_code}")

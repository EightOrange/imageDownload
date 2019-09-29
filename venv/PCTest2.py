from urllib import request
from bs4 import BeautifulSoup
import re
import ssl
import os
import bs4

ssl._create_default_https_context = ssl._create_unverified_context

# 设置模拟浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
}
path = '/Users/yuzhuofan/Documents/爬虫结果1'


def getHtmlCode(url):
    url1 = request.Request(url, headers=headers)
    page = request.urlopen(url1).read().decode('GBK')
    return page


def getImg(page):
    soup = BeautifulSoup(page, 'lxml')  # 按照html格式解析页面
    img_list = soup.find_all(attrs={'class':'bshare-custom'})
    print (img_list)
    # img_list_img = img_list.find_all('img', {'class': 'data-original'})
    # x = 0
    # # count = 0
    # print (img_list_img)
    # print (type(img_list_img))
    # for img_one in img_list_img:
    #     img_url = img_one.get('data-original')
    #     print(img_url)
    #     request.urlretrieve(img_url, path + '/%s.jpg' % x)
    #     x += 1


if __name__ == '__main__':
    url = 'https://bbs.voc.com.cn/topic-8996349-1-1.html'

    page = getHtmlCode(url)
    print (page)
    getImg(page)

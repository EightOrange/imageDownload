from urllib import request
from bs4 import BeautifulSoup
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def get_page(url, tot_page):
    url_list = []
    for i in range(1, tot_page):
        new_url = re.sub(('=(.*)'), '%s%s' % ('=', i), url)
        url_list.append(new_url)
    return url_list


if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/4792769205?pn=1'
    path = '/Users/yuzhuofan/Documents/爬虫结果'
    count = 0
    url_list = get_page(url, 4)
    for url in url_list:
        print(url)
        page = request.urlopen(url).read().decode()
        soup = BeautifulSoup(page, 'lxml')
        regex = re.compile("http://imgsrc.baidu.com/forum/w%3D580/sign=.+\.jpg")
        pic_list = soup.findAll('img', {'src': regex})
        for pic in pic_list:
            pic = pic['src']
            request.urlretrieve(pic, '%s/%s.jpg' % (path, count))
            count += 1

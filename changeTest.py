#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    for i in range(0,220,20):
        url = 'https://movie.douban.com/subject/26266893/comments?start=%d'%i+'&limit=20&status=P&sort=new_score'
        page_text = requests.get(url=url,headers=headers).text
        ex = '<span class="short">(.*?)</span>'
        text_list = re.findall(ex,page_text)
        print(text_list)
        text_list = '\n'.join(text_list)
        file = open("spider1.txt", "a+",encoding='UTF-8')#保存的文件名
        file.write(text_list + "\n")
        file.close()




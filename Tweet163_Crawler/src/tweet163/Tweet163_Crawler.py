# -*- coding:utf-8 -*-
'''
#=====================================================
#     FileName: tweet163_crawler.py
#         Desc: download html pages from sina_weibo and save to local files 
#       Author: DianaCody
#      Version: 1.0
#        Since: 2014-09-27 15:20:21
#=====================================================
'''

import string
import urllib2
import re
import chardet

# sina tweet's url = 'http://s.weibo.com/wb/topic&nodup=1&page=20' 
def writeHtml(url, start_page, end_page):
    for i in range(start_page, end_page+1):
        FileName = string.zfill(i, 3)
        HtmlPath = FileName + '.html'
        print 'Downloading No.' + str(i) + ' page and save as ' + FileName + '.html...'
        f = open(HtmlPath, 'w+')
        html = urllib2.urlopen(url + str(i)).read()
        f.write(html)
        f.close()

def crawler(key, s_page, e_page):
    url = 'http://t.163.com/tag/'+ key +'&nodup=1&page='    
    print 'Now begin to download html pages...'
    writeHtml(url, s_page, e_page)

def regex():
    start_page = 1
    end_page = 9
    for i in range(start_page, end_page):
        HtmlPath = '00'+str(i)+'.html'
        page = open(HtmlPath).read()
        
        # set encode format
        charset = chardet.detect(page)
        charset = charset['encoding']
        if charset!='utf-8' and charset!='UTF-8':
            page = page.decode('gb2312', 'ignore').encode("utf-8")
        unicodePage = page.decode('utf-8')
        
        pattern = re.compile('"content":\s".*?",', re.DOTALL)
        contents = pattern.findall(unicodePage)
        for content in contents:
            print content

if __name__ == '__main__':
    print'#--------------------------------------------------------------------------'
    print'#      Software: 163 Tweet Spider      '
    print'#       Version: 1.0                    '
    print'#        Author: DianaCody              '
    print'#      Language: Python 2.7             '
    print'#          Desc: Download html pages from sina_weibo and save to local files,'
    print'#                and read each tweet of your key    '
    print'#         Since: 2014-09-27             '
    print'#--------------------------------------------------------------------------'  
    print ''
    key = str(raw_input(u'please input you search key: \n'))
    begin_page = int(raw_input(u'input begin pages:\n'))  
    end_page = int(raw_input(u'input end pages:\n'))
    crawler(key, begin_page, end_page)
    print'Crawler finished... \n'
    print'The contents are: '
    regex()
    raw_input()
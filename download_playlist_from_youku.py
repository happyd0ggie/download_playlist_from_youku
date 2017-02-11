#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Download playlist from youku with you-get.
Prerequisites:
    1. Python3.x
    2. module: bs4, lxml
    3. you-get
Usage:
    1. press F12, open developer panel, copy outerHTML containing playlist and paste into a file, e.g. urls.txt
    2. run python download_playlist_from_youku.py urls.txt
    3. download is go on...
'''

import os
import sys

from multiprocessing import Pool
from bs4 import BeautifulSoup

class Downloader(object):
    def __init__(self, elements):
        self.elements = elements
        
    def download(self, href):
        os.system('you-get "http:{0}"'.format(href))

    def go(self):
        html = ''
        with open(self.elements, 'r') as f:
            for line in f:
                html += line.strip('\n')
        
        soup = BeautifulSoup(html, 'lxml')
        urls = soup.find_all('a', class_ = 'A')

        p = Pool(len(urls))
        for url in urls:
            p.apply_async(self.download, args = (url['href'],))
        p.close()
        p.join()

def usage():
    usage_info = '''
    Usage:
        1. press F12, open developer panel, copy outerHTML containing playlist and paste into a file, e.g. urls.txt
        2. run command: python download_playlist_from_youku.py urls.txt
        3. download is go on...
    '''
    print(usage_info)

def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit()
    
    downloader = Downloader(sys.argv[1])
    downloader.go()

if __name__ == '__main__':
    main()
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

from multiprocessing import Pool
from bs4 import BeautifulSoup

class Downloader(object):
    def __init__(self, elements):
        self.elements = elements
        
    def download(self, href):
        print('you-get "http:{0}"'.format(href))
        #os.system('you-get "http:{0}"'.format(href))

    def go(self):
        html = ''
        with open(self.elements, 'r') as f:
            for line in f:
                html += line.strip('\n')
        
        soup = BeautifulSoup(html, 'lxml')
        urls = href.find_all('a', class_ = 'A')

        p = Pool(len(urls))
        for url in urls:
            p.apply_async(download, args = (url['href'],))
        p.close()
        p.join()

def main():
    downloader = Downloader('urls.txt')
    downloader.go()

if __name__ == '__main__':
    main()
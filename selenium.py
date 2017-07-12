#coding=UTF-8
#https://gist.github.com/KhepryQuixote/46cf4f3b999d7f658853
#polipo socksParentProxy=localhost:9050

from __future__ import division
import requests
import shutil
from selenium import webdriver
import time
import os
import redis
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/')
from addtoexcel import  addtoexcel,makeexcelfile
from selenium.webdriver.common import action_chains, keys


output_excel_name = "tehran_mobile.xlsx"

if not os.path.isfile(output_excel_name) :
        makeexcelfile(output_excel_name)

PROXY = "127.0.0.1:8123" 
from stem import Signal
from stem.control import Controller


from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option( "prefs",{"profile.managed_default_content_settings.images":2},{"profile.default_content_settings.cookies": 2})
chrome_options.add_argument('--proxy-server=%s' % PROXY)
browser = webdriver.Chrome('/Users/taha/Documents/playground/scrap/istgah.com/chromedriver',chrome_options=chrome_options)
browserip = webdriver.Chrome('/Users/taha/Documents/playground/scrap/istgah.com/chromedriver',chrome_options=chrome_options)

def switchIP():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)



browser.get("site")
browserip.get("http://www.icanhazip.com")
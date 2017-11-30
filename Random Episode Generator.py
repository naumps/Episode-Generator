#!/usr/bin/python3

from selenium import webdriver
import random
import subprocess
from selenium.common.exceptions import NoSuchElementException
import psutil
import time



fileToRead = open('./FINKI/episodes.txt', 'r')
list = fileToRead.read().splitlines()
a = 0
while (1):
    a = random.randint(1, 250)
    if a not in list:
        list.append(a)
        break





flag = False
while (not flag):
    try:
        browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        browser.get('https://www.yt-to-mp3.com/video-search.html')
        textbox = browser.find_element_by_id('query')
        textbox.send_keys("lud zbunjen normalan " + str(a))
        flag = True
    except NoSuchElementException:
        browser.quit()

textbox.submit()
time.sleep(2)

browser.find_element_by_link_text("Play").click()
browser.execute_script("window.scrollTo(0, 130)")

#disable autoplay
browser.find_element_by_css_selector('.btn.btn-primary.btn-sm.btn-block.autoplay.disable').click()
browser.find_element_by_css_selector('.jwfullscreen.jwbuttoncontainer').click()
#fullscreen

fileToWrite = open('./FINKI/episodes.txt', 'a')
fileToWrite.write("\n"+str(a))
fileToWrite.close()

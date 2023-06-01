# 00. 라이브러리
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import urllib
import time
import random
import sys
import re
import os
import pyautogui
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

# 01. 이미지 저장 폴더 설정
f_dir = 'C:/Users/KimBumYun/Desktop/Github/2023/CAPSTONE_DESIGN_Crawling/'

# 02. 시간 설정
now = time.localtime()
f_name = '%04d-%02d-%02d-%02d-%02d-%02d' %(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
dir_name = 'EMART24-사진저장'

# 03. 이미지 저장 폴더 설정
os.makedirs(f_dir + f_name + '-' + dir_name)
os.chdir(f_dir + f_name + '-' + dir_name)
f_result_dir = f_dir + f_name + '-' + dir_name

# 04. 상품 이름, 가격 저장 txt
f = open(f_name + '.txt', 'w')

s_time = time.time()

# 05. pyony 웹 열기
dr = webdriver.Chrome("/chromedriver.exe")
dr.set_window_size(1440, 1000)
dr.get('https://pyony.com/')
time.sleep(1)

# 06. CU 웹 이동
choose = dr.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[6]/a')
choose.send_keys('\n')
time.sleep(2)

# 07. CU 이미지 다운로드
images = dr.find_elements(By.CSS_SELECTOR, 'img.prod_img')

page_count = 1
image_count = 2
image_full_count = 1

while True:
    try:
        product_name = dr.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/div[' + str(image_count) + ']/a/div/div[2]/div[2]/strong').text
        product_price = dr.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/div[' + str(image_count) + ']/a/div/div[2]/div[2]/span[1]').text
        product_type = dr.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/div[' + str(image_count) + ']/a/div/div[2]/div[2]/span[2]').text
        f.write(str(image_full_count) + '-EMART24-' + product_type + '-' + product_name + '-' + product_price + '\n')
        imgUrl = dr.find_elements(By.CSS_SELECTOR, "img.prod_img")[image_count-2].get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(image_full_count) + ".jpg")
        image_count = image_count + 1
        image_full_count = image_full_count + 1
        if image_count == 21:
            image_count = 2
            page_count = page_count + 1
            next_url = 'https://pyony.com/brands/emart24/?page=' + str(page_count)
            dr.get(next_url)
    except HTTPError as e:
        err = e.read()
        code = e.getcode()
        if code == int(404):
            image_full_count = image_full_count + 1
            image_count = image_count + 1
        if code == int(403):
            image_full_count = image_full_count + 1
            image_count = image_count + 1
        print(code)
        continue
    except:
        break

f.close()

e_time = time.time()#끝난시간 체크

t_time = e_time - s_time #크롤링에 쓰인 시간

print('='*100)
print('총 소요시간은 %s 초입니다.'%round(t_time, 1))
print('총 저장 건수는 %s 건입니다.'%(image_full_count-1))
print('파일 저장 경로: %s 입니다.'%f_result_dir)
print('='*100)
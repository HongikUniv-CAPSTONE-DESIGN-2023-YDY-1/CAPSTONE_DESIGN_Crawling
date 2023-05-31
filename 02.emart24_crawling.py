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
#f_dir = input('이미지를 저장할 폴더(예:C:/Users/) : ')

# 02. 시간 설정
now = time.localtime()
f_name = '%04d-%02d-%02d-%02d-%02d-%02d' %(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
dir_name = 'EMART24-사진저장'

# 03. 이미지 저장 폴더 설정
os.makedirs(f_dir + f_name + '-' + dir_name)
os.chdir(f_dir + f_name + '-' + dir_name)
f_result_dir = 'EMART24-' + f_dir + f_name + '-' + dir_name

# 04. 상품 이름, 가격 저장 txt
f = open(f_name + '.txt', 'w')

s_time = time.time()

# 05. 1+1 웹 열기
dr = webdriver.Chrome("/chromedriver.exe")
dr.set_window_size(1000, 1000)
dr.get('https://www.emart24.co.kr/goods/event?search=&category_seq=1&align=')
time.sleep(1)

images = dr.find_elements(By.CSS_SELECTOR, 'img')

li_count = 1
image_count = 1
image_full_count = 1
page_count = 1

# 06. 이미지 다운로드
while True:
    try:
        if int(li_count) == 21:
            li_count = 1
            page_count = page_count + 1
            dr.get('https://www.emart24.co.kr/goods/event?search=&page=' + str(page_count) + '&category_seq=1&align=')
        product_name = dr.find_element(By.XPATH, '/html/body/div[2]/div/section[4]/div[' + str(li_count) + ']/div[3]/div/p/a').text
        product_price = dr.find_element(By.XPATH, '/html/body/div[2]/div/section[4]/div[' + str(li_count) + ']/div[3]/span/a').text
        f.write(str(image_full_count) + '-EMART24-ONE_PLUS_ONE-' + product_name + '-' + product_price + '\n')
        imgUrl = dr.find_element(By.XPATH, '/html/body/div[2]/div/section[4]/div[' + str(li_count) + ']/div[2]/img').get_attribute("src")
        #os.system("curl " + imgUrl + " > " + str(image_full_count) + ".jpg")
        urllib.request.urlretrieve(imgUrl, str(image_full_count) + ".jpg")
        li_count = li_count + 1
        image_count = image_count + 1
        image_full_count = image_full_count + 1
    except HTTPError as e:
        err = e.read()
        code = e.getcode()
        if code == int(404):
            image_full_count = image_full_count + 1
            image_count = image_count + 1
            li_count = li_count + 1
        print(code)
        continue
    except:
        break

# 07. 2+1 웹 열기
choose = dr.find_element(By.XPATH, '/html/body/div[2]/div/section[3]/ul/li[3]/a')
choose.send_keys('\n')
time.sleep(2)

images = dr.find_elements(By.CSS_SELECTOR, 'img')

li_count = 1
image_count = 1
page_count = 1

# 08. 이미지 다운로드
while True:
    try:
        if int(li_count) == 21:
            li_count = 1
            page_count = page_count + 1
            dr.get('https://www.emart24.co.kr/goods/event?search=&page=' + str(page_count) + '&category_seq=2&align=')
        product_name = dr.find_element(By.XPATH, '/html/body/div[2]/div/section[4]/div[' + str(li_count) + ']/div[3]/div/p/a').text
        product_price = dr.find_element(By.XPATH, '/html/body/div[2]/div/section[4]/div[' + str(li_count) + ']/div[3]/span/a').text
        f.write(str(image_full_count) + '-EMART24-TWO_PLUS_ONE-' + product_name + '-' + product_price + '\n')
        imgUrl = dr.find_element(By.XPATH, '/html/body/div[2]/div/section[4]/div[' + str(li_count) + ']/div[2]/img').get_attribute("src")
        #os.system("curl " + imgUrl + " > " + str(image_full_count) + ".jpg")
        urllib.request.urlretrieve(imgUrl, str(image_full_count) + ".jpg")
        li_count = li_count + 1
        image_count = image_count + 1
        image_full_count = image_full_count + 1
    except HTTPError as e:
        err = e.read()
        code = e.getcode()
        if code == int(404):
            image_full_count = image_full_count + 1
            image_count = image_count + 1
            li_count = li_count + 1
        print(code)
        continue
    except:
        break
        
# 09. 추출내용 정리
f.close()

e_time = time.time()#끝난시간 체크

t_time = e_time - s_time #크롤링에 쓰인 시간 

print('='*100)
print('총 소요시간은 %s 초입니다.'%round(t_time, 1))
print('총 저장 건수는 %s 건입니다.'%(image_full_count))
print('파일 저장 경로: %s 입니다.'%f_result_dir)
print('='*100)
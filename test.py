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

imgUrl = "https://image.woodongs.com/imgsvr/item/GD_8809125061857_001.jpg"
urllib.request.urlretrieve(imgUrl, "test.jpg")
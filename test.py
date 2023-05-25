import os
import time

# 다운받을 이미지 url
url = "https://www.emart24.co.kr/image/MzA0MDE="

# time check
start = time.time()

# curl 요청
os.system("curl " + url + " > test.jpg")

# 이미지 다운로드 시간 체크
print(time.time() - start)
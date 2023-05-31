import http.client
import mimetypes
from codecs import encode

conn = http.client.HTTPConnection("localhost", 8080) # 서버 주소로 바꾸면 됨 숫자는 포트번호
dataList = []
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=multipartFiles; filename={0}'.format('ㅇㅇㅇㅇㅇ.png'))) # ㅇㅇㅇㅇㅇ.png 대신에 파일 이름

fileType = mimetypes.guess_type('/Users/imsubin/Desktop/ㅇㅇㅇㅇㅇ.png')[0] or 'application/octet-stream' # 앞에 경로에 이미지 파일 경로
dataList.append(encode('Content-Type: {}'.format(fileType)))
dataList.append(encode(''))

with open('/Users/imsubin/Desktop/ㅇㅇㅇㅇㅇ.png', 'rb') as f:
  dataList.append(f.read())
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=multipartFiles; filename={0}'.format('그림1.png')))

fileType = mimetypes.guess_type('/Users/imsubin/Desktop/그림1.png')[0] or 'application/octet-stream'
dataList.append(encode('Content-Type: {}'.format(fileType)))
dataList.append(encode(''))

with open('/Users/imsubin/Desktop/그림1.png', 'rb') as f:
  dataList.append(f.read())
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=list;'))

dataList.append(encode('Content-Type: {}'.format('application/json')))
dataList.append(encode(''))
#아래에 json 데이터 집어넣으면 됨
dataList.append(encode("[{\"brand\": \"GS25\",\"promotion\": \"ONE_PLUS_ONE\",\"pricePerUnit\": 10,\"name\": \"aaaaa\",\"itemType\":\"konbini\"},{\"brand\": \"GS25\",\"promotion\": \"ONE_PLUS_ONE\",\"pricePerUnit\": 1000,\"name\": \"bbbbbbbb\",\"itemType\":\"konbini\"}]"))
dataList.append(encode('--'+boundary+'--'))
dataList.append(encode(''))
body = b'\r\n'.join(dataList)
payload = body
headers = {
   'Content-type': 'multipart/form-data; boundary={}'.format(boundary) 
}
conn.request("POST", "/konbini/items", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
import urllib.request
#import requests
import urllib.parse
#import certifi


#https://www.cnblogs.com/zhaof/p/6910871.html
# result = urllib.request.urlopen('http://wwww.baidu.com')
#
# print(result.read().decode())
#
# data = bytes(urllib.parse.urlencode({"hello": "world!"}), encoding="utf-8")
# result = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(result.read().decode("utf-8"))

# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as tout:
#     print("timeout!!!")
#
# response = urllib.request.urlopen("http://wwww.baidu.com")
# print(response.getheader("server"))
# print(response.getheaders())
# url = "http://httpbin.org/post"
# headers = {
# "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
# }
# # url='https://www.douban.com/'
# data = bytes(urllib.parse.urlencode({"name": "Joke"}), encoding="utf-8")
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")   # POST must be Caps
# result = urllib.request.urlopen(req)
# print(result.read().decode("utf-8"))

# SSL Error to install certificates.command
url = "https://www.douban.com"
headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}
# req = requests.Request(url=url, headers=headers)
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))

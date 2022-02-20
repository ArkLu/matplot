"""
Ark Lu
2020-06-24
Version 1.0
"""


import requests
import hashlib, time, random


def md5(word):
    word = word.encode()
    result = hashlib.md5(word)
    return result.hexdigest()


def youdao(word):

    headers = {
        'Accept': 'application / json, text / javascript, * / *; q = 0.01',
        'Accept-Encodingg': 'zip, deflate',
        'Accept - Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Length': '255',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'JSESSIONID=abcqvlXgyrNd2bHGVgClx; _ntes_nnid=51b2078cc4077e13288249f78ef60584,1592830656555; OUTFOX_SEARCH_USER_ID_NCOO=246273121.26279658; OUTFOX_SEARCH_USER_ID=1630396520@10.169.0.102; YOUDAO_MOBILE_ACCESS_TYPE=1; ___rl__test__cookies=1592830707900',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/?keyfrom=dict2.top',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'X-Requested-With': 'XMLHttpRequest'
    }
    t = md5(
        "5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
    r = str(int(time.time() * 1000))
    i = r + str(random.randint(0, 9))
    words = {
        'i': word,
        'from': "AUTO",
        'to': "AUTO",
        'smartresult': "dict",
        'client': "fanyideskweb",
        'salt': i,
        'sign': md5("fanyideskweb" + word + i + "mmbP%A-r6U3Nw(n]BjuEU"),
        'ts': r,
        'bv': t,
        'doctype': "json",
        'version': "2.1",
        'keyfrom': "fanyi.web",
        'action': "FY_BY_CLICKBUTTION"
    }

    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    result = requests.post(url, data=words, headers=headers)
    print(result)
    print(result.text)


if __name__ == '__main__':
    while 1:
        word = input("Please input your word:")
        youdao(word)

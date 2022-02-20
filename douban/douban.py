# Author: Ark Lu
# Date: 2020-06-27
# Version: 1.0
# Purpose: Self Practice for CrapyHub


import sys
from bs4 import BeautifulSoup  # 网页解析获取数据
import re  # 正则表达shi
import urllib.request  # 获取网页数据
import urllib.error  # 获取网页数据
import xlwt  # Excel操作
import sqlite3  # 数据库操作


def main():
    # """
    # 1. Get the URL source website
    # 2. Get the data from this website
    # 3. Analyze the data one by one
    # 4. Saved the data to local
    # """
    print('starting to spider douban movies information.......')
    baseurl = 'https://movie.douban.com/top250?start='
    datalist = getData(baseurl)
    # savepath = 'doubantop250.xls'
    dbpath = 'movie.db'
    # saveData(datalist, savepath)
    saveData2Db(datalist, dbpath)
    # askURL("https://movie.douban.com/top250?start=")


findlink = re.compile(r'<a href="(.*?)">')

# 影片图片的链接
findSrcImg = re.compile(r'img.*src="(.*?)"', re.S)  # re.S 表示前面忽视换行符

findTitle = re.compile(r'<span class="title">(.*)</span>')

findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')

findJudge = re.compile(r'<span>(\d*)人评价</span>')

findInq = re.compile(r'<span class="inq">(.*)</span>')

findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)
        # print(html)
        # 3. Analyze the data one by one
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)
            link = re.findall(findlink, item)[0]  # re通过正则表达式查找字符串 [0]表示第一页
            data.append(link)
            imgsrc = re.findall(findSrcImg, item)[0]
            data.append(imgsrc)
            titles = re.findall(findTitle, item)
            if len(titles) == 2:
                ctitle = titles[0]
                etitle = titles[1].replace("/", "")  # to Remove /
                data.append(ctitle)  # Add Chinese Title
                data.append(etitle)  # add foreign Title
            else:
                data.append(titles[0])
                data.append(" ")  # Must save one empty value

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgenumb = re.findall(findJudge, item)[0]
            data.append(judgenumb)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", " ")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?>(\s+)?', " ", bd)
            data.append(bd.strip())  # remove the 前后空格
            print('-' * 20 + str(i) + '-' * 10)
            # print(data)
            datalist.append(data)

    # print(soup)
    # print(datalist)
    return datalist


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # Create workbook object
    sheet = book.add_sheet('DouBan Movie Top250', cell_overwrite_ok=True)  # Create work sheet
    col = ("Hyperlink", "Imagelink", "CName", "ForeignName", "Rating", "Comments", "Inquery", "Detail")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)


def saveData2Db(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'
        sql = '''
            insert into movie250 (
                info_link, pic_link, cname, ename, score, rating, introduction, info)
                values (%s)''' % ",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    conn = sqlite3.connect(dbpath)
    print("Created Table:", dbpath)
    c = conn.cursor()

    sql = '''
            create table movie250
                (id integer primary key autoincrement,
                info_link text,
                pic_link text,
                cname varchar,
                ename varchar,
                score numeric,
                rating numeric,
                introduction text,
                info text)
            '''

    c.execute(sql)

    conn.commit()

    conn.close()


def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    # req = requests.Request(url=url, headers=headers)
    req = urllib.request.Request(url, headers=headers)
    html = ''
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


if __name__ == "__main__":
    main()

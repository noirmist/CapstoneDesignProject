#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import os
import pymysql as mysql

# # MySQL DB 연결을 한다
# db = mysql.connect(host='localhost', user='root', password='1234', db='capstone', charset='utf8')
#
# cursor = db.cursor()
# t = cursor.execute("SELECT * FROM url_list")
#
# for rec in cursor.fetchall():
#     CRAWLING_URL = rec[1]
#     print (CRAWLING_URL)


class crawlerImageDownload:
    def imageDownlad(self, imageUrl, count):
        image = urllib.request.urlopen(imageUrl)
        fileName = 'image/image_'+ str(count) + '.jpg'
        imageFile = open(fileName, 'wb')
        imageFile.write(image.read())
        imageFile.close()


if __name__ == '__main__':
    # Crawling URL
    #CRAWLING_URL = 'http://thezam.co.kr'
    # MySQL DB 연결을 한다
    db = mysql.connect(host='localhost', user='root', password='1234', db='capstone', charset='utf8')

    cursor = db.cursor()
    t = cursor.execute("SELECT * FROM url_list")
    index = 0

    for rec in cursor.fetchall():

        try:
            CRAWLING_URL = rec[1]
            print("url : ", CRAWLING_URL)
            # 지정된 URL을 오픈하여 requset 정보를 가져옵니다
            source_code_from_URL = urllib.request.urlopen(CRAWLING_URL)



            soup = BeautifulSoup(source_code_from_URL, 'html.parser')

            for item in soup.find_all('img'):
                #print(item)
                #print(item['src'])
                src = str(item['src'])
                #print(src)
                #if(src.find('facebook')):
                #    print(src)
                if(src[0:11] == 'about:blank'):
                    continue
                if(src[0:5] == 'https'):
                    continue
                elif (src[0:7] == 'http://'):
                    src = src
                elif (src[0:2] == '//'):
                    src = 'http:'+src
                elif (src[0:1] == '/'):
                    src = 'http://thezam.co.kr' + src
                elif (src[0:1] ==''):
                    continue

                # elif (src[23:32] =='/product/'):
                #     src = 'http://thezam.co.kr/web' +src
                print(index, " : ",src)
                cid = crawlerImageDownload()
                cid.imageDownlad(src, index)
                index += 1

        except Exception:
            continue


# t = open("/Users/Dani/Documents/CapstoneDesignProject/maintest/url_list.txt", "r")
# while True:
#     line = t.readline()
#     if not line: break
#     print(line)
#     f = crawlerImageDownload()
#     f.imageDownlad(line, index)
#
#
#     size = os.path.getsize(imageFile)
#     print(size)
#     if (size > 5000):
#
# t.close()
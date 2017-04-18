import os
import time
from selenium import webdriver
from lxml import etree
import pymongo


chromedriver = "F:\TGP\firefox.exe"
connection=pymongo.MongoClient()
tdb=connection.c
post=tdb.self

driver = webdriver.Firefox()

q=0
url=""
def web(w_url):
    driver.get(w_url)
    # driver.get('https://search.jd.com/Search?keyword=%E6%9C%8D%E8%A3%85%E4%BA%AC%E4%B8%9C%E8%87%AA%E8%90%A5&enc=utf-8&wq=%E6%9C%8D%E8%A3%85%E4%BA%AC%E4%B8%9C%E8%87%AA%E8%90%A5&pvid=79463552e98d4812ae84a850009efbb0')
    driver.execute_script("window.scrollTo(0,10000)")
    time.sleep(5)
    data = driver.page_source
    code = etree.HTML(data)
    data = {}
    for i in range(1, 61):
        u_title = ".//*[@id='J_goodsList']/ul/li" + "[" + str(i) + "]" + "/div/div[4]/a/em/text()"
        u_price = ".//*[@id='J_goodsList']/ul/li" + "[" + str(i) + "]" + "/div/div[3]/strong/i/text()"
        u_commit = ".//*[@id='J_goodsList']/ul/li" + "[" + str(i) + "]" + "/div/div[5]/strong/a/text()"

        # 标题
        title = code.xpath(u_title)
        info = "".join(title)
        data['title'] = info

        # 价格
        price = code.xpath(u_price)
        data['price'] = price

        # 评论数量
        commit = code.xpath(u_commit)
        data['commit'] = commit

        # 店名
        shop = code.xpath(".//*[@id='J_goodsList']/ul/li" + "[" + str(i) + "]" + "/div/div[7]/span/a/text()")
        data['shop'] = shop

        # 是否自营
        inco = code.xpath(".//*[@id='J_goodsList']/ul/li" + "[" + str(i) + "]" + "/div//div[@class='p-icons']")
        if etree.tostring(inco[0]).find(b"img") == -1:
            data['self'] = "no_self"

        else:
            data['self'] = "self"
        data['_id'] = q*60+i

        #print(data)
        post.insert(data)



for i in range(1,101):
   url="https://search.jd.com/Search?keyword=服装京东自营&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=服装京东自营&page="+str(2*i-1)
   web(url)
   q=i
   print("已经爬完第"+str(i)+"页")

















# driver.get('https://search.jd.com/Search?keyword=%E6%9C%8D%E8%A3%85&enc=utf-8&wq=%E6%9C%8D%E8%A3%85&pvid=12da848282864849ae3ceda2666c8b72')
# #driver.get('https://search.jd.com/Search?keyword=%E6%9C%8D%E8%A3%85%E4%BA%AC%E4%B8%9C%E8%87%AA%E8%90%A5&enc=utf-8&wq=%E6%9C%8D%E8%A3%85%E4%BA%AC%E4%B8%9C%E8%87%AA%E8%90%A5&pvid=79463552e98d4812ae84a850009efbb0')
# driver.execute_script("window.scrollTo(0,10000)")
# time.sleep(5)
# data = driver.page_source
# code=etree.HTML(data)
#
# data={}
# for i in range(1, 61):
#     u_title = ".//*[@id='J_goodsList']/ul/li" + "[" + str(i) + "]" + "/div/div[4]/a/em/text()"
#     u_price=".//*[@id='J_goodsList']/ul/li" + "[" + str(i) + "]" + "/div/div[3]/strong/i/text()"
#     u_commit=".//*[@id='J_goodsList']/ul/li" + "[" + str(i) + "]" + "/div/div[5]/strong/a/text()"
#     #标题
#     title = code.xpath(u_title)
#     info = "".join(title)
#     data['title']=info
#
#     # 价格
#     price = code.xpath(u_price)
#     data['price'] = price
#
#     #评论数量
#     commit=code.xpath(u_commit)
#     data['commit']=commit
#
#     #店名
#     shop = code.xpath(".//*[@id='J_goodsList']/ul/li" + "[" + str(i) + "]" + "/div/div[7]/span/a/text()")
#     data['shop'] = shop
#
#
#     #是否自营
#     inco = code.xpath(".//*[@id='J_goodsList']/ul/li" + "[" + str(i) + "]" + "/div//div[@class='p-icons']")
#     if etree.tostring(inco[0]).find(b"img")==-1:
#         data['self']="no_self"
#
#     else:
#         data['self']="self"
#     data['_id']=i
#
#     print(data)
#     post.insert(data)











    # price=code.xpath(".//*[@id='J_goodsList']/ul/li/div/div[3]/strong/i/text()")
    # commit=code.xpath(".//*[@id='J_goodsList']/ul/li/div/div[5]/strong/a/text()")
    # #shop=code.xpath(".//*[@id='J_goodsList']/ul/li/div/div[7]/span/a/text()")
    # icons=code.xpath("//*[@id='J_goodsList']/ul//li[@class='gl-item']//div[@class='p-icons']")


    # 获取当前页面下的li标签的数量
    # num=code.xpath(".//*[@id='J_goodsList']/ul/li")
    # print(len(num))

    # print(shop)
    # for i in range(1,61):
    #     inco = code.xpath(".//*[@id='J_goodsList']/ul/li" + "[" + str(i) + "]" + "/div//div[@class='p-icons']")
    #     if etree.tostring(inco[0]).find(b"img")==-1:
    #         data['self']="no_self"
    #
    #     else:
    #         data['self']="self"
    #     print(data)

#driver.quit()


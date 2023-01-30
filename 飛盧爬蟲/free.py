#收集免費章節
#1.分析數據內容來自哪裡
    #F12開發者工具進行抓包分析
    #Network中,刷新網頁找尋數據
    #搜尋想要查找的數據,Response返回要查找的數據,Header中會有請求訊息以及url等
    #請求網址General-->Request URL , 能夠得到自己想要的小說數據
#2.code步驟：
    #1.發送請求
    #2.獲取數據
    #3.解析數據
    #4.保存數據


#1.發送請求
import requests #數據請求模組

import parsel #數據解析模組

#目錄頁url連結
link = 'https://b.faloo.com/1259955.html'

#模擬瀏覽器發送請求
headers = {
    #User-Agent 瀏覽器基本身分訊息
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

#response響應對象
html_data = requests.get(url = link, headers = headers).text  #發送請求 get是請求方式

#解析數據
#解析方法：css選擇器-->根據標籤以及屬性
#將response的文本數據(text)轉成可解析的數據

selector = parsel.Selector(html_data)

#獲取小說名字
name = selector.css('#novelName::text').get()
#print(name)

#獲取所有章節url連結, a::attr(href)獲取a中的href屬性
href = selector.css('.DivTd a::attr(href)').getall()[:58]
#print(href)
for index in href:
    url = f'https:{index}' #確定請求連結
    
    #模擬瀏覽器發送請求
    headers = {
        #User-Agent 瀏覽器基本身分訊息
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
    
    #response響應對象
    response = requests.get(url = url, headers = headers)  #發送請求 get是請求方式
    
    #2.獲取數據-->獲取response的文本數據(text)
    #print(response.text)
    
    #解析數據
    #解析方法：css選擇器-->根據標籤以及屬性
    #將response的文本數據(text)轉成可解析的數據
    
    selector = parsel.Selector(response.text)
    #提取小說章節標題
    title = selector.css('.nr_center .c_left .c_l_title h1::text').get()
    #print(title)
    
    #提取小說內容
    content_list = selector.css('div.noveContent p::text').getall()
    #print(content_list)
    
    #將列表content_list轉換成字串content
    content = '\n'.join(content_list)
    #print(content)
    
    #保存數據
    with open(name + '.txt', mode='a', encoding='utf-8') as f:
        f.write(title)
        f.write('\n')
        f.write(content)
        f.write('\n')
        print('成功保存' + title)
    
    




















from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time

#検索欄にキーワードを記入
keys = input('検索キーワード:')

#Google Chromeのドライバーを用意
browser = webdriver.Chrome()



#Google_mapを開く
url = 'https://www.google.com/'
browser.get(url)
time.sleep(2)

google_search = browser.find_element_by_name('q')
google_search.send_keys('google map')

searching_btn = browser.find_element_by_name('btnK')
browser.implicitly_wait(10)
searching_btn.click()


seaching_result = browser.find_element_by_xpath('/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/a')
seaching_result.click()



#データ入力
serching_text = browser.find_element_by_id('searchboxinput')
serching_text.send_keys(keys)
time.sleep(2)

#クリック
serch_btn = browser.find_element_by_id('searchbox-searchbutton')
browser.implicitly_wait(10)
serch_btn.click()

time.sleep(3)


for s in range(1):
    shops_lists = browser.find_elements_by_class_name('hfpxzc')
    for n in shops_lists:
        nums = n
        nums.click()
        
        time.sleep(4)
        shop_info = browser.page_source
        soup = BeautifulSoup(shop_info,'html.parser')

        title = soup.find(class_='DUwDvf fontHeadlineLarge')
        link = soup.find_all(class_='Io6YTe fontBodyMedium')
        lists = []
        for l in link:
            list=l.text
            lists.append(list)

        print('検索キーワード：' + keys)
        print('--------------------------')
        print(title.text)
        print(lists[0])
        print(lists[2])
        print('--------------------------')

        back_btn = browser.find_element_by_xpath('/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/div[3]/span/button')
        back_btn.click()
        time.sleep(1)

        height=1500
        browser.execute_script('window.scrollTo(0,{});'.format(height))
        height += 100
        time.sleep(1)
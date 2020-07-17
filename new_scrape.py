from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep
import re
import requests as res
base  ="https://www.wikiart.org/en/artists-by-genre/abstract#!#resultType:text"
driver = webdriver.Chrome('/usr/bin/chromedrive')
driver.get(base)
html = driver.page_source

contain = bs(html,'html.parser').find('div',class_='masonry-text-view ng-scope')

for i in contain.div.ul:
    print(i)
# container = driver.find_elements_by_xpath('/html/body/div/div[1]/section/main/div[3]/div[2]/div/div/ul[1]')
# print(container)


# html = res.get(base)
# text = html.text
# print(text)
# sleep(2)
# container = bs(text,'html.parser').find('div',class_='masonry-text-view ng-scope').text
# print(container)
# for contain in container:
#     print(contain)
    # break
# html = driver.find_element_by_class_name('ng-scope')

# print(html)


# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# sleep(2)
# button = driver.find_element_by_class_name('masonry-load-more-button').click()
# button = driver.find_element_by_link_text('LOAD MORE').click()

# html = driver.page_source
# new_dict ={}
# container = bs(html,'html.parser').find('li',class_='dottedItem').text
# container = re.split('',container)[1]
# print(container)







from collections import OrderedDict
# new_dict = {}
#
# num = [1,2,3,4,5,6,7,8]
# names = ['bhanu','bhawna','rick','motry','eve','ryan','baxter','venessa']
#
# for i,b in enumerate(names):
#
#     new_dict.update({b:num[i]})
#
#
# # print(new_dict)
#
# for x,c in new_dict.items():
#     print(x,c)


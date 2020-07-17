from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup as bs
import re
import math


class Wiki_Art():
    list_urls_nums = {}
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        # self.driver = webdriver.Chrome('/usr/bin/chromedrive')
        chrome_driver= '/usr/bin/chromedrive'
        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chrome_driver)

        # list_urls_nums = {}


    def base(self,url):

        list_urls_nums = {}
        self.url =url
        self.class_name = 'dottedItem'
        self.driver.get(self.url)
        html = self.driver.page_source
        container  =bs(html,'html.parser').find_all('li',class_=self.class_name)

        for contain in container:
            link = contain.a.get('href')
            full_link = 'https://www.wikiart.org'+link+'#!#resultType:text'
            # print(contain.text)
            number = re.split(' ',contain.text)[-1]
            print(number)

            list_urls_nums.update({full_link:number})
        return self.genres(list_urls_nums)
    #
    def genres(self,list_url_nums):
        self.list_urls_nums=list_url_nums
        for link,number in list_url_nums.items():
            self.driver.get(link)
            sleep(3)
            clicks = math.ceil(number/60)
            for i in range(clicks):
                sleep(2)
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                sleep(2)
                button = self.driver.find_element_by_class_name('masonry-load-more-button').click()



bot = Wiki_Art()
url = 'https://www.wikiart.org/en/artists-by-genre'
# class_name='dottedItem'
bot.base(url)
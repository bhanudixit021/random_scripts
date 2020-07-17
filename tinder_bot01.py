from selenium import webdriver
from time import sleep
from secret import username, password


# base = "https://www.google.com"
# ch = "/usr/bin/chromedrive"
# driver = webdriver.Chrome(ch)
# html = driver.get(base)

class Tinder_Bot():

    def __init__(self):
        self.ch = "/usr/bin/chromedrive"
        self.driver = webdriver.Chrome(self.ch)

    def login(self):
        self.driver.get('https://www.tinder.com')
        sleep(5)

        try:
            pop = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
            pop.click()
        except:
            pass

        more_opts =  self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
        more_opts.click()
        fb_login = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_login.click()

        # switching windows
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in =  self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        passwrd_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        passwrd_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()

bot = Tinder_Bot
bot.__init__()
bot.login()







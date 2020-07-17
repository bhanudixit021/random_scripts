from selenium import webdriver

base = 'https://www.google.com'

driver = webdriver.Chrome('/usr/bin/chromedrive')
driver.get(base)
html = driver.page_source
print(html)
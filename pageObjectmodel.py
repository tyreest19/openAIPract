# from selenium import webdriver as driver
#
# class GoogleHomePage(object):
#     def __init__(self, driver):
#         self.driver = driver.Chrome()
#         self.driver.get('http://www.google.com/');
#
#     def search(self, query):
#
#         searchPage = self.driver.find_element("name", "q")
#         searchPage.send_keys(query)
#
# googleHomePage = GoogleHomePage(driver)
# googleHomePage.search('Test')
# ============== This was all created by a gpt model =======================

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com/")

search_bar = driver.find_element("name", "q")

search_bar.send_keys("test")

search_bar.submit()

from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("翅尖")
driver.find_element_by_id('su').click()
driver.find_element_by_xpath('//div[@class="search_tool"]').click()
driver.find_element_by_xpath('//span[@class="search_tool_tf "]/i').click()
sleep(3)
driver.find_element_by_xpath('//p[@class="c-tip-custom-st"]/input').send_keys('2021-07-01')
sleep(3)




sleep(3)
driver.quit()

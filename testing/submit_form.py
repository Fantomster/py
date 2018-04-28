from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS(executable_path='C:/Users/user/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get('http://pythonscraping.com/pages/files/form.html')

firstnameField = driver.find_element_by_name('firstname')
lastnameField = driver.find_element_by_name('lastname')
submitButton = driver.find_element_by_id('submit')

# Метод 1
firstnameField.send_keys('Ryan')
lastnameField.send_keys('Mitchell')
submitButton.click()
# !Метод 1

# Метод 2
actions = ActionChains(driver).click(firstnameField).send_keys('Ryan').click(lastnameField).send_keys('Mitchell').send_keys(Keys.RETURN)
actions.perform()
# !Метод 2

print(driver.find_element_by_tag_name('body').text)
driver.close()
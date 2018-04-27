from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='C:/Users/user/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get('http://pythonscraping.com')
driver.implicitly_wait(1)
# print(driver.get_cookies())

savedCookies = driver.get_cookies()

driver2 = webdriver.PhantomJS(executable_path='C:/Users/user/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver2.get('http://pythonscraping.com')
driver2.delete_all_cookies()
for cookie in savedCookies:
    print(cookie)
    # cookie = {"domain": "pythonscraping.com", "httponly": False, "name": "has_js", "path": "/", "secure": False, "value": "1"}
    driver2.add_cookie(cookie)

exit()
driver2.get('http://pythonscraping.com')
driver.implicitly_wait(1)
print(driver2.get_cookies())
#Suka nerabotaet
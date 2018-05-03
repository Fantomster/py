from selenium import webdriver

service_args = ['--proxy=localhost:9150', '--proxy-type=socks5', ]
driver = webdriver.PhantomJS(executable_path='C:/Users/administrator/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe', service_args=service_args)
driver.get('http://icanhazip.com')
print(driver.page_source)
driver.close()
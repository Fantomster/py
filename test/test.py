from selenium import webdriver

ff = webdriver.Chrome(executable_path='./chromedriver_win32/chromedriver.exe')
ff.get("https://www.google.ru/")
# find the element that's name attribute is q (the google search box)
inputElement = ff.find_element_by_id("lst-ib")

# type in the search
inputElement.send_keys("cheese! cheese!")

# submit the form (although google automatically searches now without submitting)
inputElement.submit()

ff.get_screenshot_as_file('./screenshots/google.png')
print(ff)
exit()
try:
    element = WebDriverWait(ff, 10).until(EC.presence_of_element_located((By.ID, "lst-ib")))
finally:
    ff.quit()
print(element)
# driver.get("https://www.google.com")
# driver.get_screenshot_as_file('google.png')
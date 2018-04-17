from urllib.request import urlopen
from bs4 import BeautifulSoup
try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    if html is None:
        print("URL is not found")
    else:
        #программа продолжает работа
        print(1)
except HTTPError as e:
    print(e)
    #возвратимь null, прервать или выполнять операции по "Плану Б"
else:
    #программа продолжает работы. Примечание: если возвращаете или прерываете в #exception catch, оператор "else" использовать не нужно
    print(1)
bsObj = BeautifulSoup(html.read())

try:
    badContent = bsObj.nonExistingTag.anotherTag
except AttributeError as e:
    print("Tag was not found")
else:
    if badContent == None:
        print("Tag was not found")
    else:
        print(badContent)


# print(bsObj)
print(bsObj.h1)
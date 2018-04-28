import unittest
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import re
import random

class TestWikipedia(unittest.TestCase):
    bsObj = None
    url = None

    def test_PageProperties(self):
        global bsObj
        global url

        url = 'http://en.wikipedia.org/wiki/Monty_Python'
        #Тестируем первые 100 страниц
        for i in range(1, 100):
            bsObj = BeautifulSoup(urlopen(url))
            titles = self.titleMatchesURL()
            self.assertEquals(titles[0], titles[1])
            self.assertTrue(self.contentExists())
            url = self.getNextLink()
        print('Done!')

    def titleMatchesURL(self):
        global bsObj
        global url
        print(bsObj.find('h1'))
        pageTitle = bsObj.find('h1').get_text()
        try:
            urlTitle = url[(url.index('/wiki/')+6):]
        except ValueError:
            print(url.index('/wiki/')+6)

        urlTitle = url[(url.index('/wiki/')+6):]
        urlTitle = urlTitle.replace('_', ' ')
        urlTitle = urllib.request.unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]

    def contentExists(self):
        global bsObj
        content = bsObj.find('div', {'id':'mw-content-text'})
        if content is not None:
            return True
        return False

    def getNextLink(self):
        global bsObj
        global url
        externalLinks = self.getExternalLinks()

        return externalLinks[random.randint(0, len(externalLinks)-1)]

    def getExternalLinks(self):
        global bsObj
        externalLinks = []
        #Находим все ссылки, которые начинаются с "http" или "www"
        #не содержат текущего URL-адреса
        for link in bsObj.findAll("a", href=re.compile("^(http|www).*$")):
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in externalLinks:
                    externalLinks.append(link.attrs['href'])
        return externalLinks

    def splitAddress(self, address):
        addressParts = address.replace("http://", "").split("/")
        return addressParts

if __name__ == '__main__':
    unittest.main()

#Извлекаем список всех внешних ссылок, найденных на странице
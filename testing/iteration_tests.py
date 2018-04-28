import unittest
from urllib.request import urlopen
from bs4 import BeautifulSoup

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
        pageTitle = bsObj.find('h1').get_text()
        urlTitle = url[(url.index('/wiki/')+6)]
        urlTitle = urlTitle.replace('_', ' ')
        urlTitle = unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]

    def contentExists(self):
        global bsObj
        content = bsObj.find('div', {'id':'mw-content-text'})
        if content is not None:
            return True
        return False

    def getNextLink(self):
        global bsObj
        bsObj = BeautifulSoup(html)
        externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
        if len(externalLinks) == 0:
            internalLinks = getInternalLinks(startingPage)
            return getNextExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
        else:
            return externalLinks[random.randint(0, len(externalLinks)-1)]

if __name__ == '__main__':
    unittest.main()



#Извлекаем список всех внешних ссылок, найденных на странице
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    #Находим все ссылки, которые начинаются с "http" или "www"
    #не содержат текущего URL-адреса
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getNextExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

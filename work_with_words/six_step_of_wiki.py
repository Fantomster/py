from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd=None, db='scraping', charset='utf8')

cur = conn.cursor()
cur.execute('USE scraping')

class SolutionFound(RuntimeError):
    def __init__(self, message):
        self.message = message

def getLinks(fromPageId):
    cur.execute("SELECT toPageId FROM links WHERE fromPageId = %s", (fromPageId))
    if cur.rowcount == 0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]

def constructDict(currentPageId):
    links = getLinks(currentPageId)
    if links:
        return dict(zip(links, [{}]*len(links)))
    return {}

#Дерево ссылок может быть пустым или содержать ссылки
def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0:
        #Останавливаем рекурсию и возвращаемся
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree:
            #Ссылки не найдены. Продолжение в этом узле невозможно
            return {}
    if targetPageId in linkTree.keys():
        print("TARGET "+str(targetPageId)+" FOUND!")
        raise SolutionFound("PAGE: "+str(currentPageId))

    for branchKey, branchValue in linkTree.items():
        try:
            #Выполняем рекурсивный вызов для продолжения построения дерева
            linkTree[branchKey] = searchDepth(targetPageId, branchKey, branchValue, depth-1)
        except SolutionFound as e:
            print(e.message)
            raise SolutionFound("PAGE: "+str(currentPageId))
    return linkTree

try:
    searchDepth(29, 1, {}, 5)
    print("No solution found")
except SolutionFound as e:
    print(e.message)
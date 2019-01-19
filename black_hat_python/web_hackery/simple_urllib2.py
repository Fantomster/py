from urllib.request import urlopen

body = urlopen("https://ya.ru")

print(body.read())
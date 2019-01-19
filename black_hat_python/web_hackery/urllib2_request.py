from urllib.request import urlopen, Request

url = "https://ya.ru"

headers = {}
headers['User-Agent'] = "GoogleBot"

request = Request(url, headers=headers)
response = urlopen(request)

print(response.read())
response.close()

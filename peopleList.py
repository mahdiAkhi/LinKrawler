from requests_html import HTMLSession
cookies = {'li_at': '***'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
    'Content-Type': 'text/html',
}
r = requests.get('https://www.linkedin.com/in/mahdiakhi/', cookies=cookies,headers=headers)

file = open('result.html',r'w+')
print(r.content)
# file.write(r.content)
file.close()
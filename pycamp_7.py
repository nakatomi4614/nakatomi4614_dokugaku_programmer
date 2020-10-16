# https://pycamp.pycon.jp/textbook/7_scraping.html
import requests
from bs4 import BeautifulSoup

def main():
    params = {
        'keyword': 'python',
        'ym': '201812',
    }
    url = 'https://connpass.com/api/v1/event/'
    r = requests.get(url, params=params)
    event_info = r.json()  # レスポンスのJSONを変換

    print('件数:', event_info['results_returned'])  # 件数を表示
    for event in event_info['events']:
        print(event['title'])
        print(event['started_at'])

if __name__ == '__main__':
    main()
print("スクレイピング\r\n")
def main2():
    url = 'https://pycon.jp/2017/ja/sponsors/'
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    sponsors = soup.find_all('div', class_='sponsor-content')
    for sponsor in sponsors:
        url = sponsor.h3.a['href']
        name = sponsor.h4.text
        print(name, url)

if __name__ == '__main__':
    main2()

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)

payload = {'key1': 'value1', 'key2': 'value2'} # POST するパラメーター
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
# http://httpbin.org/get?key2=value2&key1=value1
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)

r = requests.get('https://www.python.org/blogs/')
soup = BeautifulSoup(r.content, 'html.parser') # 取得したHTMLを解析
print(soup.title) # titleタグの情報を取得
print(soup.title.name)
print(soup.title.string) # titleタグの文字列を取得
print(soup.a)

print(len(soup.find_all('a'))) # 全ての a タグを取得しt len() で件数を取得

#h1とかの数を表示している
print(len(soup.find_all('h1')))
print(len(soup.find_all(['h1', 'h2', 'h3'])))
print(len(soup.find_all('h3', {'class': 'event-title'})))
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

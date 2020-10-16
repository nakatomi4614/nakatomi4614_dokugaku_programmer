# 16章　Bashの使い方など

# git bashつかったらいいのか？
# Bashとcmdは結構違う
# 実行環境はPythonコンソールで
# | パイプ　前｜後　前のコマンドをやってあと後のコマンドをやる
# git bashにはsudoは無い　Unix系のみ
# メモしかねーなｗ

# 20章　知識を一つにまとめる
# HTML
# pycharmのプロ版なら実行できるが、community版はできないのでメモ帳ブラウザ環境で実行する
"""
<!--This is a comment in HTML.
Save this file as index.html-->
<!-- 略 -->

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Website</title>
</head>
<body>
    Hello, World!
    <a href="https://www.google.com"/>here</a>
</body>
</html>
"""
#BeautifulSoup

import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("link"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

news = "https://news.google.com/topstories?hl=ja&gl=JP&ceid=JP:ja"
Scraper(news).scrape()

# 上記実行してもa tagが無いことに気づく
# このままだと表示されないのでdebugerでspの中身を調査する
# <link>ってタグがlinkらしい
# でねぇ…
# これ参照先ソースが複雑すぎてこんな単純なスクレイピングは無理じゃねえの？ってなっている




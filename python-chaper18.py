# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:50:41 2020

@author: 0604000030
"""

#chapter18
#package管理

#Flaskインストール済み
from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello, World!"

app.run(port = 8000)

#http://127.0.0.1:8000/ と入力したらHello, World!が表示される

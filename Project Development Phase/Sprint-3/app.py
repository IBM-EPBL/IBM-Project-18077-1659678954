#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import ibm_db
from flask import Flask, render_template, request, redirect
from newsapi import NewsApiClient

conn = ibm_db.connect(
        "DATABASE=bludb;HOSTNAME=21fecfd8-47b7-4937-840d-d791d0218660.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31864;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=jfs93288;PWD=7DLlZanU3kI83jSN;",
        "", "")

app = Flask(__name__, template_folder='tempelate', static_folder='Static', static_url_path='/Static/')

login = False
user = None



@app.route("/news")
def news():
    global main_article, contents, all
    api_key = 'd5f3ead3b25c4fa3b3d25a142b816e59'

    newsapi = NewsApiClient(api_key=api_key)

    top_headlines = newsapi.get_top_headlines(sources="bbc-news")
    all_articles = newsapi.get_everything(sources="buzzfeed") #, MakeUseOf, PRNewswire, The Economist, the-verge

    t_articles = top_headlines['articles']
    a_articles = all_articles['articles']

    news = []
    desc = []
    img = []
    p_date = []
    url = []
    auth = []

    for i in range(len(t_articles)):
        main_article = t_articles[i]

        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])
        auth.append(main_article['author'])

        contents = zip(news, desc, img, p_date, url, auth)

    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []
    url_all = []
    auth_all = []

    for j in range(len(a_articles)):
        main_all_articles = a_articles[j]

        news_all.append(main_all_articles['title'])
        desc_all.append(main_all_articles['description'])
        img_all.append(main_all_articles['urlToImage'])
        p_date_all.append(main_all_articles['publishedAt'])
        url_all.append(main_article['url'])
        auth_all.append(main_article['author'])

        all = zip(news_all, desc_all, img_all, p_date_all, url_all, auth_all)

    return render_template('blog.html', all={'all': all, 'head': contents, 'length': len(auth_all)})


    @app.route("/login", methods=['POST', 'GET'])
    def loginUser():
        global login, user
        if request.method == 'POST':
            userEmail = request.form.get("email")
            userPassword = request.form.get("pswd")
            stmt = ibm_db.exec_immediate(conn, "SELECT * FROM USERS where username='"+userEmail+"' and password='"+userPassword+"'")
            while ibm_db.fetch_row(stmt):
                login = True
                user = ibm_db.result(stmt, 1)
                return redirect('/news')
            return render_template("login.html", yes=True)
        else:
            return render_template('login.html')


    @app.route("/register", methods=['POST', 'GET'])
    def registerUserData():
        global login, user
        if request.method == 'POST':
            userName = request.form.get("un")
            userEmail = request.form.get("ue")
            userPassword = request.form.get("up")

            print(userEmail, userName, userPassword)
            stmt = ibm_db.exec_immediate(conn, "INSERT INTO USERS values(1,'"+userEmail+"', '"+userPassword+"','"+userName+"')")
            login = True
            user = userName
            return redirect('/news')
        else:
            return render_template('register.html')


    @app.route("/")
    def home():
        api_key = 'd5f3ead3b25c4fa3b3d25a142b816e59'

        newsapi = NewsApiClient(api_key=api_key)

        top_headlines = newsapi.get_top_headlines(sources="bbc-news")
        all_articles = newsapi.get_everything(sources="buzzfeed")  # , MakeUseOf, PRNewswire, The Economist, the-verge

        t_articles = top_headlines['articles']

        news = []
        desc = []
        img = []
        p_date = []
        url = []
        auth = []

        for i in range(len(t_articles)):
            main_article = t_articles[i]

            news.append(main_article['title'])
            desc.append(main_article['description'])
            img.append(main_article['urlToImage'])
            p_date.append(main_article['publishedAt'])
            url.append(main_article['url'])
            auth.append(main_article['author'])

            contents = zip(news, desc, img, p_date, url, auth)
        return render_template("index.html", data = [login, user, contents])


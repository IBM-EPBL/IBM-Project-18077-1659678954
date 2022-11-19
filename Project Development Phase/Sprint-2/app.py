import os
import ibm_db
from flask import Flask, render_template, request, redirect
from newsapi import NewsApiClient

conn = ibm_db.connect(
        "DATABASE=bludb;HOSTNAME=21fecfd8-47b7-4937-840d-d791d0218660.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31864;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=jfs93288;PWD=7DLlZanU3kI83jSN;",
        "", "")

app = Flask(__name__, template_folder='tempelate', static_folder='Static', static_url_path='/Static/')

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


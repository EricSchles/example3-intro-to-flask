from flask import render_template, request, redirect, url_for, jsonify, flash
from app import app

@app.route("/", methods=["GET","POST"])
@app.route("/index", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/add/<int:first>/<int:second>", methods=["GET","POST"])
@app.route("/add",methods=["GET","POST"])
def add(first='',second=''):
    if first == '':
        first = int(request.form.get("first"))
    if second == '':
        second = int(request.form.get("second"))
    result = first + second
    return render_template("index.html",result=result)

  

@app.route("/send_data", methods=["GET","POST"])
def send_data():
    data={"Eric Schles":"eric.schles@syncano.com",
          "job":"developer evangelist",
          "mission":"end slavery",
          "training for":"the olympics",
          "hobbies":["guitar","rock climbing"],
          "friends":"everyone"
          }
    return render_template("index.html",data=jsonify(data).get_data())

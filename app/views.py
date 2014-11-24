from flask import render_template, request, redirect, url_for, jsonify

@app.route("/", methods=["GET","POST"])
@app.route("/index", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/add/<int:first>/<int:second>")
@app.route("/add")
def add(first='',second=''):
    if first == '':
        first = int(request.get("first"))
    if second == '':
        second = int(request.get("second"))
    result = first + second
    return render_template("index.html",result=result)

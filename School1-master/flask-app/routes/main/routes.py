from app import app
from flask import render_template

@app.route("/")
def main():
    return render_template("main/index.html")

@app.route("/calc/<int:x>/<int:y>/<oper>")
def calc(x,y,oper):
    if oper == "+":
        res = x + y
    else:
        res = x - y
    return render_template("main/calc.html", x=x, y=y, res=res, oper=oper)


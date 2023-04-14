from app import app
from flask import render_template
from models import Article

@app.route("/")
def main():
    articles = Article.query.order_by("id").all()
    return render_template("main/index.html", articles=articles)

@app.errorhandler(404)
def not_found(e):
    return render_template("main/not_found.html"), 404

@app.route("/article/<int:id>")
def article_details(id):
    article = Article.query.get(id)
    if article is None:
        return not_found(404)
    return render_template("main/article_detail.html", article=article)

@app.route("/calc/<int:x>/<int:y>/<oper>")
def calc(x,y,oper):
    if oper == "+":
        res = x + y
    else:
        res = x - y
    return render_template("main/calc.html", x=x, y=y, res=res, oper=oper)


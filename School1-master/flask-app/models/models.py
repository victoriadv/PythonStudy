from app import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
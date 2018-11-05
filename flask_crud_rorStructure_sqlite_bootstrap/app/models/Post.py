from app.setup import app,db
#from ..controllers.posts import *


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.VARCHAR(255))
    created_at = db.Column(db.TIMESTAMP)

    def __init__(self, title,content,created_at):
        self.title = title
        self.content = content
        self.created_at = created_at

    def __repr__(self):
        return '<E-mail %r>' % self.title
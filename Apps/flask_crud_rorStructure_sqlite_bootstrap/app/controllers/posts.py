from app.setup import app,db,render_template,request,random,fake
from ..models.Post import *
from datetime import datetime

@app.route('/posts')
def post_index(): 
  posts = Post.query.all()
  return render_template('posts/index.html',posts=posts)

@app.route('/post/add', methods=['POST'])
def posts():
    if request.method == 'POST':
        try:
          title = request.form['title']
          content= request.form['content']
          if content =="":
            content=fake.text()
          created_at = datetime(2018,9,28,10,10,10)
        except:
          title = fake.first_name()
          content= fake.text()
          created_at = datetime(2018,9,28,10,10,10)
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(Post).filter(Post.title == title).count():
            reg = Post(title,content,created_at)
            db.session.add(reg)
            db.session.commit()
            return render_template('posts/success.html',title=title)
    return render_template('posts/index.html')
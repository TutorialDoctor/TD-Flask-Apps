from app.setup import app,db,render_template,request,random,fake
from ..models.Post import *
from datetime import datetime

@app.route('/posts')
def post_index(): 
  posts = Post.query.all()
  return render_template('posts/index.html',posts=posts)

@app.route('/post/add', methods=['POST'])
def create_post():
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
  
@app.route('/posts/<int:post_id>')
def show_post(post_id):
    post = Post.query.filter_by(id=post_id).one()
    return render_template('posts/show.html', post=post)

@app.route('/posts/<int:post_id>/edit',methods=['GET','POST'])
def edit_post(post_id):
    post = Post.query.filter_by(id=post_id).one()
    if request.method == 'POST':
        try:
          title = request.form['title']
          content = request.form['content']
          post.title = title
          post.content = content
          if content =="":
            post.content=fake.text()
          post.created_at = datetime(2018,9,28,10,10,10)
        except:
          post.title = fake.first_name()
          post.content= fake.text()
          post.created_at = datetime(2018,9,28,10,10,10)
        # Check that email does not already exist (not a great query, but works)
        if db.session.query(Post).filter(Post.title == title).count():
            db.session.commit()
            return render_template('posts/post_edit_success.html',title=title)
    elif request.method == "GET":
      return render_template('posts/edit.html',title=post.title,post=post)
    
    return render_template('posts/index.html')
  
    #return render_template('posts/edit.html', post=post)

@app.route('/posts/<int:post_id>/delete')
def delete_post(post_id):
    post = Post.query.filter_by(id=post_id).one()
    post_title = post.title
    db.session.delete(post)
    db.session.commit()
    return render_template('posts/delete.html',post_title=post_title)
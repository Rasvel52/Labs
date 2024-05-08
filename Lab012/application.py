from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Post {self.id}>'
app.app_context().push()
db.create_all()

posts = []

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/main')
def re_main():
    return redirect(url_for('main'))

@app.route('/Posts')
def Posts():
    posts = Post.query.all()
    return render_template('History.html', posts=posts)

@app.route('/Posts')
def re_Posts():
    return redirect(url_for('Posts'))

@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('add_post'))
    return render_template('add_post.html')

if __name__ == '__main__':
    app.run(debug=True)
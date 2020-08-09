from flask import render_template, session
from app.model.user import User
from app.model.post import Post, posts_Schema
from app.model.ImgPost import ImgPost

import base64


def index():
	user = None
	if 'user_id' in session:
		user = User.query.filter_by(id=session['user_id']).first()
	posts = Post.query.all()
	imgs  = ImgPost.query.all()
	dic = {}
	for img in imgs:
		if img.id_post in dic:
			dic[img.id_post].append(base64.b64encode(img.imagem_dt).decode('ascii'))
		else:
			dic[img.id_post] = [base64.b64encode(img.imagem_dt).decode('ascii')]
	
	return render_template('index.html',user=user,imgs=dic,posts=posts_Schema.dump(Post.query.all()))
from flask import render_template, session

import base64

from app.model.user import User
from app.model.user_img import UserImg
from app.model.post import Post, posts_Schema
from app.model.reacoes import Reacoes
from app.model.comentario import Comentario
from app.model.ImgPost import ImgPost



def index():
	
	user = None
	userImg = None
	if 'user_id' in session:
		user = User.query.filter_by(id=session['user_id']).first()
		img = UserImg.query.filter_by(id_user=user.id).first()
		if img:
			userImg = base64.b64encode(img.imagem).decode('ascii')
		


	posts = posts_Schema.dump(Post.query.all())
	for post in posts:
		post["user"] = User.query.filter_by(id=post["id_user"]).first()
		img = UserImg.query.filter_by(id_user=post['user'].id).first()
		if img:
			post['perfil'] = base64.b64encode(img.imagem).decode('ascii')
		post["comm"] = Comentario.query.filter_by(id_post=post["id"]).all()
		post['reac'] = []
		reacao = Reacoes.query.filter_by(id_post=post['id']).all()
		for re in reacao:
			post['reac'].append(re.id_user)
			if user:
				if user.id == re.id_user:
					post["Liked"] = True
	posts.reverse()



	imgs  = ImgPost.query.all()
	dic = {}
	for img in imgs:
		if img.id_post in dic:
			dic[img.id_post].append(base64.b64encode(img.imagem_dt).decode('ascii'))
		else:
			dic[img.id_post] = [base64.b64encode(img.imagem_dt).decode('ascii')]

	
	return render_template('index.html',user=user,imgs=dic,posts=posts,userImg=userImg)
	
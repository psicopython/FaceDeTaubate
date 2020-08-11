from flask import render_template, session

import base64

from app.model.user import User
from app.model.user_img import UserImg
from app.model.post import Post, posts_Schema
from app.model.reacoes import Reacoes
from app.model.comentario import Comentario
from app.model.ImgPost import ImgPost



def index():
	
	user, userImg = None, None
	
	if 'user_id' in session:
		user = User.query.filter_by(id=session['user_id']).first()
		img = UserImg.query.filter_by(id_user=session['user_id']).first()
		if img:
			userImg = base64.b64encode(img.imagem).decode('ascii')
		


	posts = Post.query.all()
	for post in posts:
	
	
		post.user = User.query.filter_by(id=post.id_user).first()
		img = UserImg.query.filter_by(id_user=post.user.id).first()
		if img:
			post.user.img = base64.b64encode(img.imagem).decode('ascii')
		
		
		listComm=[]
		comms = Comentario.query.filter_by(id_post=post.id).all()
		for comm in comms:
			user_comm = User.query.filter_by(id=comm.id_user).first()
			img = UserImg.query.filter_by(id_user=user_comm.id).first()
			user_comm.img = base64.b64encode(img.imagem).decode('ascii')
			listComm.append({'data':comm.data,'body':comm.body,'id':comm.id,'id_post':comm.id_post,'user':user_comm})
	
		post.commLen = len(listComm)
		post.comm = listComm
	
	
		reacs = []
		reacao = Reacoes.query.filter_by(id_post=post.id).all()
		for re in reacao:
			reacs.append({'data':re.data,'user':User.query.filter_by(id=re.id_user).first(),'post':re.id_post})
			if user:
				if user.id == re.id_user:
					post.Liked = True
		
		post.reactLen = len(reacs)
		post.reacs = reacs
		
	posts.reverse()



	imgs  = ImgPost.query.all()
	dic = {}
	for img in imgs:
		if img.id_post in dic:
			dic[img.id_post].append(base64.b64encode(img.imagem_dt).decode('ascii'))
		else:
			dic[img.id_post] = [base64.b64encode(img.imagem_dt).decode('ascii')]

	
	return render_template('index.html',user=user,imgs=dic,posts=posts,userImg=userImg)
	
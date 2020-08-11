from flask import (
	redirect, request,
	render_template,
	current_app,session,
)

import base64

from app.model.user import User
from app.model.user_img import UserImg

from app.model.post import Post
from app.model.ImgPost import ImgPost
from app.model.reacoes import Reacoes
from app.model.comentario import Comentario


def perfil(id):
	
	user, userImg, user_local = None, None, None
	
	
	if not id:
		return redirect('/')
	
	
	
	if 'user_id' in session:
		try:
			user = User.query.filter_by(id=session['user_id']).first()
			img = UserImg.query.filter_by(id_user=user.id).first()
			user.img = base64.b64encode(img.imagem).decode('ascii')
		except:
			session.pop('user_id',None)
		
	
	user_local = User.query.filter_by(id=id).first()
	if user_local:
		img = UserImg.query.filter_by(id_user=user_local.id).first()
		if img:
			user_local.img = base64.b64encode(img.imagem).decode('ascii')
	else:
		return redirect('/')
	
	posts = Post.query.filter_by(id_user=id).all()
	for post in posts:
		
		
		imgs = ImgPost.query.filter_by(id_post=post.id).all()
		imgList = []
		if imgs:
			for img in imgs:
				imgList.append({'imagem': base64.b64encode(img.imagem_dt).decode('ascii'),
								 'data':img.data_upl,'id_post':img.id_post})
			post.imgs = imgList
		
		
		
		dicComm = {}
		comms = Comentario.query.filter_by(id_post=post.id).all()
		for comm in comms:
			dicComm[post.id] = {'comm':comm.body,'id_user':comm.id_user}
		post.comm = dicComm
		
		
		
		dicReac = {}
		reacs = Reacoes.query.filter_by(id_post=post.id).all()
		dicReac['len']= len(reacs)
		dicReac['id_users'] = []
		for re in reacs:
			dicReac['id_users'].append(re.id)
			if user:
				if re.id_user == user.id:
					post.Liked = True
		post.reacs = dicReac
	posts.reverse()
	return render_template('perfil.html',posts=posts,user=user,user_local=user_local)
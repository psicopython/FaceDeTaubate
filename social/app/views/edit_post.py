from flask import (
	redirect, request,
	render_template, session,
)

import base64

from app.model import db
from app.model.post import Post
from app.model.ImgPost import ImgPost
from app.model.comentario import Comentario



def edit_post(pag,id):
	if not 'user_id' in session:
		return redirect('/')
	if pag.upper() == 'POST':
		post = Post.query.filter_by(id=id).first()
		if post:
			if post.id_user != session['user_id']:
				return redirect('/')
		else:
			return redirect('/')
			
		if request.method.upper() == 'POST':
			body = request.form['body']
			bodyLast = Post.query.filter_by(id=id).update({'body_post':body})
			db.session.commit()
			return redirect('/')
			
			
		else:
			post = Post.query.filter_by(id=id).first()
			imgTmp = ImgPost.query.filter_by(id_post=id).all()
			imgs = {}
			for img in imgTmp:
				if post.id in imgs:
					imgs[post.id].append(base64.b64encode(img.imagem_dt).decode('ascii'))
				else:
					imgs[post.id] = [base64.b64encode(img.imagem_dt).decode('ascii')]
					
			return render_template('edit_post.html',post=post,imgs=imgs,pag=pag)
	
	
	elif pag.upper() == 'COMM':
	
		comm = Comentario.query.filter_by(id=id).first()
		if not comm or comm.id_user != session['user_id']:
			return redirect('/')
			
		if request.method.upper() == 'POST':
			body = request.form['body']
			bodyLast = Comentario.query.filter_by(id=id).update({'body':body})
			db.session.commit()
			return redirect('/')
			
			
		else:
			comm = Comentario.query.filter_by(id=id).first()
			#imgTmp = ImgPost.query.filter_by(id_post=id).all()
			#imgs = {}
			#for img in imgTmp:
			#	if post.id in imgs:
			#		imgs[post.id].append(base64.b64encode(img.imagem_dt).decode('ascii'))
			#	else:
			#		imgs[post.id] = [base64.b64encode(img.imagem_dt).decode('ascii')]
					
			return render_template('edit_post.html',post=comm,pag=pag)
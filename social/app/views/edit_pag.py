from flask import (
	redirect, request, flash,
	render_template, session,
	current_app,
)

import base64


from app.model.post import Post
from app.model.ImgPost import ImgPost

from app.model.user import User
from app.model.user_img import UserImg

from app.model.amigo import Solicitacao as Sl


from app.model.ImgPost import ImgComm
from app.model.comentario import Comentario



def edit_pag(pag,id):
	if not 'user_id' in session:
		return redirect('/')
	
	user = User.query.filter_by(id=session['user_id']).first()
	if user:
		img = UserImg.query.filter_by(id_user=user.id).first()
		if img:
			user.img = base64.b64encode(img.imagem).decode('ascii')

		listSol = []
		sols = Sl.query.filter_by(id_re=user.id).all()
		for sol in sols:
			usu = User.query.filter_by(id=sol.id_en).first()
			usuImg = UserImg.query.filter_by(id_user=usu.id).first()
			listSol.append({
				'user':usu,
				'img':base64.b64encode(usuImg.imagem).decode('ascii')
			})
		user.solsLen = len(listSol)
		user.sols = listSol	

	else:
		user = None
		session.clear()
		return redirect('/')
			
			
			
	if pag.upper() == 'POST':
		post = Post.query.filter_by(id=id).first()
		if post:
			if post.id_user != session['user_id']:
				return redirect('/')
		else:
			return redirect('/')
			
		imgsP = ImgPost.query.filter_by(id_post=post.id).all()
	
		if request.method.upper() == 'POST':
			body = request.form['body']
			new_img = request.files.getlist('img')
			
			if imgsP:
				for im in imgsP:
					valida = request.form['img-del-'+str(im.id)]
					if valida.lower() == 'delete':
						dele = ImgPost.query.filter_by(id=im.id).first()
						current_app.db.session.delete(dele)
						current_app.db.session.commit()
						
						
			bodyLast = Post.query.filter_by(id=id).update({'body':body})
			current_app.db.session.commit()
			
			if new_img:
				for img in new_img:
					if img:
						img1 = ImgPost(post_id=post.id,imagem=img)
						current_app.db.session.add(img1)
						current_app.db.session.commit()
						
			return redirect('/')
				
			
			
		else:
			post = Post.query.filter_by(id=id).first()
			imgTmp = ImgPost.query.filter_by(id_post=id).all()
			imgs = {}
			for img in imgTmp:
				if post.id in imgs:
					imgs[post.id].append({'id':img.id,'img':base64.b64encode(img.imagem).decode('ascii')})
				else:
					imgs[post.id] = [{'id':img.id,'img':base64.b64encode(img.imagem).decode('ascii')}]
					
			return render_template(
					'edit_post.html',
					post=post,imgs=imgs,
					pag=pag,user=user
				)
	
	
	
	
	elif pag.upper() == 'COMM':
	
		comm = Comentario.query.filter_by(id=id).first()
		if not comm or comm.id_user != session['user_id']:
			return redirect('/')
			
		if request.method.upper() == 'POST':
			body = request.form['body']
			img = request.files['img']
			
			
						
					
				
				
			imgC = ImgComm.query.filter_by(id_comm=id).first()
			
			if body or img:
				bodyLast = Comentario.query.filter_by(id=id).update({'body':body})
				current_app.db.session.commit()
				
				if img:
					comm_img = ImgComm(id_comm=id,imagem=img)
					current_app.db.session.add(comm_img)
					current_app.db.session.commit()
					
				if imgC:
					val = request.form['img-del']
					if val == 'delete' or img:
						current_app.db.session.delete(imgC)
						current_app.db.session.commit()
			
			
				return redirect('/')
			else:
				flash('Algum Campo deve ser preenchido!')
				return redirect(request.url)
			
		else:
			comm = Comentario.query.filter_by(id=id).first()
			img = ImgComm.query.filter_by(id_comm=id).first()
			imgs = {'id':img.id,'img':base64.b64encode(img.imagem).decode('ascii')} if img else False
			
			return render_template(
					'edit_post.html',
					post=comm,pag=pag,
					img=imgs,user=user,
					editar=True,
			)
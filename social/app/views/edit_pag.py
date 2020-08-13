from flask import (
	redirect, request, flash,
	render_template, session,
	current_app,
)

import base64


from app.model.post import Post
from app.model.ImgPost import ImgPost
from app.model.comentario import Comentario



def edit_pag(pag,id):
	if not 'user_id' in session:
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
						
						
			bodyLast = Post.query.filter_by(id=id).update({'body_post':body})
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
					imgs[post.id].append({'id':img.id,'img':base64.b64encode(img.imagem_dt).decode('ascii')})
				else:
					imgs[post.id] = [{'id':img.id,'img':base64.b64encode(img.imagem_dt).decode('ascii')}]
					
			return render_template('edit_post.html',post=post,imgs=imgs,pag=pag)
	
	
	
	
	elif pag.upper() == 'COMM':
	
		comm = Comentario.query.filter_by(id=id).first()
		if not comm or comm.id_user != session['user_id']:
			return redirect('/')
			
		if request.method.upper() == 'POST':
			body = request.form['body']
			if body:
				bodyLast = Comentario.query.filter_by(id=id).update({'body':body})
				db.session.commit()
				return redirect('/')
			else:
				flash('o campo não pode ficar vazio!')
				return redirect(request.url)
			
		else:
			comm = Comentario.query.filter_by(id=id).first()
			return render_template('edit_post.html',post=comm,pag=pag)
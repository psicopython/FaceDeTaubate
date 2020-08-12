from flask import (
	request, redirect, url_for,
	render_template, current_app,
	flash, session,
)

import os

from app.model.user import User
from app.model.user_img import UserImg


def cadastro():
	if 'user_id' in session:
		return redirect('/')
		
	if request.method.upper() == 'POST':
		#tel = request.form['tel']
		#data = request.form['data']
		#username = request.form['username']
		nome = request.form['nome']
		sexo = request.form['sexo']
		email = request.form['email']
		email2 = request.form['email2']
		senha = request.form['senha']
		senha2 = request.form['senha2']
		imgs = request.files.getlist('img')
		
		
		if not nome:
			flash('O campo "Nome" não pode ficar vazio!')
			return redirect(request.url)
	
		if not sexo:
			flash('O campo "Sexo" não pode ficar vazio!')
			return redirect(request.url)
		
		if not email or not email2:
			flash('O campo "Email" não pode ficar vazio!')
			return redirect(request.url)
		
		if not senha or not senha2:
			flash('O campo "Senha" não pode ficar vazio!')
			return redirect(request.url)
		
		
		
		if email != email2:
			flash(" Os emails não coincidem!")
			return redirect(request.url)
		
		if senha != senha2:
			flash(" As senhas não coincidem!")
			return redirect(request.url)
		
		
			
		if User.query.filter_by(email=email).first():
			flash(" Email não disponível!")
			return redirect(request.url)
			
		
		user = User(nome=nome,email=email,senha=senha,sexo=sexo)
		
		current_app.db.session.add(user)
		current_app.db.session.commit()
		session['user_id'] = user.id
		
		if imgs[0]:
			user_img = UserImg(imagem=imgs[0].read(),id_user=user.id)
			current_app.db.session.add(user_img)
			current_app.db.session.commit()
		
		else:
			img = None
			if sexo == 'm':
				with open('app/front/static/img/perfil/user_img_m.png','rb') as im:
					img = im.read()
			elif sexo == 'f':
				with open('app/front/static/img/perfil/user_img_f.png','rb') as im:
					img = im.read()
			else:
				with open('app/front/static/img/perfil/user_img.png','rb') as im:
					img = im.read()
			user_img=UserImg(imagem=img,id_user=user.id)
			current_app.db.session.add(user_img)
			current_app.db.session.commit()
			
		return redirect('/')
	else:
		return render_template('cadastro.html')

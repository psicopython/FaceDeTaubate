from flask import (
	request, redirect, 
	render_template, current_app,
	flash, session
)
from app.model.user import User
from app.model.user_img import UserImg


def cadastro():
	if 'user_id' in session:
		return redirect('/')
		
	if request.method.upper() == 'POST':
		#tel = request.form['tel']
		#data = request.form['data']
		nome = request.form['nome']
		email = request.form['email']
		email2 = request.form['email2']
		senha = request.form['senha']
		senha2 = request.form['senha2']
		username = request.form['username']
		imgs = request.files.getlist('img')
		
		
		if not nome:
			flash('O campo "Nome" não pode ficar vazio!')
			return redirect(request.url)
		#if not data:
		#	flash('O campo "Data De nascimento" não pode ficar vazio!')
		#	return redirect(request.url)
		if not username:
			flash('O campo "Usuário" não pode ficar vazio!')
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
		
		
			
		if User.query.filter_by(username=username).first():
			flash(" Usuário não disponível!")
			return redirect(request.url)
			
		if User.query.filter_by(email=email).first():
			flash(" Email não disponível!")
			return redirect(request.url)
			
		
		user = User(nome=nome,email=email,senha=senha,username=username)
		
		current_app.db.session.add(user)
		current_app.db.session.commit()
		session['user_id'] = user.id
		
		if imgs:
			user_img=UserImg(imagem=imgs[0],id_user=user.id)
			current_app.db.session.add(user_img)
			current_app.db.session.commit()
			print("\n\n salvou\n\n")
			
		return redirect('/')
	else:
		return render_template('cadastro.html'),200

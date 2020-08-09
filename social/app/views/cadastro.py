from flask import (
	request, redirect, 
	render_template, current_app,
	flash, session
)
from app.model.user import User


def cadastro():
	if 'user_id' in session:
		return redirect('/')
		
	if request.method.upper() == 'POST':
		tel = request.form['tel']
		nome = request.form['nome']
		#data = request.form['data']
		email = request.form['email']
		email2 = request.form['email2']
		senha = request.form['senha']
		senha2 = request.form['senha2']
		username = request.form['username']
		
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
		
		
		
		if senha != senha2:
			flash(" As senhas não coincidem!")
			return redirect(request.url)
		if email != email2:
			flash(" Os emails não coincidem!")
			return redirect(request.url)
			
			
			
		if User.query.filter_by(email=email).first():
			flash(" Email não disponível!")
			return redirect(request.url)
	
		if User.query.filter_by(username=username).first():
			flash(" Usuário não disponível!")
			return redirect(request.url)
			
		if User.query.filter_by(tel=tel).first():
			flash(" Usuário não disponível!")
			return redirect(request.url)
		
		
		
		user = User(tel=tel,nome=nome,email=email,senha=senha,username=username)
		
		current_app.db.session.add(user)
		current_app.db.session.commit()
		session['user_id'] = user.id
		return redirect('/')
	else:
		return render_template('cadastro.html'),200

from flask import (
	redirect, request,
	current_app, session,
	url_for, render_template,
	flash,
)

import base64

from werkzeug.security import generate_password_hash as gph

from app.model.user     import User
from app.model.user_img import UserImg



def editar_perfil(id,nome):
	if not 'user_id' in session:
		return redirect('/?not_credentials')
		
	if session['user_id'] != id:
		return redirect('/?not_found')
	user = User.query.filter_by(id=session['user_id']).first()
	
	if request.method.lower() == 'post':
		
		img = request.files['img']
		nome  = request.form['nome']
		sexo  = request.form['sexo']
		senha = request.form['senha']
		email1 = request.form['email1']
		email2 = request.form['email2']
		senha1 = request.form['senha1']
		senha2 = request.form['senha2']
		
		
		
		if not User.ver_pass(user,senha):
			flash('senha inválida!')
			return redirect(f'/{user.id}/{user.nome.split()[0]}/editar/')
	
		if email1:
			if email1 != email2:
				flash('Os e-mails não coincidem!')
				return redirect(f'/{user.id}/{user.nome.split()[0]}/editar/')
		
		if senha1:	
			if senha1 != senha2:
				flash('As senha não coincidem!')
				return redirect(f'/{user.id}/{userr.nome.split()[0]}/editar/')
			
			
			
			
		if nome:
			User.query.filter_by(id=user.id).update({'nome':nome})
			
			current_app.db.session.commit()
		
		
		if email1:
			conf = User.query.filter_by(email=email1).first()
			if conf:
				flash('Email Indisponível!')
				return redirect(f"/{User.id}/{user.nome.split()[0]}/editar/")
			User.query.filter_by(id=session['user_id']).update({'email':email1})
			
			current_app.db.session.commit()
		
		
		if senha1:
			User.query.filter_by(id=user.id).update({'senha':gph(senha1)})
			
			current_app.db.session.commit()
	
	
		if sexo:
			User.query.filter_by(id=user.id).update({'sexo':sexo})
			
			current_app.db.session.commit()
		
		
		if img:
			UserImg.query.filter_by(id_user=user.id).update({'imagem':img.read()})
			
			current_app.db.session.commit()
		
		
		
		
		
		return redirect(f'/{user.id}/{user.nome.split()[0]}/')
	
	
	else:
		img  = UserImg.query.filter_by(id_user=user.id).first()
		if img:
			user.img = base64.b64encode(img.imagem).decode('ascii')
		return render_template('edit_perfil.html',user=user)
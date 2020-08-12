from flask import (
	redirect, request,
	current_app, session,
	url_for, render_template,
	flash,
)

import base64

from app.model.user     import User
from app.model.user_img import UserImg



def editar_perfil(id):
	if not 'user_id' in session:
		return redirect('/')
	if session['user_id'] != id:
		return redirect('/')
	user = User.query.filter_by(id=session['user_id']).first()
	
	if request.method.lower() == 'post':
		nome  = request.form['nome']
		sexo  = request.form['sexo']
		email1 = request.form['email1']
		email2 = request.form['email2']
		senha = request.form['senha']
		senha1 = request.form['senha1']
		senha2 = request.form['senha2']
		img = request.files['img']
		
		
		
		if not User.ver_pass(user,senha):
			flash('senha inválida!')
			return redirect('/perfil/'+str(session['user_id'])+'/editar/')
	
		if email1:
			if email1 != email2:
				flash('Os e-mails não coincidem!')
				return redirect('/perfil/'+str(session['user_id'])+'/editar/')
		
		if senha1:	
			if senha1 != senha2:
				flash('As senha não coincidem!')
				return redirect('/perfil/'+str(session['user_id'])+'/editar/')
			
			
		if nome:
			User.query.filter_by(id=session['user_id']).update({'nome':nome})
			
			current_app.db.session.commit()
		
		
		if email1:
			conf = User.query.filter_by(email=email1).update({'email':email1})
			if conf:
				flash('Email Indisponível!')
				return redirect(f"/perfil/{{User.id}}/editar/")
			User.query.filter_by(id=session['user_id']).update({'email':email1})
			
			current_app.db.session.commit()
		
		
		if senha1:
			User.query.filter_by(id=session['user_id']).update({'senha':senha1})
			
			current_app.db.session.commit()
	
	
		if sexo:
			User.query.filter_by(id=session['user_id']).update({'sexo':sexo})
			
			current_app.db.session.commit()
		
		
		if img:
			UserImg.query.filter_by(id_user=session['user_id']).update({'imagem':img.read()})
			
			current_app.db.session.commit()
		
		
		
		return redirect('/perfil/'+str(session['user_id'])+'/')
	
	
	else:
		img  = UserImg.query.filter_by(id_user=user.id).first()
		if img:
			user.img = base64.b64encode(img.imagem).decode('ascii')
		return render_template('edit_perfil.html',user=user)
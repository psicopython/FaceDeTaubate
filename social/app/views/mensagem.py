from flask import (
	session, current_app,
	request, redirect,
	render_template,
)

import base64

from app.model.user import User
from app.model.chat import Chat
from app.model.chat import Msg

from app.model.user_img import UserImg



def chat(id_2,nome):
	if not 'user_id' in session:
		return redirect('/?not_user_log')
	
	user = User.query.filter_by(id=session['user_id']).first()
	if user:
		imgU = UserImg.query.filter_by(id_user=user.id).first()
		user.img = base64.b64encode(imgU.imagem).decode('ascii')
	else:
		session.pop('user_id',None)
		return redirect('/')
	
	user_rec = User.query.filter_by(id=id_2).first()
	if user_rec:
		imgU = UserImg.query.filter_by(id_user=user_rec.id).first()
		user_rec.img = base64.b64encode(imgU.imagem).decode('ascii')
	
	if user and user_rec:
		if nome != user_rec.nome.replace(' ','_'):
			return redirect('/?nome_di')
		
		if user_rec == user:
			return redirect('/?mesmo_user')
			
		if request.method == "POST":
			body = request.form['body']
			img = request.files.get('img')
			
			if body or img:
				
				conv1 = Chat.query.filter_by(id_1 =user.id,id_2=user_rec.id).first()
				conv2 = Chat.query.filter_by(id_2 =user.id,id_1=user_rec.id).first()
				if not conv1 and not conv2:
					
					conv1 = Chat(id_1=session["user_id"],id_2=user_rec.id)
					current_app.db.session.add(conv1)
					current_app.db.session.commit()
				
					conv2 = Chat(id_2=session["user_id"],id_1=user_rec.id)
					current_app.db.session.add(conv2)
					current_app.db.session.commit()
			
				if not conv1:
					conv1 = Chat(id_1=session["user_id"],id_2=user_rec.id)
					current_app.db.session.add(conv1)
					current_app.db.session.commit()
			
				if not conv2:
					conv2 = Chat(id_2=session["user_id"],id_1=user_rec.id)
					current_app.db.session.add(conv2)
					current_app.db.session.commit()
					
					
				msg1 = Msg(
					msg=body,
					imagem=img,
					id_1=user.id,
					id_conv=conv2.id,
					id_2=user_rec.id,
				)
				current_app.db.session.add(msg1)
				current_app.db.session.commit()
						
				
				msg2 = Msg(
					msg=body,
					imagem=img,
					id_1=user.id,
					id_conv=conv1.id,
					id_2=user_rec.id,
				)
				current_app.db.session.add(msg2)
				current_app.db.session.commit()
				
				
			return redirect(f'/chat/{user_rec.id}/{user_rec.nome.replace(" ","_")}/')

		else:
		
			msgs =None
			conv = Chat.query.filter_by(id_1=user.id,id_2=user_rec.id).first()
			
			
			if conv:
				msgs = Msg.query.filter_by(id_conv=conv.id).all()
				if msgs:
					for msg in msgs:
						msg.dec = msg.decrypt(msg.msg).decode('utf-8')
						msg.user = User.query.filter_by(id=msg.id_2).first()
					
						if msg.imagem:
							msg.msgImg = base64.b64encode(msg.imagem).decode('ascii')
							
			
			return render_template(
				'chat.html',msgs=msgs,
				user=user, user_rec=user_rec,
				chat=True,
			)
			
	return redirect('/?not_user_db')






def all_chat():
	if not 'user_id' in session:
		return redirect('/')
	user = User.query.filter_by(id=session['user_id']).first()
	
	convs = Chat.query.filter_by(id_1=user.id).all()
	if convs:
		for con in convs:
			con.user_env = User.query.filter_by(id=con.id_2).first()
			msg = Msg.query.filter_by(id_1=con.user_env.id).first()
			img = UserImg.query.filter_by(id_user=con.user_env.id).first()
			if img:
				con.user_env.img = base64.b64encode(img.imagem).decode('ascii')
			if not msg:
				msg = Msg.query.filter_by(id_1=con.user_env.id).order_by('id').first()
			if msg:
				con.f_msg = msg.decrypt(msg.msg).decode('utf-8')
			
	return render_template(
		'allchats.html',user=user,
		convs=convs,chat=True
	)
	
	



def del_chat(opt,id):
	
	if opt and id:
		if not 'user_id' in session:
			return redirect(request.url)
			
		if opt == 'chat':
			
			chat = Chat.query.filter_by(id=id).first()
			user = User.query.filter_by(id=session['user_id']).first()
			
			
			if chat.id_1 == user.id or chat.id_2 == user.id:
				msgs = Msg.query.filter_by(id_conv=id).all()
				if msgs:
					for msg in msgs:
						current_app.db.session.delete(msg)
						current_app.db.session.commit()
		
			if chat:
				current_app.db.session.delete(chat)
				current_app.db.session.commit()
			return redirect('/chat/')
			
			
		elif opt == 'msg':
			
			msg = Msg.query.filter_by(id=id).first()
			if msg:
				user = User.query.filter_by(id=session["user_id"]).first()
				iden = msg.id_1 if msg.id_1 != user.id else msg.id_2
				user_rec = User.query.filter_by(id=iden).first()
				if msg:
					current_app.db.session.delete(msg)
					current_app.db.session.commit()
				
				return redirect(f'/chat/{user_rec.id}/{user_rec.nome.replace(" ","_")}/')
			return redirect('/chat')
	
		
	else:
		return redirect('/chat/')


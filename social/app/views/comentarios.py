from flask import (
	current_app, session,
	redirect, request,
)

from app.model.ImgPost import ImgComm
from app.model.comentario import Comentario



def comentario(pag,id):
	if not 'user_id' in session:
		return redirect('/')
	if request.method.upper() == 'POST':
		if pag.lower() == 'post':
			body = request.form['body']
			img = request.files['img']
			
			if id and body:
				comm = Comentario(body=body,id_post=id,id_user=session['user_id'])
				current_app.db.session.add(comm)
				current_app.db.session.commit()
				
				if img:
					img = ImgComm(id_comm=comm.id,imagem=img)
					current_app.db.session.add(img)
					current_app.db.session.commit()
					print(img)
					
				return redirect('/')
			else:
				return redirect('/')
	else:
		return redirect('/')

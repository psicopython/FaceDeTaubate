from flask import (
	current_app, session,
	redirect, request,
)

from app.model.comentario import Comentario



def comentario(id):
	if not 'user_id' in session:
		return redirect('/')
	if request.method.upper() == 'POST':
		
		body = request.form['body']
		if id and body:
			comm = Comentario(body=body,id_post=id,id_user=session['user_id'])
			current_app.db.session.add(comm)
			current_app.db.session.commit()
			return redirect('/')
		else:
			return redirect('/')
	else:
		return redirect('/')

from flask import (
	redirect,request,
	url_for,
	current_app,session,
)

from app.model.reacoes import Reacoes

def like(id):
	if not 'user_id' in session:
		return redirect('/')
	reacTmp = Reacoes.query.filter_by(id_user=session['user_id'],id_post=id).first()
	if reacTmp:
		return redirect('/')
	if request.method.upper() == 'GET':
		if id:
			reac = Reacoes(id_post=id,id_user=session['user_id'])
			current_app.db.session.add(reac)
			current_app.db.session.commit()
			return redirect('/')
		else:
			return redirect('/')
	else:
		return redirect('/')




def unlike(id):
	if not 'user_id' in session:
		return redirect('/')
	reac = Reacoes.query.filter_by(id_user=session['user_id'],id_post=id).first()
	if not reac:
		return redirect('/?jalike')
	if request.method.upper() == 'GET':
		if id:
			current_app.db.session.delete(reac)
			current_app.db.session.commit()
			return redirect('/')
		else:
			return redirect('/')
	else:
		return redirect('/')
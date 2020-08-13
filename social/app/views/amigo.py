from flask import(
	current_app, session,
	request, redirect,
)

from app.model.user  import User
from app.model.amigo import Amigo
from app.model.amigo import Solicitacao as Sl



def sol(re):
	url = request.path
	user1,user2 = None,None
	if not 'user_id' in session:
		return redirect('/')
		
	if not re:
		return redirect('/')
		
	if re == session['user_id']:
		return redirect('/')
		
	user1 = User.query.filter_by(id=session['user_id']).first()
	user2 = User.query.filter_by(id=re).first()
	conf = Sl.query.filter_by(id_en=user1.id,id_re=user2.id).first()
	conf2 = Sl.query.filter_by(id_en=user2.id,id_re=user1.id).first()
	if conf:
		return redirect(f'/{re}/{user2.nome.split()[0]}/')
		
	if conf2:
		return redirect(f'/{re}/{user2.nome.split()[0]}/')
	if user1 and user2:
		soli = Sl(id_en=user1.id,id_re=user2.id)
		current_app.db.session.add(soli)
		current_app.db.session.commit()
		return redirect(f'/{re}/{user2.nome.split()[0]}/')
	else:
		return redirect(f'/{re}/{user2.nome.split()[0]}/')


def ami(re):
	user1,user2 = None,None
	if not 'user_id' in session:
		return redirect('/')
		
	if not re:
		return redirect('/')
		
	if session['user_id'] == re:
		return redirect('/')
		
	user1 = User.query.filter_by(id=session['user_id']).first()
	user2 = User.query.filter_by(id=re).first()
	if user1 and user2:
		ami1 = Amigo(id_en=user1.id,id_re=user2.id)
		current_app.db.session.add(ami1)
		current_app.db.session.commit()
		
		ami2 = Amigo(id_en=user2.id,id_re=user1.id)
		current_app.db.session.add(ami2)
		current_app.db.session.commit()
		
		soli = Sl.query.filter_by(id_re=re,id_en=session['user_id']).all()
		if soli:
			for sol in soli:
				delete(sol)
				current_app.db.session.commit()
		
		soli2 = Sl.query.filter_by(id_en=re,id_re=session['user_id']).all()
		if soli2:
			for sol in soli2:
				current_app.db.session.delete(sol)
				current_app.db.session.commit()
		
		return redirect('/')
	else:
		return redirect('/')


def des_ami(re):
	if not 'user_id' in session:
		return redirect('/')
		
	if not re:
		return redirect('/')
		
	if session['user_id'] == re:
		return redirect('/')
	
	use1 = User.query.filter_by(id=session['user_id']).first()
	use2 = User.query.filter_by(id=re).first()
	
	ami1 = Amigo.query.filter_by(
		id_user=use1.id,id_amigo=use2.id).first()
		
	ami2 = Amigo.query.filter_by(
		id_user=use2.id,id_amigo=use1.id).first()
	
	if ami1:
		current_app.db.session.delete(ami1)
		current_app.db.session.commit()
		
	if ami2:
		current_app.db.session.delete(ami2)
		current_app.db.session.commit()
	
	return redirect('/')





def can_sol(re):
	if not 'user_id' in session:
		return redirect('/')
		
	if not re:
		return redirect('/')
		
	if session['user_id'] == re:
		return redirect('/')
	
	use1 = User.query.filter_by(id=session['user_id']).first()
	use2 = User.query.filter_by(id=re).first()
	
	sol1 = Sl.query.filter_by(id_en=use1.id,id_re=use2.id).first()
	sol2 = Sl.query.filter_by(id_en=use2.id,id_re=use1.id).first()
	
	if sol1:
		current_app.db.session.delete(sol1)
		current_app.db.session.commit()
		
	if sol2:
		current_app.db.session.delete(sol2)
		current_app.db.session.commit()
	
	return redirect('/')
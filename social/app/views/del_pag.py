from flask import (
	request,redirect,
	session,current_app
)
from app.model         import db
from app.model.post    import Post
from app.model.reacoes import Reacoes
from app.model.ImgPost import ImgPost
from app.model.comentario import Comentario




def del_pag(pag,id):
	if not 'user_id' in session:
		return redirect('/')
	if request.method.upper() == 'GET':
		if pag == 'post':
			post = Post.query.filter_by(id=id).first()
			imgs = ImgPost.query.filter_by(id_post=id).all()
			comms = Comentario.query.filter_by(id_post=id).all()
			reacs  = Reacoes.query.filter_by(id_post=id).all()
			if post:
				if session['user_id'] != post.id_user:
					return redirect('/')
				if imgs:
					for img in imgs:
						current_app.db.session.delete(img)
						current_app.db.session.commit()
				if comms:
					for comm in comms:
						current_app.db.session.delete(comm)
						current_app.db.session.commit()
				if reacs:
					for reac in reacs:
						current_app.db.session.delete(reac)
						current_app.db.session.commit()
				db.session.delete(post)
				db.session.commit()
				return redirect('/')
			else:
				return redirect('/')
		
		
		
		
		elif pag == 'comm':
			comm = Comentario.query.filter_by(id=id).first()
			if comm:
				post = Post.query.filter_by(id=comm.id_post).first()
				if session['user_id'] != comm.id_user:
					return redirect('/')
				db.session.delete(comm)
				db.session.commit()
				return redirect('/')
			return redirect('/')
				
		else:
			return redirect('/')
	else:
		return redirect('/')
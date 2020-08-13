from flask import (
	request,redirect,
	session,current_app
)


from app.model.post    import Post
from app.model.user    import User
from app.model.reacoes import Reacoes
from app.model.reacoes import ReacoesComm

from app.model.ImgPost import ImgPost
from app.model.ImgPost import ImgComm

from app.model.comentario import Comentario




def del_pag(pag,id):
	if not 'user_id' in session:
		return redirect('/')
	user = User.query.filter_by(id=session['user_id']).first()
	if not user:
		return redirect('/logout/')
		
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
						if comm:
							
							if session['user_id'] != comm.id_user:
								return redirect('/?user_invalid')
								
								
							comm_img = ImgComm.query.filter_by(id_comm=comm.id).first()
							reacs = ReacoesComm.query.filter_by(id_comm=comm.id).all()
							
							if comm_img:
								current_app.db.session.delete(comm_img)
								current_app.db.session.commit()
							if reacs:
								for reac in reacs:
									current_app.db.session.delete(reac)
									current_app.db.session.commit()
									
							current_app.db.session.delete(comm)
							current_app.db.session.commit()
				
				
				if reacs:
					for reac in reacs:
						current_app.db.session.delete(reac)
						current_app.db.session.commit()
				current_app.db.session.delete(post)
				current_app.db.session.commit()
				return redirect('/')
				
			else:
				return redirect('/')
		
		
		
		
		
		elif pag == 'comm':
			comm = Comentario.query.filter_by(id=id).first()
				
			if comm:
				
				if session['user_id'] != comm.id_user:
					return redirect('/')
					
					
				comm_img = ImgComm.query.filter_by(id_comm=comm.id).first()
				reacs = ReacoesComm.query.filter_by(id_comm=comm.id,id_user=user.id).all()
				
				if comm_img:
					current_app.db.session.delete(comm_img)
					current_app.db.session.commit()
				if reacs:
					for reac in reacs:
						current_app.db.session.delete(reac)
						current_app.db.session.commit()
						
				current_app.db.session.delete(comm)
				current_app.db.session.commit()
				return redirect('/?ok')
			return redirect('/?not_com')
				
		else:
			return redirect('/?pag_err')
	else:
		return redirect('/?post')
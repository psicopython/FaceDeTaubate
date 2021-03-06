from flask import (
	redirect, request,
	render_template,
	current_app,session,
)

import base64

from app.model.user import User
from app.model.user_img import UserImg

from app.model.amigo import Amigo
from app.model.amigo import Solicitacao as Sl


from app.model.post import Post
from app.model.ImgPost import ImgPost

from app.model.reacoes import Reacoes
from app.model.reacoes import ReacoesComm

from app.model.ImgPost import ImgComm
from app.model.comentario import Comentario


def perfil(id,nome):
	
	user, userImg, user_local = None, None, None
	
	if not id:
		return redirect('/')
	
	
	
	user_local = User.query.filter_by(id=id).first()
	if not user_local:
		return redirect('/')
	else:
		if user_local.nome.replace(' ','_') != nome:
			return redirect('/')
			
		img = UserImg.query.filter_by(id_user=user_local.id).first()
		if img:
			user_local.img = base64.b64encode(img.imagem).decode('ascii')
	
		amigos = Amigo.query.filter_by(id_user=id).all()
		user_local.lenAmigos=len(amigos)
	
	if 'user_id' in session:
		user = User.query.filter_by(id=session['user_id']).first()
		img = UserImg.query.filter_by(id_user=user.id).first()
		user.img = base64.b64encode(img.imagem).decode('ascii')
		
		
		
	if user:
		listSol = []
		sols = Sl.query.filter_by(id_re=user.id).all()
		for sol in sols:
			usu = User.query.filter_by(id=sol.id_en).first()
			usuImg = UserImg.query.filter_by(id_user=usu.id).first()
			listSol.append({
				'user':usu,
				'img':base64.b64encode(usuImg.imagem).decode('ascii')
			})
		user.solsLen = len(listSol)
		user.sols = listSol	
		
		
		
		
	if user:
		ami = Amigo.query.filter_by(id_user=user.id,id_amigo=id).first()
		amigo = {}
		if ami:
			amigo['id']  = ami.id_amigo
			amigo['data'] = ami.data
		user.amigo = amigo
		
		
	if user:
		if not user.amigo:
			ami = Sl.query.filter_by(id_en=user.id,id_re=id).first()
			if ami:
				user.Sol = 'ren'
			else:
				ami2 = Sl.query.filter_by(id_en=id,id_re=user.id).first()
				if ami2:
					user.Sol = 'env'
	

	
	
	
	
	posts = Post.query.filter_by(id_user=id).all()
	for post in posts:
		
	
		listCommI={}
		imgPs = ImgPost.query.filter_by(id_post=post.id).all()
		for imgP in imgPs:
			if imgP.id_post in listCommI:
				listCommI[imgP.id_post].append(
					base64.b64encode(imgP.imagem).decode('ascii')
				)
					
			else:
				listCommI[imgP.id_post] = [
					base64.b64encode(imgP.imagem).decode('ascii')
				]
		
		post.imgs = listCommI
	
	
	
		post.user = User.query.filter_by(id=post.id_user).first()
		img = UserImg.query.filter_by(id_user=post.user.id).first()
		if img:
			post.user.img = base64.b64encode(img.imagem).decode('ascii')
		
		
		listComm=[]
		comms = Comentario.query.filter_by(id_post=post.id).all()
		if comms:
			for comm in comms:
				user_comm = User.query.filter_by(id=comm.id_user).first()
				img = UserImg.query.filter_by(id_user=user_comm.id).first()
				user_comm.img = base64.b64encode(img.imagem).decode('ascii')
				
				comm_img = ImgComm.query.filter_by(id_comm=comm.id).first()
				
				reacs = []
				liked = False
				reacao = ReacoesComm.query.filter_by(id_comm=comm.id).all()
				if reacao:
					for re in reacao:
						if user:
							if user.id == re.id_user:
								liked=True
								
						reacs.append({
							'data':re.data,
							'id_comm':re.id_comm,
							'user':User.query.filter_by(id=re.id_user).first(),
						})
					
				listComm.append({'data':comm.data,'body':comm.body,'id':comm.id,
					'id_post':comm.id_post,'user':user_comm,
					'reactLen':len(reacs),'reacs':reacs,
					'Liked':liked,
					'img':base64.b64encode(comm_img.imagem).decode('ascii') if comm_img else False
				})
				
		post.commLen = len(listComm)
		post.comm = listComm
	
	
	
	
		reacs = []
		liked = False
		reacao = Reacoes.query.filter_by(id_post=post.id).all()
		for re in reacao:
			if user:
				if user.id == re.id_user:
					liked = True
			if re:
				reacs.append({
					'data':re.data,
					'id_post':re.id_post,
					'user':User.query.filter_by(id=re.id_user).first(),
				})
		
		post.reactLen = len(reacs)
		post.reacs = reacs
		post.Liked = liked
		
	posts.reverse()
	
	return render_template(
		'perfil.html',user=user,posts=posts,
		user_local=user_local,
	)
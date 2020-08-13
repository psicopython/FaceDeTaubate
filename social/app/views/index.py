from flask import render_template, session

import base64


from app.model.user import User
from app.model.user_img import UserImg

from app.model.post import Post
from app.model.ImgPost import ImgPost

from app.model.reacoes import Reacoes
from app.model.reacoes import ReacoesComm

from app.model.ImgPost import ImgComm
from app.model.comentario import Comentario

from app.model.amigo import Amigo
from app.model.amigo import Solicitacao as Sl


def index():
	
	user, posts = None, None
	
	if 'user_id' in session:
		user = User.query.filter_by(id=session['user_id']).first()
		if user:
			img = UserImg.query.filter_by(id_user=user.id).first()
			if img:
				user.img = base64.b64encode(img.imagem).decode('ascii')
		else:
			user = None
			session.clear()
	else:
		return render_template('login.html')
		
		
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
	
	
		



	posts = Post.query.all()
	for post in posts:
		
		if user:
			listAmigo = {}
			ami = Amigo.query.filter_by(id_user=user.id,id_amigo=post.id_user).first()
			if ami:
				listAmigo['id_ami'] = ami.id_amigo
				listAmigo['data'] = ami.data
			
				post.amigo	= listAmigo
			
			
			
		if user:
			listSolAmigo = {}
			ami = Sl.query.filter_by(id_en=user.id,id_re=post.id_user).first()
			if ami:
				listSolAmigo['id_ami'] = ami.id_re
			
				post.jasol	= listSolAmigo
	
		
			
		
	
		listCommI={}
		imgPs = ImgPost.query.filter_by(id_post=post.id).all()
		for imgP in imgPs:
			if imgP.id_post in listCommI:
				listCommI[imgP.id_post].append(base64.b64encode(imgP.imagem).decode('ascii'))
			else:
				listCommI[imgP.id_post] = [base64.b64encode(imgP.imagem).decode('ascii')]
		
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
				user_comm_img = UserImg.query.filter_by(id_user=user_comm.id).first()
				comm.img = base64.b64encode(user_comm_img.imagem).decode('ascii')
				
				
				comm_img = ImgComm.query.filter_by(id_comm=comm.id).first()
				
				reacs = []
				liked = False
				reacao = ReacoesComm.query.filter_by(id_comm=comm.id).all()
				for re in reacao:
					usu_reac = User.query.filter_by(id=re.id_user).first()
					if user:
						if user.id == re.id_user:
							liked = True
							
					reacs.append({
						'data':re.data,
						'id_comm':re.id_comm,
						'usu':usu_reac,
					})
				
				
				listComm.append({
					'data':comm.data,'body':comm.body,'id':comm.id,
					'id_post':comm.id_post,'user':user_comm,
					'reactLen':len(reacs),'reacs':reacs,'Liked':liked,
					'img': base64.b64encode(comm_img.imagem).decode('ascii') if comm_img else False,
				})
				
				
		post.commLen = len(listComm)
		post.comm = listComm
	
	
	
	
	
	
		reacs = []
		reacao = Reacoes.query.filter_by(id_post=post.id).all()
		for re in reacao:
			reacs.append({
				'data':re.data,
				'id_post':re.id_post,
				'user':User.query.filter_by(id=re.id_user).first(),
			})
			if user:
				if user.id == re.id_user:
					post.Liked = True
		
		post.reactLen = len(reacs)
		post.reacs = reacs
		
	posts.reverse()


	
	return render_template(
		'index.html',user=user,
		posts=posts,
	)
	
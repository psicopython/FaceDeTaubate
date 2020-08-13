from . import db, ma

from datetime import datetime



class ImgPost(db.Model):
	
	__tablename__='imgPost'
	
	id = db.Column(db.Integer,primary_key=True)
	data = db.Column(db.DateTime,nullable=False)
	imagem = db.Column(db.BLOB,nullable=False)
	id_post = db.Column(db.Integer,nullable=False)
	
	
	
	def __init__(self,post_id,imagem):
		
		self.data = datetime.now()
		self.imagem = imagem.read()
		self.id_post = post_id
		
		
	def __repr__(self):
		return f"<Imagem: post n° {self.id}>"



class ImgComm(db.Model):
	
	__tablename__='imgComm'
	
	id = db.Column(db.Integer,primary_key=True)
	data = db.Column(db.DateTime,nullable=False)
	imagem = db.Column(db.BLOB,nullable=False)
	id_comm = db.Column(db.Integer,nullable=False)
	
	
	
	def __init__(self,id_comm,imagem):
		
		self.data = datetime.now()
		self.imagem = imagem.read()
		self.id_comm = id_comm
		
		
	def __repr__(self):
		return f"<Imagem: comentário n° {self.id}>"
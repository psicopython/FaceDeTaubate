from . import db
from datetime import datetime

class UserImg(db.Model):
	
	__tablename__="user_img"
	
	id = db.Column(db.Integer,primary_key=True)
	data = db.Column(db.DateTime,nullable=False)
	imagem = db.Column(db.BLOB,nullable=False)
	id_user = db.Column(db.Integer,nullable=False)
	
	def __init__(self,imagem,id_user):
		
		self.data = self._get_data()
		self.imagem = imagem
		self.id_user = id_user
	
	def _get_data(self):
		return datetime.now()
	
	def __repr__(self):
		return f"Perfil:{self.id} user:{self.id_user}"
from . import db
from datetime import datetime

class UserImg(db.Model):
	
	__tablename__="user_img"
	
	id = db.Column(db.Integer,primary_key=True)
	imagem = db.Column(db.BLOB,nullable=False)
	id_user = db.Column(db.Integer,nullable=False)
	data_upl = db.Column(db.DateTime,nullable=False)
	
	def __init__(self,imagem,id_user):
		self.imagem = imagem
		self.id_user = id_user
		self.data_upl = self._get_data()
	
	def _get_data(self):
		return datetime.now()
	
	def __repr__(self):
		return f"Perfil:{self.id} user:{self.id_user}"

from . import db

from datetime import datetime


class Amigo(db.Model):
	
	__tablename__='amigo'
	
	id = db.Column(db.Integer, primary_key=True)
	id_user = db.Column(db.Integer,nullable=False)
	id_amigo = db.Column(db.Integer,nullable=False)
	data = db.Column(db.DateTime,nullable=False)
	
	def __init__(self,id_en,id_re):
		self.data     = self._get_data()
		self.id_user  = id_en
		self.id_amigo = id_re
	
	def _get_data(self):
		return datetime.now()
	


class Solicitacao(db.Model):
	
	__tablename__='solicitacao'

	id = db.Column(db.Integer, primary_key=True)
	id_en = db.Column(db.Integer, nullable=False)
	id_re = db.Column(db.Integer, nullable=False)
	
	
	def __init__(self,id_en,id_re):
		
		self.id_en = id_en
		self.id_re = id_re
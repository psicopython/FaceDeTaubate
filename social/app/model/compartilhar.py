
from . import db,ma

from datetime import datetime




class Compartilhar(db.Model):
	
	__tablename__='compartilhar'
	
	id  = db.Column(db.Integer,primary_key=True)
	data = db.Column(db.DateTime,nullable=False)
	id_user = db.Column(db.Integer,nullable=False)
	id_post = db.Column(db.Integer,nullable=False)
	
	
	def _get_data(self):
		return datetime.now()
	
	def __init__(self, id_post, id_user ):
		self.data    = self._get_data()
		self.id_post = id_post
		self.id_user = id_user
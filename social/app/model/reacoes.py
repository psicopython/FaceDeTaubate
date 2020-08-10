from app.model import db,ma

from datetime import datetime


class Reacoes(db.Model):
	
	__tablename__='reacoes'
	
	id = db.Column(db.Integer,primary_key=True)
	data = db.Column(db.DateTime,nullable=False)
	id_user = db.Column(db.Integer,nullable=False)
	id_post = db.Column(db.Integer,nullable=False)
	
	
	def __init__(self,id_post,id_user):
		self.id_user = id_user
		self.id_post = id_post
		self.data = datetime.today()
	
	def __repr__(self):
		return f"Reações:{self.id} Post:{self.id_post}"
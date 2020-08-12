from app.model import db, ma

from datetime import datetime



class Comentario(db.Model):
	
	__tablename__ = 'comentario'
	
	id   = db.Column(db.Integer, primary_key=True)
	data = db.Column(db.DateTime,nullable=False)
	body = db.Column(db.Text,nullable=False)
	id_post = db.Column(db.Integer,nullable=False)
	id_user = db.Column(db.Integer,nullable=False)
	
	def _get_data(self):
		return datetime.today()
	
	def __init__(self, body, id_post,id_user):
		
		self.data = self._get_data()
		self.body = body
		self.id_post = id_post
		self.id_user = id_user
	
	
	
	
	def __repr__(self):
		return f"Comentário:{self.id}, Post:{self.id_post}"


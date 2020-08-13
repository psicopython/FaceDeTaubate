from . import db, ma

import datetime




class Post(db.Model):
	
	__tablename__='post'
	
	id = db.Column(db.Integer,primary_key=True)
	data = db.Column(db.DateTime,nullable=False)
	body= db.Column(db.String())
	id_user = db.Column(db.Integer,nullable=False)
	
	
	def __get_data(self):
		return datetime.datetime.now()
	
	
	def __init__(self,user_id,body):
		self.body = body
		self.data = self.__get_data()
		self.id_user = user_id
		
		
	def __repr__(self):
		return f"< Post {self.id}>"
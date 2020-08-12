from . import db, ma

from datetime import datetime

from werkzeug.security import generate_password_hash as gph
from werkzeug.security import check_password_hash as cph



class User(db.Model):
	
	__tablename__="user"
	
	id = db.Column(db.Integer,primary_key=True)
	nome = db.Column(db.String(128),nullable=False)
	sexo = db.Column(db.CHAR,nullable=False)
	email = db.Column(db.String(128),unique=True,nullable=False)
	senha  = db.Column(db.String(512),nullable=False)
	data_cr = db.Column(db.DateTime,nullable=False)
	
	
	
	def __init__(self,nome, email,senha,sexo):
	
		self.nome = nome
		self.sexo = sexo
		self.email = email
		self.senha  = gph(senha)
		self.data_cr = datetime.now()
	
	
	def __repr__(self):
		return f"<Usuário {self.nome} | id:{self.id}>"
	
	
	def ver_pass(self,senha):
		return cph(self.senha,senha)
		


class UserSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = User
		include_fk = True



userSchema = UserSchema()
users_Schema = UserSchema(many=True)
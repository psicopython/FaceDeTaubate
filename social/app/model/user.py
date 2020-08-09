from . import db, ma

from datetime import datetime
from werkzeug.security import generate_password_hash as gph
from werkzeug.security import check_password_hash as cph



class User(db.Model):
	
	__tablename__="user"
	
	id = db.Column(db.Integer,primary_key=True)
	tel = db.Column(db.String(20),unique=True,nullable=False)
	nome = db.Column(db.String(128),nullable=False)
	email = db.Column(db.String(128),unique=True,nullable=False)
	senha  = db.Column(db.String(512),nullable=False)
	data_cr = db.Column(db.DateTime,default=datetime.utcnow(),nullable=False)
	data_nas = db.Column(db.DateTime,nullable=False)
	username  = db.Column(db.String, unique=True,nullable=False)
	
	def __init__(self,tel,nome, email,senha,username):
		self.tel = tel
		self.nome = nome
		self.email = email
		self.senha  = gph(senha)
		self.data_nas = datetime.utcnow()
		self.username  = username
	
	def ver_pass(self,senha):
		return cph(self.senha,senha)
		


class UserSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = User
		include_fk = True



userSchema = UserSchema()
users_Schema = UserSchema(many=True)
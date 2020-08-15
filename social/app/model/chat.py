from app.model import db


from cryptography.fernet import Fernet


# deve ficar em arquivo separado
# e não deve ser uppado no git,
# mas sem essa chave, vcs não poderam desencriptar 
# a mensagem, então pode
key = b'64LbH1YTE_H6WZTO21m0yi1x_CzD6ChO9ohBxx-yqUU='


from datetime import datetime



class Chat(db.Model):
	
	__tablename__= "conversa"
	
	id = db.Column(db.Integer,primary_key=True)
	id_1 = db.Column(db.Integer)
	id_2 = db.Column(db.Integer)
	
	
	def __init__(self,id_1, id_2):
	
		self.id_1 = id_1
		self.id_2 = id_2
	
	def __repr__(self):
		return f"< Conv. ID:{self.id}>"



class Msg(db.Model):
	
	__tablename__= "mensagem"
	
	id = db.Column(db.Integer,primary_key=True)
	id_1 = db.Column(db.Integer)
	id_2 = db.Column(db.Integer)
	msg = db.Column(db.Unicode(512))
	data = db.Column(db.DateTime,nullable=False)
	id_conv = db.Column(db.Integer,nullable=False)
	imagem = db.Column(db.BLOB)
	
	def _get_data(self):
		return datetime.now()
		
		
	def encrypt(self,msg):
		encry = Fernet(key)
		atum = encry.encrypt(bytes(msg,'utf-8'))
		return atum
		
	def decrypt(self,msg):
		decry = Fernet(key)
		return decry.decrypt(msg)
		
	
	def __init__(self, msg, imagem, id_1, id_2, id_conv):
		self.id_1 = id_1
		self.id_2 = id_2
		self.id_conv = id_conv
		self.imagem = imagem.read()
		self.data = self._get_data()
		self.msg = self.encrypt(msg)
	
	def __repr__(self):
		return f"< Msg. ID:{self.id} || conv:{self.id_conv}>"



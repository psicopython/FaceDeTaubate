from . import db
from . import ma

from datetime import datetime




class Post(db.Model):
	
	__tablename__='post'
	
	id = db.Column(db.Integer,primary_key=True)
	id_user = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
	data_cr = db.Column(db.DateTime,default=datetime.utcnow(),nullable=False)
	body_post = db.Column(db.String(),nullable=False)
	user = db.relationship('User')
	
	
	def __init__(self,id_user,body_post):
		self.id_user = id_user
		self.body_post = body_post



class PostSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = Post
		include_fk = True



postSchema = PostSchema()
posts_Schema = PostSchema(many=True)
from . import db, ma

from datetime import datetime




class Post(db.Model):
	
	__tablename__='post'
	
	id = db.Column(db.Integer,primary_key=True)
	id_user = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
	data_cr = db.Column(db.DateTime,default=datetime.utcnow(),nullable=False)
	body_post = db.Column(db.String(),nullable=False)
	user = db.relationship('User')
	
	
	def __init__(self,user_id,body):
		self.id_user = user_id
		self.body_post = body
		
		
	def __repr__(self):
		return f"< Post {self.id}>"


class PostSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = Post
		include_fk = True



postSchema = PostSchema()
posts_Schema = PostSchema(many=True)
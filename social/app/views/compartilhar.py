

from flask import (
	redirect, request,
	session, current_app,
)


from app.model.user import User
from app.model.post import Post



def shared(id):
	
	if not 'user_id' in session:
		return redirect('/')
	
	
	user = User.query.filter_by(id=session['user_id']).first()
	post = Post.query.filter_by(id=id).first()
	if user:
		comp = Post(id_post=post.id,id_user=user.id)
		current_app.db.session.add(comp)
		current_app.db.session.commit()
		
		post = Post(id_post=id,id_user=user.id,body_post=0, compartilhado=comp.id)
		current_app.db.session.add(post)
		current_app.db.session.commit()
		
		
		return redirect('/')
		
		
	else:
		return redirect('/')
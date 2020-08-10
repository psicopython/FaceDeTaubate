from flask import (
	request,redirect,
	session,
)
from app.model         import db
from app.model.post    import Post
from app.model.ImgPost import ImgPost

def del_post(id):
	if not 'user_id' in session:
		return redirect('/')
	if request.method.upper() == 'GET':
		post = Post.query.filter_by(id=id).first()
		imgs = ImgPost.query.filter_by(id_post=id).all()
		if post:
			if session['user_id'] != post.id_user:
				return redirect('/')
			if imgs:
				for img in imgs:
					db.session.delete(img)
					db.session.commit()
			db.session.delete(post)
			db.session.commit()
			return redirect('/')
		else:
			return redirect('/')
	else:
		return redirect('/')
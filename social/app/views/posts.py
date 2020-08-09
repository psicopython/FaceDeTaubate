from flask import (
	request,render_template,
	redirect,url_for,
	current_app,session,
	flash,
)

from app.model.user    import User
from app.model.ImgPost import ImgPost
from app.model.post    import Post



def post():
	user = None
	if not 'user_id' in session:
		return redirect(url_for('webui.login'))
	else:
		user = User.query.filter_by(id=session['user_id']).first()
	if request.method.upper() == 'POST':
		if not request.files:
			...
		body = request.form['body']
		imgs = request.files.getlist('img')
		img_list = []
		for img in imgs:
			img_list.append(img)
		
		if img_list and body:
			post = Post(user_id=session['user_id'],body=body)
			current_app.db.session.add(post)
			current_app.db.session.commit()
			for img in img_list:
				imgPost = ImgPost(post_id=post.id,imagem=img)
				current_app.db.session.add(imgPost)
				current_app.db.session.commit()
				
			flash('post criado com sucesso!')
			return redirect(request.url)
		else:
			flash('Todos os campos devem ser preenchidos! ')
			return redirect(request.url)
		
		
	else:
		return render_template('post.html',user=user)






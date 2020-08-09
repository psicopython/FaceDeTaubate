from flask import (
	request,render_template,
	redirect,url_for,
	current_app,session,
	)

def post():
	if not 'user_id' in session:
		return redirect(url_for('webui.login'))
	if request.method.upper() == 'POST':
		if not request.files:
			...
		body = request.form['body']
		imgs = request.files.getlist()
		
	else:
		return render_template('post.html')
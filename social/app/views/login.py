from flask import(
	 request, redirect,
	 flash, render_template,
	 session
)
from app.model.user import User



def login():
	if 'user_id' in session:
		return redirect('/')
	if request.method == 'POST':
			
		email = request.form['email']
		senha = request.form['senha']
		if not email:
			flash('O campo email não pode ficar vazio!')
			return redirect(request.url)
		if not senha:
			flash('O campo senha não pode ficar vazio!')
			return redirect(request.url)
		
		user = User.query.filter_by(email=email).first()
		
		if user:
			if User.ver_pass(user,senha):
				session["user_id"] = user.id
				return redirect('/')
			else:
				flash(' Usuário ou senha Inválidos!')
				return redirect(request.url)
		else:
			flash(' Usuário ou senha Inválidos!')
			return redirect(request.url)
	else:
		return render_template('login.html')
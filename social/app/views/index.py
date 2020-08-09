from flask import render_template, session
from app.model.user import User


def index():
	user = None
	if 'user_id' in session:
		user = User.query.filter_by(id=session['user_id']).first()
	return render_template('index.html',user=user)
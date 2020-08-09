from flask import session, redirect


def logout():
	if 'user_id' in session:
		session.pop('user_id',None)
		return redirect('/')
	else:
		return redirect('/')
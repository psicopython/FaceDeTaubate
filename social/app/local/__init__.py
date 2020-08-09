from flask import app


def config_lc(app):
	app.config["SECRET_KEY"] = 'hsgayhsg688'
	app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
	#app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://user:pass@db/table'
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.template_folder = './app/front/templates/'
	app.static_folder   = './app/front/static/'

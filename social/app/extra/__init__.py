from flask_cors import CORS


def config_ex(app):
	CORS(app,resource={r'/api/*':{'origins':'*'}})
from flask import Blueprint
import os

from .index    import index
from .cadastro import cadastro
from .login    import login
from .logout    import logout


bp = Blueprint('webui',__name__.split()[0])



bp.add_url_rule('/',methods=["GET"],view_func=index,endpoint='index')
bp.add_url_rule('/login/',methods=["GET","POST"],view_func=login,endpoint='login')
bp.add_url_rule('/cadastro/',methods=["GET","POST"],view_func=cadastro,endpoint='cadastro')
bp.add_url_rule('/logout/',methods=["GET"],view_func=logout,endpoint='logout')

def config_vw(app):
	app.register_blueprint(bp)
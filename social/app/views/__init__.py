from flask import Blueprint


from .index    import index

from .posts      import post
from .del_post   import del_post
from .edit_post  import edit_post

from .cadastro import cadastro
from .login    import login
from .logout   import logout



bp = Blueprint('webui',__name__.split()[0])


bp.add_url_rule('/',methods=["GET"],view_func=index,endpoint='index')


bp.add_url_rule('/login/',methods=["GET","POST"],view_func=login,endpoint='login')
bp.add_url_rule('/cadastro/',methods=["GET","POST"],view_func=cadastro,endpoint='cadastro')
bp.add_url_rule('/logout/',methods=["GET"],view_func=logout,endpoint='logout')


bp.add_url_rule('/post/',              methods=["GET","POST"],
		view_func=post,endpoint='post')
		
bp.add_url_rule('/excluir/<int:id>/',  methods=["GET","POST"],
		view_func=del_post,endpoint='del_post')
		
bp.add_url_rule('/editar/<int:id>/',   methods=["GET","POST"],
		view_func=edit_post,endpoint='edit_post')
	
	
def config_vw(app):
	app.register_blueprint(bp)
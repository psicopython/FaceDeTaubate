from flask import Blueprint


from .index    import index

from .posts       import post
from .reacao      import like, unlike
from .comentarios import comentario

from .perfil import perfil
from .edit_perfil import editar_perfil
from .amigo  import sol,ami,des_ami,can_sol

from .del_pag    import del_pag
from .edit_pag  import edit_pag

from .cadastro import cadastro
from .login    import login
from .logout   import logout



bp = Blueprint('webui',__name__.split()[0])


bp.add_url_rule('/',methods=["GET"],view_func=index,endpoint='index')

bp.add_url_rule('/perfil/<int:id>/',methods=["GET"],
	view_func=perfil,endpoint='perfil')

bp.add_url_rule('/perfil/<int:id>/editar/',methods=["GET","POST"],
	view_func=editar_perfil,endpoint='editar_perfil')




bp.add_url_rule('/amizade/solicitar/<int:re>/',
	methods=["GET"],view_func=sol,endpoint='env_sol')

bp.add_url_rule('/amizade/cancelar_solicitacao/<int:re>/',
	methods=["GET"],view_func=can_sol,endpoint='can_sol')

bp.add_url_rule('/amizade/responder/<int:re>/',methods=["GET"],
	view_func=ami,endpoint='resp_sol')

bp.add_url_rule('/amizade/desfazer/<int:re>/',methods=["GET"],
	view_func=des_ami,endpoint='des_ami')




bp.add_url_rule('/login/',methods=["GET","POST"],view_func=login,endpoint='login')
bp.add_url_rule('/cadastro/',methods=["GET","POST"],view_func=cadastro,endpoint='cadastro')
bp.add_url_rule('/logout/',methods=["GET"],view_func=logout,endpoint='logout')




bp.add_url_rule('/post/', methods=["GET","POST"],
	view_func=post,endpoint='post')
	
bp.add_url_rule('/post/comentario/<string:pag>/<int:id>/', methods=["GET","POST"],
	view_func=comentario,endpoint='comentario')




bp.add_url_rule('/post/like/<int:id>/', methods=["GET"],
	view_func=like,endpoint='reacao')
	
bp.add_url_rule('/post/unlike/<int:id>/', methods=["GET"],
	view_func=unlike,endpoint='unlike')



bp.add_url_rule('/excluir/<string:pag>/<int:id>/',  methods=["GET","POST"],
	view_func=del_pag,endpoint='del_pag')
		
bp.add_url_rule('/editar/<string:pag>/<int:id>/',   methods=["GET","POST"],
	view_func=edit_pag,endpoint='edit_pag')



	
def config_vw(app):
	app.register_blueprint(bp)
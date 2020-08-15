from flask import Blueprint


from .index    import index

from .posts       import post
from .reacao      import like, unlike

from .reacao      import likeComm, unlikeComm
from .comentarios import comentario


from .perfil      import perfil
from .edit_perfil import editar_perfil

from .amigo       import sol,ami,des_ami,can_sol

from .del_pag    import del_pag
from .edit_pag  import edit_pag

from .mensagem import chat
from .mensagem import del_chat
from .mensagem import all_chat

from .login    import login
from .logout   import logout
from .cadastro import cadastro



bp = Blueprint('webui',__name__.split()[0])

# home
bp.add_url_rule('/',methods=["GET"],view_func=index,endpoint='index')

# perfil dos usuários
bp.add_url_rule('/<int:id>/<string:nome>/',methods=["GET"],
	view_func=perfil,endpoint='perfil')

# editar o perfil
bp.add_url_rule('/<int:id>/<string:nome>/editar/',methods=["GET","POST"],
	view_func=editar_perfil,endpoint='editar_perfil')



# mandar solicitação
bp.add_url_rule('/amizade/solicitar/<int:re>/',
	methods=["GET"],view_func=sol,endpoint='env_sol')

# cancelar solicitação enviada
bp.add_url_rule('/amizade/cancelar_solicitacao/<int:re>/',
	methods=["GET"],view_func=can_sol,endpoint='can_sol')

# aceitar solicitação
bp.add_url_rule('/amizade/responder/<int:re>/',methods=["GET"],
	view_func=ami,endpoint='resp_sol')

# desfazer amizade
bp.add_url_rule('/amizade/desfazer/<int:re>/',methods=["GET"],
	view_func=des_ami,endpoint='des_ami')



# login
bp.add_url_rule('/login/',methods=["GET","POST"],view_func=login,endpoint='login')

# cadastro
bp.add_url_rule('/cadastro/',methods=["GET","POST"],view_func=cadastro,endpoint='cadastro')

# logout
bp.add_url_rule('/logout/',methods=["GET"],view_func=logout,endpoint='logout')



# criar post

bp.add_url_rule('/post/', methods=["POST"],
	view_func=post,endpoint='post'
)



# comentarios

bp.add_url_rule('/comentario/<string:pag>/<int:id>/',
	methods=["POST"], view_func=comentario, endpoint='comentario'
)



# like nas publicações

bp.add_url_rule('/post/like/<int:id>/', methods=["GET"],
	view_func=like,endpoint='like_post'
)
	
# deslike nas publicações

bp.add_url_rule('/post/unlike/<int:id>/', methods=["GET"],
	view_func=unlike,endpoint='unlike_post'
)




# like nos comentários

bp.add_url_rule('/comentario/like/<int:id>/', methods=["GET"],
	view_func=likeComm,endpoint='like_comm'
)
	
# deslike nos comentários

bp.add_url_rule('/comentario/unlike/<int:id>/', methods=["GET"],
	view_func=unlikeComm,endpoint='unlike_comm'
)




bp.add_url_rule('/excluir/<string:pag>/<int:id>/',  methods=["GET","POST"],
	view_func=del_pag,endpoint='del_pag'
)
		
bp.add_url_rule('/editar/<string:pag>/<int:id>/',   methods=["GET","POST"],
	view_func=edit_pag,endpoint='edit_pag'
)



bp.add_url_rule('/chat/<int:id_2>/<string:nome>/',methods=["GET","POST"],
	view_func=chat, endpoint='chat'
)

bp.add_url_rule('/chat/excluir/<string:opt>/<int:id>/',methods=["GET","POST"],
	view_func=del_chat, endpoint='del_chat'
)

bp.add_url_rule('/chat/',methods=["GET"],
	view_func=all_chat, endpoint='all_chat'
)

	
	
	
def config_vw(app):
	app.register_blueprint(bp)
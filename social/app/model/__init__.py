from flask_sqlalchemy  import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate     import Migrate


db = SQLAlchemy()
ma = Marshmallow()
mi = Migrate()




def config_db(app):
	db.init_app(app)
	app.db = db
	ma.init_app(app)
	app.ma = ma
	mi.init_app(app,app.db)


from . import user
from . import user_img

from . import amigo

from . import post
from . import ImgPost

from . import reacoes
from . import comentario


from . import chat
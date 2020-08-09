from app.local import config_lc
from app.extra import config_ex
from app.model import config_db
from app.views import config_vw
#from app.auth  import config_at

def config(app):
	config_lc(app)
	config_ex(app)
	config_db(app)
	config_vw(app)
	#config_at(app)
from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'!_Uv\x9f^\x82\xde\xbf\xe4\xbc\xa7\xac\xa2\xbe\xa5'

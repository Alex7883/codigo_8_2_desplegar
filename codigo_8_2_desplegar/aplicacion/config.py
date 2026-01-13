import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True # En despliegue esto pasa a FALSE
#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Ejemplo basico de postgresql
# Comparalo con ejemplo de Mysql
#SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://root:password@localhost/base_datos'
#SQLALCHEMY_TRACK_MODIFICATIONS=False

SQLALCHEMY_DATABASE_URI= 'postgresql+psycpg2://dbweb_i4hz_user:6Gd8ccgO7tPVypD2LPKyOa3DtnN3kYr2@dpg-d5flshh5pdvs73fdkmf0-a.frankfurt-postgres.render.com/dbweb_i4hz'
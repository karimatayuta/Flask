from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

username = 'root'
password = 'password'
host     = 'localhost'
dbname   = 'MemBar'

engine   = create_engine(
    'mysql+pymysql://{username}:{password}@{host}/{dbname}?charset=utf8'\
    .format(username=username, password=password, host=host, dbname=dbname)
)

Session = sessionmaker(bind=engine)
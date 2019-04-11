from sqlalchemy import Column, Integer, String, MetaData, TEXT
from sqlalchemy.ext.declarative import declarative_base
# from : ファイル名 import : 値
from session import engine,Session

Base = declarative_base()

class sample_model(Base):
    __tablename__ = 'sample_model' # テーブル名

    id = Column(Integer, primary_key=True) # カラム設定

class post(Base):
    __tablename__ = 'post'

    id      = Column(Integer, primary_key=True, autoincrement=True)
    title   = Column(TEXT)
    opinion = Column(TEXT)

if __name__ == '__main__':
    Base.metadata.create_all(engine)

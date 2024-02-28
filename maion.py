import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Uuid, String, DateTime, func, DECIMAL,Integer, BOOLEAN,ForeignKey



motor = create_engine('sqlite+pysqlite:///banco_de_dados.sqlite',
                      echo=True)


class Base(DeclarativeBase):
    pass

class DataMixin():
    dta_cadastro = Column(DateTime,server_default=func.now(),  nullable=False)

    dtaatualizacao = Column(DateTime, onupdate=func.now(), default=func.now(),nullable=False)

class Categoria(Base, DataMixin):
    __tablename__ = 'tbl_categorias'
    id =Column(Uuid(as_uuid=True),primary_key=True, default=uuid.uuid4)
    nome =Column(String(256), nullable=False)

    lista_de_produtos = relationship("Produto", back_populates="categoria",
                                 cascade="all, delete-orphan", lazy="selectin")

class Produtos(Base, DataMixin):
        __tablename__ = 'tb_produtos'
        id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
        nome = Column(String(256), nullable=False)
        preco = Column(DECIMAL( 10, 2), default=0.00)
        estoque =Column (Integer, default=0)
        ativo =Column(BOOLEAN,default=True)
        categoria_id =Column(Uuid(as_uuid=True), ForeignKey('tbl_categorias.id'))

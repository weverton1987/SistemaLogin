from Models import Pessoas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import hashlib

def retorna_session():
    conexao = 'sqlite:///projeto2.db'
    engine = create_engine(conexao, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

class ControllerCadastro:
    @classmethod
    def verificar_dados(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 3:
            return 2
        if len(email) > 200:
            return 3
        if len(senha) > 100 or len(senha) < 6:
            return 4
        return 1
    
    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = retorna_session()
        usuario = session.query(Pessoas).filter(Pessoas.email == email).all()
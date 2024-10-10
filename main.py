#Banco de Dados
# #SQLite
# S Q L
#Linguagem de Consulta Estruturada

#SELECT * FROM CLIENTES
#nome, sobrenome, idade
import os
os.system("cls || clear")
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com o banco de dados
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha


# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

# Salvar no banco de dados
print("Solicitando dados para o usuário")
inserir_nome = input("Digite seu nome: ")
inserir_email = input("Digite seu email: ")
inserir_senha = input("Digite sua senha: ")

usuario = Usuario(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(usuario)
session.commit()

# Listando todos os usuários do banco de dados.
print("\nExibindo todos os usuários do banco de dados.")
lista_usuarios = session.query(Usuario).all()

# READ
for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

# DELETE
print("\nExcluindo um usuário.")
email_usuario = input("Informe o e-mail do usuário para ser excluído: ")

# Buscando o usuário pelo e-mail
usuario = session.query(Usuario).filter_by(email=email_usuario).first()

if usuario:
    session.delete(usuario)
    session.commit()
    print("Usuário excluído com sucesso.")
else:
    print("Nenhum usuário encontrado com o e-mail fornecido.")

# Listando novamente todos os usuários para verificar a exclusão
print("\nExibindo todos os usuários do banco de dados.")
lista_usuarios = session.query(Usuario).all()

# READ
for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

print("\nAtualizando dados do usuário.")
usuario = session.query(Usuario).filter_by(email email_usuario).first()

novos_dados = Usuario(
    nome = input("Digite seu nome: "),
    email = input("Digite seu e-mail: "),
    senha = input("Digite seu senha: ")
)

usuario = novos_dados
session.add(usuario)
session.commit()

# Fecha a sessão/conexão
session.close()

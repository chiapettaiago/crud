import services.database as db

def incluir(cliente):
    count = db.cursor.execute("""
INSERT INTO cliente (cliNome, cliIdade, cliProfissao) 
VALUES (?,?,?)""",
cliente.nome, cliente.idade, cliente.profissao).rowcount
db.cnxn.commit()

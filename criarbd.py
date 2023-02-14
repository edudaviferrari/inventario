#importando sqlite
import sqlite3 as lite

#Criando Conexão com Banco de Dados
con= lite.connect('dados.db')

#Criando Tabela
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT,local TEXT, descricao TEXT, marca TEXT, data_da_compra DATE,valor_da_compra DECIMAL, serie TEXT, imagem TEXT)")
import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=TOSIN\SQLEXPRESS;"
    "Database=PyhonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()

id = int(input('Qual o id?'))
nome = input('Qual o nome?')
preco = int(input('Qual o preço?'))



comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{nome}', 'PC', '', {preco}, 1)"""

cursor.execute(comando)
cursor.commit()
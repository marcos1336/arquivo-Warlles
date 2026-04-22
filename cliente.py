arquivo = open("cliente.txt", "w",)
clientes = [
    " ------------------------------------------------------",
    " | TABELA CLIENTE:                                     |",
    " |ID:/    NOME: /     CPF: /     TELEFONE: / CIDADE:   |",      
    " |1,Joao Silva,123.456.789-00,86999990001,Teresina/    |",
    " |2,Maria Souza,987.654.321-00,86999990002,Timon/      |",
    " |3,Carlos Lima,111.222.333-44,86999990003,Parnaiba/   |",
    " |4,Ana Paula,555.666.777-88,86999990004,Picos/        |",
    " |5,Bruno Alves,999.888.777-66,86999990005,Floriano/   |",
    " |6,Juliana Rocha,444.333.222-11,86999990006,Teresina/ |",
    " |7,Rafael Mendes,222.333.444-55,86999990007,Altos/    |",
    " |8,Patricia Gomes,666.555.444-33,86999990008,Uniao/   |",
    " |9,Fernando Costa,777.888.999-00,86999990009,Barras/  |", 
    " |10,Larissa Nunes,101.202.303-40,86999990010,Piripiri/|",
    
]

for cliente in clientes:
    arquivo.write(cliente + "\n")

arquivo.close()

print("Arquivo cliente.txt criado com sucesso!")
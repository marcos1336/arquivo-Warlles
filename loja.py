import os

# --- DICIONÁRIO DE DADOS PRÉ-EXISTENTES (Para não iniciar vazio) ---
DADOS_INICIAIS = {
    "TI": [
        ["1", "Andre Luiz", "andre.ti", "and123", "Administrador", "Notebook Dell", "06/05/2026"],
        ["2", "Bianca Melo", "bianca.ti", "bia456", "Supervisor", "Desktop HP", "06/05/2026"],
        ["3", "Rafael Gomes", "rafael.ti", "raf789", "Técnico", "Notebook Lenovo", "06/05/2026"],
        ["4", "Carlos Silva", "carlos.ti", "car321", "Técnico", "Desktop Acer", "07/05/2026"],
        ["5", "Juliana Costa", "juliana.ti", "jul654", "Supervisor", "Notebook Asus", "07/05/2026"],
        ["6", "Felipe Rocha", "felipe.ti", "fel987", "Administrador", "Notebook Dell", "08/05/2026"],
        ["7", "Mariana Sousa", "mariana.ti", "mar111", "Técnico", "Desktop HP", "08/05/2026"],
        ["8", "Bruno Lima", "bruno.ti", "bru222", "Técnico", "Notebook Lenovo", "09/05/2026"],
        ["9", "Larissa Gomes", "larissa.ti", "lar333", "Supervisor", "Desktop Acer", "09/05/2026"],
        ["10", "Gustavo Alves", "gustavo.ti", "gigus444", "Administrador", "Notebook Asus", "10/05/2026"],
        ["11", "Renata Lima", "renata.ti", "ren555", "Técnico", "Desktop Dell", "10/05/2026"],
        ["12", "Felipe Costa", "felipe.ti", "fel666", "Supervisor", "Notebook Acer", "11/05/2026"],
        ["13", "Camila Rocha", "camila.ti", "cam777", "Técnico", "Desktop Lenovo", "11/05/2026"],
        ["14", "Eduardo Gomes", "eduardo.ti", "edu888", "Administrador", "Notebook HP", "12/05/2026"],
        ["15", "Vanessa Silva", "vanessa.ti", "van999", "Técnico", "Desktop Asus", "12/05/2026"],
        ["16", "Tiago Mendes", "tiago.ti", "tia101", "Supervisor", "Notebook Dell", "13/05/2026"],
        ["17", "Patricia Alves", "patricia.ti", "pat202", "Técnico", "Desktop Acer", "13/05/2026"],
        ["18", "Bruno Freitas", "bruno.ti", "bru303", "Administrador", "Notebook Lenovo", "14/05/2026"],
        ["19", "Larissa Costa", "larissa.ti", "lar404", "Supervisor", "Desktop HP", "14/05/2026"],
        ["20", "Diego Ramos", "diego.ti", "die777", "Técnico", "Desktop Dell", "14/05/2026"]
    ],
    "Administrativo": [
        ["1", "Carlos Henrique", "Gerente", "(86) 99911-2233", "carlos@dm.com", "6500", "12/03/2021"],
        ["2", "Fernanda Lima", "Supervisora", "(86) 99877-4455", "fer@dm.com", "4800", "08/06/2022"],
        ["3", "João Pedro", "Assistente", "(86) 99755-3322", "joao@dm.com", "2300", "15/01/2024"],
        ["4", "Amanda Costa", "Coordenadora", "(86) 99661-1100", "amanda@dm.com", "5200", "11/05/2020"],
        ["5", "Lucas Martins", "Assistente", "(86) 99544-8822", "lucas@dm.com", "2400", "19/08/2023"],
        ["6", "Bianca Melo", "Analista", "(86) 99455-3311", "bianca@dm.com", "3900", "02/09/2022"],
        ["7", "Rafael Gomes", "Supervisor", "(86) 99322-1144", "rafael@dm.com", "4700", "10/10/2021"],
        ["8", "Juliana Sousa", "Recepcionista", "(86) 99211-2255", "juliana@dm.com", "1900", "22/02/2024"],
        ["9", "Felipe Costa", "Assistente", "(86) 99123-9988", "felipe@dm.com", "2200", "30/01/2023"],
        ["10", "Mariana Rocha", "Coordenadora", "(86) 99977-4411", "mariana@dm.com", "5000", "15/07/2020"],
        ["11", "Tiago Mendes", "Analista", "(86) 99812-4422", "tiago@dm.com", "3700", "05/04/2022"],
        ["12", "Camila Alves", "Assistente", "(86) 99771-2299", "camila@dm.com", "2500", "13/03/2024"],
        ["13", "Bruno Lima", "Supervisor", "(86) 99666-1199", "bruno@dm.com", "4900", "01/08/2021"],
        ["14", "Larissa Nunes", "Recepcionista", "(86) 99555-3311", "larissa@dm.com", "1850", "27/09/2023"],
        ["15", "Gustavo Silva", "Gerente", "(86) 99444-7766", "gustavo@dm.com", "6800", "14/11/2019"],
        ["16", "Renata Moura", "Analista", "(86) 99333-2288", "renata@dm.com", "3600", "18/12/2022"],
        ["17", "Diego Freitas", "Assistente", "(86) 99222-4499", "diego@dm.com", "2400", "09/01/2024"],
        ["18", "Patrícia Oliveira", "Coordenadora", "(86) 99111-7788", "patri@dm.com", "5300", "03/03/2021"],
        ["19", "Eduardo Ramos", "Supervisor", "(86) 99900-6677", "edu@dm.com", "4600", "25/06/2022"],
        ["20", "Vanessa Castro", "Assistente", "(86) 99888-5566", "vanessa@dm.com", "2350", "17/02/2024"]
    ],
    "Financeiro": [
        ["1", "PIX", "3500", "05/05/2026", "Fornecedor", "NF1001", "Mariana Costa"],
        ["2", "Cartão", "1250", "05/05/2026", "Materiais", "NF1002", "Ricardo Souza"],
        ["3", "Boleto", "5700", "06/05/2026", "Estoque", "NF1003", "Mariana Costa"],
        ["4", "PIX", "950", "06/05/2026", "Energia", "NF1004", "Felipe Lima"],
        ["5", "Dinheiro", "400", "06/05/2026", "Interno", "NF1005", "Ana Paula"],
        ["6", "Cartão", "1100", "07/05/2026", "Equipamento", "NF1006", "Ricardo Souza"],
        ["7", "PIX", "6300", "07/05/2026", "Estoque", "NF1007", "Mariana Costa"],
        ["8", "Boleto", "780", "07/05/2026", "Água", "NF1008", "Felipe Lima"],
        ["9", "PIX", "2450", "08/05/2026", "Marketing", "NF1009", "Ana Paula"],
        ["10", "Cartão", "900", "08/05/2026", "Limpeza", "NF1010", "Ricardo Souza"],
        ["11", "PIX", "1700", "08/05/2026", "Transporte", "NF1011", "Mariana Costa"],
        ["12", "Boleto", "2300", "09/05/2026", "Aluguel", "NF1012", "Felipe Lima"],
        ["13", "Dinheiro", "320", "09/05/2026", "Café", "NF1013", "Ana Paula"],
        ["14", "PIX", "4100", "09/05/2026", "Produtos", "NF1014", "Ricardo Souza"],
        ["15", "Cartão", "2050", "10/05/2026", "Equip. TI", "NF1015", "Mariana Costa"],
        ["16", "Boleto", "5900", "10/05/2026", "Fornecedor", "NF1016", "Felipe Lima"],
        ["17", "PIX", "870", "10/05/2026", "Escritório", "NF1017", "Ana Paula"],
        ["18", "Cartão", "1430", "11/05/2026", "Publicidade", "NF1018", "Ricardo Souza"],
        ["19", "Dinheiro", "260", "11/05/2026", "Manutenção", "NF1019", "Mariana Costa"],
        ["20", "PIX", "7200", "11/05/2026", "Eletrônicos", "NF1020", "Felipe Lima"]
    ],
    "Recursos_Humanos": [
        ["1", "Juliana Martins", "123.456.789-00", "Rua Flores, 120", "(86) 99944", "14/09/94", "Analista", "4000", "Sim", "VR"],
        ["2", "Paulo Ricardo", "987.654.321-00", "Av Central, 450", "(86) 99888", "21/03/88", "Supervisor", "5500", "Não", "Saúde"],
        ["3", "Camila Sousa", "741.852.963-11", "Rua Verde, 78", "(86) 99771", "11/07/99", "Assistente", "2500", "Não", "VT"],
        ["4", "André Silva", "222.333.444-55", "Rua A, 90", "(86) 99666", "08/01/90", "Analista", "4200", "Sim", "Saúde"],
        ["5", "Bianca Rocha", "333.444.555-66", "Rua B, 101", "(86) 99555", "19/06/95", "Assistente", "2700", "Não", "VR"],
        ["6", "Diego Costa", "444.555.666-77", "Rua C, 202", "(86) 99444", "03/10/87", "Supervisor", "5800", "Sim", "Odonto"],
        ["7", "Larissa Nunes", "555.666.777-88", "Rua D, 55", "(86) 99333", "27/04/98", "Assistente", "2600", "Não", "VT"],
        ["8", "Felipe Lima", "666.777.888-99", "Rua E, 87", "(86) 99222", "14/12/92", "Analista", "4100", "Sim", "VR"],
        ["9", "Amanda Freitas", "777.888.999-00", "Rua F, 33", "(86) 99111", "09/09/96", "Coord.", "6000", "Não", "Saúde"],
        ["10", "Gustavo Ramos", "888.999.000-11", "Rua G, 44", "(86) 99999", "05/11/85", "Supervisor", "5600", "Sim", "VR"],
        ["11", "Renata Alves", "999.000.111-22", "Rua H, 77", "(86) 99888", "17/05/97", "Assistente", "2550", "Não", "VT"],
        ["12", "Carlos Mendes", "111.222.333-44", "Rua I, 11", "(86) 99777", "30/08/91", "Analista", "4300", "Sim", "Odonto"],
        ["13", "Vanessa Castro", "222.444.666-88", "Rua J, 66", "(86) 99666", "25/02/93", "Coord.", "6200", "Não", "Saúde"],
        ["14", "Bruno Rocha", "333.555.777-99", "Rua K, 88", "(86) 99555", "12/04/89", "Supervisor", "5400", "Sim", "VR"],
        ["15", "Patrícia Moura", "444.666.888-00", "Rua L, 99", "(86) 99444", "22/07/94", "Assistente", "2700", "Não", "VT"],
        ["16", "Eduardo Gomes", "555.777.999-11", "Rua M, 100", "(86) 99333", "01/01/90", "Analista", "4500", "Sim", "Odonto"],
        ["17", "Fernanda Lima", "666.888.000-22", "Rua N, 12", "(86) 99222", "06/06/98", "Assistente", "2650", "Não", "VR"],
        ["18", "Tiago Souza", "777.999.111-33", "Rua O, 23", "(86) 99111", "18/03/86", "Coord.", "6300", "Sim", "Saúde"],
        ["19", "Ana Paula", "888.000.222-44", "Rua P, 34", "(86) 99900", "15/10/95", "Analista", "4000", "Não", "VT"],
        ["20", "Rafael Costa", "999.111.333-55", "Rua Q, 45", "(86) 99800", "29/09/92", "Supervisor", "5700", "Sim", "Vale"]
    ]
}

SETORES = {
    "1": ("TI", ["ID", "Nome", "Login", "Senha", "Acesso", "Equip", "Data"]),
    "2": ("Administrativo", ["ID", "Nome", "Cargo", "Telefone", "Email", "Salario", "Admissao"]),
    "3": ("Financeiro", ["ID", "Tipo", "Valor", "Data", "Desc", "NF", "Resp"]),
    "4": ("Recursos_Humanos", ["ID", "Nome", "CPF", "Endereço", "Tel", "Nasc", "Cargo", "Salario", "Férias", "Benef"])
}

# --- FUNÇÕES DE SISTEMA ---
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def verificar_e_popular_dados():
    """Cria os arquivos com os dados iniciais se eles estiverem vazios."""
    for id_setor in SETORES:
        nome_setor = SETORES[id_setor][0]
        arquivo = f"{nome_setor}.txt"
        
        # Se o arquivo não existir ou estiver vazio, popula com os dados iniciais
        if not os.path.exists(arquivo) or os.stat(arquivo).st_size == 0:
            with open(arquivo, "w", encoding="utf-8") as f:
                for linha in DADOS_INICIAIS[nome_setor]:
                    f.write("|".join(linha) + "\n")

def ler_arquivo(nome_setor):
    arquivo = f"{nome_setor}.txt"
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, "r", encoding="utf-8") as f:
        return [linha.strip().split("|") for linha in f]

def salvar_arquivo(nome_setor, dados):
    with open(f"{nome_setor}.txt", "w", encoding="utf-8") as f:
        for linha in dados:
            f.write("|".join(linha) + "\n")

def mostrar_tabela(nome_setor, campos, dados):
    print(f"\n{'='*110}")
    print(f" TABELA: {nome_setor.upper()} ".center(110, " "))
    print(f"{'='*110}")
    
    # Cabeçalho formatado
    header = " | ".join(f"{c:<10}" for c in campos)
    print(header)
    print("-" * 110)
    
    for i, d in enumerate(dados):
        # Mostra o índice da lista para facilitar alteração/exclusão
        linha = " | ".join(f"{str(item):<10}"[:10] for item in d)
        print(f"[{i}] {linha}")
    print("-" * 110)

def gerenciar_setor(opcao_setor):
    nome_setor, campos = SETORES[opcao_setor]
    
    while True:
        dados = ler_arquivo(nome_setor)
        print(f"\n>> GERENCIANDO SETOR: {nome_setor}")
        print("1. Ver registros (Listar)")
        print("2. Adicionar novo")
        print("3. Alterar registro")
        print("4. Excluir registro")
        print("5. Voltar ao menu principal")
        
        op = input("\nEscolha uma ação: ")

        if op == "1":
            mostrar_tabela(nome_setor, campos, dados)
            input("\nPressione Enter para continuar...")
        
        elif op == "2":
            novo = []
            print("\n--- CADASTRO ---")
            for campo in campos:
                novo.append(input(f"Digite {campo}: "))
            dados.append(novo)
            salvar_arquivo(nome_setor, dados)
            print("\n✔ Registro adicionado com sucesso!")

        elif op == "3":
            mostrar_tabela(nome_setor, campos, dados)
            try:
                idx = int(input("Digite o número [índice] à esquerda para alterar: "))
                if 0 <= idx < len(dados):
                    for i, campo in enumerate(campos):
                        valor = input(f"Novo {campo} (Vazio para manter '{dados[idx][i]}'): ")
                        if valor: dados[idx][i] = valor
                    salvar_arquivo(nome_setor, dados)
                    print("\n✔ Registro alterado!")
                else: print("Índice inválido!")
            except ValueError: print("Por favor, digite um número.")

        elif op == "4":
            mostrar_tabela(nome_setor, campos, dados)
            try:
                idx = int(input("Digite o número [índice] para excluir: "))
                if 0 <= idx < len(dados):
                    removido = dados.pop(idx)
                    salvar_arquivo(nome_setor, dados)
                    print(f"\n✔ Registro '{removido[1]}' excluído!")
                else: print("Índice inválido!")
            except ValueError: print("Por favor, digite um número.")

        elif op == "5":
            break

# --- INÍCIO DO PROGRAMA ---
verificar_e_popular_dados() # Garante que as tabelas existam com dados

while True:
    limpar_tela()
    print("╔══════════════════════════════════════════════════════╗")
    print("║          LOJA DE VARIEDADES - GESTÃO MULTI-TABELA      ║")
    print("╚══════════════════════════════════════════════════════╝")
    print("Escolha qual Tabela (Setor) deseja acessar:")
    print("1. Setor de TI")
    print("2. Setor Administrativo")
    print("3. Setor Financeiro")
    print("4. Setor de Recursos Humanos (RH)")
    print("5. Encerrar Sistema")
    
    escolha = input("\nOpção: ")
    
    if escolha in SETORES:
        gerenciar_setor(escolha)
    elif escolha == "5":
        print("\nFinalizando... Banco de dados salvo.")
        break
    else:
        input("\nOpção inválida! Enter para tentar novamente...")
# Solução simples com ficheiro texto

turma = []

def criar_turma():
    global turma
    turma = []
    print("Turma criada!")

def inserir_aluno():
    nome = input("Nome: ")
    id_aluno = input("ID: ")
    notaTPC = float(input("Nota TPC: "))
    notaProj = float(input("Nota Projeto: "))
    notaTeste = float(input("Nota Teste: "))
    aluno = (nome, id_aluno, [notaTPC, notaProj, notaTeste])
    turma.append(aluno)
    print(f"Aluno {nome} adicionado!")

def listar_turma():
    if not turma:
        print("Turma vazia!")
    else:
        for a in turma:
            print(f"ID: {a[1]} | Nome: {a[0]} | Notas: {a[2]}")

def consultar_aluno():
    id_busca = input("ID do aluno: ")
    for a in turma:
        if a[1] == id_busca:
            print(f"Nome: {a[0]} | Notas: {a[2]}")
            return
    print("Aluno não encontrado!")

def guardar_turma(fnome):
    f = open(fnome,"w")
    for a in turma:
        linha = f"{a[0]},{a[1]},{a[2][0]},{a[2][1]},{a[2][2]}\n"
        f.write(linha)
    f.close()
    print("Turma guardada!")

def carregar_turma(fnome):
    global turma
    turma = []
    f = open(fnome,"r")
    linhas = f.readlines()
    f.close()
    for linha in linhas:
        partes = linha.strip().split(",")
        nome = partes[0]
        id_aluno = partes[1]
        notas = list(map(float, partes[2:]))
        turma.append((nome,id_aluno,notas))
    print("Turma carregada!")

while True:
    print("\n===== MENU =====")
    print("1 - Criar turma")
    print("2 - Inserir aluno")
    print("3 - Listar turma")
    print("4 - Consultar aluno por ID")
    print("8 - Guardar turma")
    print("9 - Carregar turma")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_turma()
    elif opcao == "2":
        inserir_aluno()
    elif opcao == "3":
        listar_turma()
    elif opcao == "4":
        consultar_aluno()
    elif opcao == "8":
        fnome = input("Nome do ficheiro: ")
        guardar_turma(fnome)
    elif opcao == "9":
        fnome = input("Nome do ficheiro: ")
        carregar_turma(fnome)
    elif opcao == "0":
        print("A sair...")
        break
    else:
        print("Opção inválida!")

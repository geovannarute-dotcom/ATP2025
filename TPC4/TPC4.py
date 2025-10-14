# TPC4 - Aplicação para gerir um cinema
# Cada sala = [nlugares, vendidos, filme]

def inserirSala(cinema, sala):
    for s in cinema:
        if s[2] == sala[2]:
            print("Sala com este filme já existe.")
            return cinema
    cinema.append(sala)
    print(f"Sala do filme '{sala[2]}' adicionada.")
    return cinema

def listar(cinema):
    if not cinema:
        print("Não há salas registadas.")
        return
    for s in cinema:
        print("Filme:", s[2], "| Lugares:", s[0], "| Vendidos:", len(s[1]))

def disponivel(cinema, filme, lugar):
    for s in cinema:
        if s[2] == filme:
            return lugar not in s[1] and 1 <= lugar <= s[0]
    return False

def vendebilhete(cinema, filme, lugar):
    for s in cinema:
        if s[2] == filme:
            if disponivel(cinema, filme, lugar):
                s[1].append(lugar)
                print(f"Lugar {lugar} vendido para '{filme}'.")
            else:
                print("Lugar já ocupado ou inválido.")
            return cinema
    print("Filme não encontrado.")
    return cinema

def listardisponibilidades(cinema):
    if not cinema:
        print("Não há salas registadas.")
        return
    for s in cinema:
        livres = s[0] - len(s[1])
        print(f"{s[2]} - {livres} lugares disponíveis")

def libertarLugar(cinema, filme, lugar):
    for s in cinema:
        if s[2] == filme and lugar in s[1]:
            s[1].remove(lugar)
            print(f"Lugar {lugar} libertado em '{filme}'.")
            return cinema
    print("Lugar não encontrado.")
    return cinema

def removerSala(cinema, filme):
    for s in cinema:
        if s[2] == filme:
            if not s[1]:
                cinema.remove(s)
                print(f"Sala do filme '{filme}' removida.")
            else:
                print("Não é possível remover: bilhetes vendidos.")
            return cinema
    print("Filme não encontrado.")
    return cinema

def menu():
    print("""
===== GESTÃO DE CINEMA =====
(1) Inserir Sala
(2) Remover Sala
(3) Listar Filmes
(4) Vender Bilhete
(5) Libertar Lugar
(6) Listar Disponibilidades
(0) Sair
""")

def aplicacao():
    cinema = []
    while True:
        menu()
        op = input("Opção: ")

        if op == "1":
            filme = input("Nome do filme: ")
            lugares = int(input("Número de lugares: "))
            sala = [lugares, [], filme]
            cinema = inserirSala(cinema, sala)

        elif op == "2":
            filme = input("Filme a remover: ")
            cinema = removerSala(cinema, filme)

        elif op == "3":
            listar(cinema)

        elif op == "4":
            filme = input("Filme: ")
            lugar = int(input("Lugar a vender: "))
            cinema = vendebilhete(cinema, filme, lugar)

        elif op == "5":
            filme = input("Filme: ")
            lugar = int(input("Lugar a libertar: "))
            cinema = libertarLugar(cinema, filme, lugar)

        elif op == "6":
            listardisponibilidades(cinema)

        elif op == "0":
            print("A encerrar aplicação...")
            break

        else:
            print("Opção inválida.")

# Inicia a aplicação
if __name__ == "__main__":
    aplicacao()

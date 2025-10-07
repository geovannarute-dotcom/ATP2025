import random

def criar_lista():
    n = int(input("Quantos números quer gerar? "))
    lista = []
    for i in range(n):
        lista.append(random.randint(1, 100))
    print("Lista criada:", lista)
    return lista

def ler_lista():
    numeros = input("Introduza os números separados por espaço: ")
    lista = [int(x) for x in numeros.split()]
    print("Lista lida:", lista)
    return lista

def soma(lista):
    return sum(lista)

def media(lista):
    return sum(lista) / len(lista)

def maior(lista):
    return max(lista)

def menor(lista):
    return min(lista)

def ordenada_crescente(lista):
    return lista == sorted(lista)

def ordenada_decrescente(lista):
    return lista == sorted(lista, reverse=True)

def procurar(lista):
    x = int(input("Qual número quer procurar? "))
    if x in lista:
        return lista.index(x)
    else:
        return -1

def menu():
    print("\n(1) Criar Lista")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Está ordenada por ordem crescente")
    print("(8) Está ordenada por ordem decrescente")
    print("(9) Procurar um elemento")
    print("(0) Sair")

def main():
    lista = []
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            lista = criar_lista()

        elif opcao == "2":
            lista = ler_lista()

        elif opcao == "3":
            if lista:
                print("Soma =", soma(lista))
            else:
                print("A lista está vazia.")

        elif opcao == "4":
            if lista:
                print("Média =", media(lista))
            else:
                print("A lista está vazia.")

        elif opcao == "5":
            if lista:
                print("Maior =", maior(lista))
            else:
                print("A lista está vazia.")

        elif opcao == "6":
            if lista:
                print("Menor =", menor(lista))
            else:
                print("A lista está vazia.")

        elif opcao == "7":
            if lista:
                if ordenada_crescente(lista):
                    print("Sim, está ordenada por ordem crescente.")
                else:
                    print("Não está ordenada por ordem crescente.")
            else:
                print("A lista está vazia.")

        elif opcao == "8":
            if lista:
                if ordenada_decrescente(lista):
                    print("Sim, está ordenada por ordem decrescente.")
                else:
                    print("Não está ordenada por ordem decrescente.")
            else:
                print("A lista está vazia.")

        elif opcao == "9":
            if lista:
                pos = procurar(lista)
                if pos != -1:
                    print("Elemento encontrado na posição", pos)
                else:
                    print("Elemento não encontrado (-1)")
            else:
                print("A lista está vazia.")

        elif opcao == "0":
            print("A sair... Lista final:", lista)
            break

        else:
            print("Opção inválida. Tente outra vez.")

if __name__ == "__main__":
    main()

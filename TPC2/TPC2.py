#Jogo dos 21 Fósforos

#Explicação

print("Jogo dos 21 Fósforos ")
print("Há 21 fósforos. Em cada jogada podes tirar 1 a 4 fósforos. Quem tirar o último fósforo perde.")

# escolher quem começa
quem_comeca = input("Quem começa? (utilizador/computador): ")

fosforos = 21

while fosforos > 0:
    print("\nFósforos restantes:", fosforos)

    if quem_comeca == "utilizador":
        jogada = int(input("Quantos fósforos queres tirar? (1-4): "))
        if jogada < 1:
            jogada = 1
        if jogada > 4:
            jogada = 4
        if jogada > fosforos:
            jogada = fosforos
        fosforos = fosforos - jogada
        if fosforos == 0:
            print("Tirou o último fósforo, o utilizador perdeu!")
            break
        quem_comeca = "computador"
    else:
        
        if fosforos >= 4:
            jogada_pc = 1
        else:
            jogada_pc = 1
        print("Computador tira", jogada_pc, "fósforo(s).")
        fosforos = fosforos - jogada_pc
        if fosforos == 0:
            print("O computador tirou o último fósforo. O utilizador ganhou!")
            break
        quem_comeca = "utilizador"

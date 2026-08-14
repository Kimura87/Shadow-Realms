print("========================")
print("      SHADOW REALMS")
print("========================")

print("Bem-vindo ao jogo!")
print("Escolha sua classe:")
print("1. Guerreiro")
print("2. Mago")
print("3. Arqueiro")

classe = int(input("Digite sua escolha: "))

if classe == 1:
    classe = "Guerreiro"
    vida = 120
    ataque = 25
    defesa = 15

elif classe == 2:
    classe = "Mago"
    vida = 80
    ataque = 15
    defesa = 5

elif classe == 3:
    classe = "Arqueiro"
    vida = 100
    ataque = 20
    defesa = 10

else:
    print("Escolha inválida!")


print("Você escolheu a classe:", classe)
print("Sua vida é:", vida)
print("Seu poder de ataque é:", ataque)
print("Sua defesa é:", defesa)

print("Agora você está pronto para começar sua aventura!")

print("Você encontra um Goblin!")

inimigo = "Goblin"
vida_inimigo = 50
ataque_inimigo = 30
defesa_inimigo = 10git add RPG.py


while vida_inimigo > 0 and vida > 0:

    print("O que deseja fazer?")
    print("1. Atacar")
    print("2. Fugir")

    acao = int(input("Digite sua escolha: "))

    if acao == 1:
        print("Você atacou o Goblin!")

        dano = ataque - defesa_inimigo
        vida_inimigo = vida_inimigo - dano

        print("Você causou", dano, "de dano!")
        print("O Goblin agora tem", vida_inimigo, "de vida.")

        # Goblin só ataca se ainda estiver vivo
        if vida_inimigo > 0:

            dano_inimigo = ataque_inimigo - defesa

            if dano_inimigo < 0:
                dano_inimigo = 0

            vida = vida - dano_inimigo

            print("O Goblin atacou você!")
            print("O Goblin causou", dano_inimigo, "de dano!")
            print("Sua vida agora é", vida)

    else:
        print("Você fugiu do Goblin!")
        break


if vida_inimigo <= 0:
    print("========================")
    print("        VITÓRIA!")
    print("========================")
    print("Você derrotou o Goblin!")
    print("Vida restante:", vida)

if vida <= 0:
    print("========================")
    print("       GAME OVER")
    print("========================")
    print("Você foi derrotado pelo Goblin!")
from random import randint

pontos = [0, 0]  # contador de pontos: [usuário, máquina]
continuar = 'sim'
def jogo():
    opcoes = ['Tesoura', 'Pedra', 'Papel']
    while True:
        jogada = int(input('Qual é a sua jogada?\n1 - Tesoura\n2 - Pedra\n3 - Papel\n'))
        if jogada not in [1, 2, 3]:
            print("Opção invalida invalida")
        else:
            escolha_usuario = opcoes[jogada - 1]
            escolha_maquina = opcoes[randint(0, 2)]

            print(f"Você escolheu: {escolha_usuario}")
            print(f"A máquina escolheu: {escolha_maquina}")
            if escolha_usuario == escolha_maquina:
                print('Empate')
            elif (escolha_usuario == 'Tesoura' and escolha_maquina == 'Papel') or \
                (escolha_usuario == 'Pedra' and escolha_maquina == 'Tesoura') or \
                (escolha_usuario == 'Papel' and escolha_maquina == 'Pedra'): 
                print("Você venceu!")
                pontos[0] +=1
            else:
                print('Você perdeu!')
                pontos[1] += 1

            print(f'Placar: Você {pontos[0]} x {pontos[1]} Máquina')
            continuar = input("Você deseja jogar de novo?(sim/não): ")
            if continuar.strip().lower() == 'nao' or continuar.strip().lower() == 'não': #.strip para tirar os espaços
                break
    print("Fim de jogo")
jogo()

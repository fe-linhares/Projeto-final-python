from random import randint

def obter_jogada_usuario():
    while True:
        try:
            jogada = int(input('Qual é a sua jogada?\n1 - Tesoura\n2 - Pedra\n3 - Papel\n'))
            if jogada in [1, 2, 3]:
                return jogada
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def gerar_jogada_maquina():
    return randint(1, 3)

def determinar_resultado(jogada_usuario, jogada_maquina):
    opcoes = ['Tesoura', 'Pedra', 'Papel']
    escolha_usuario = opcoes[jogada_usuario - 1]
    escolha_maquina = opcoes[jogada_maquina - 1]

    print(f"\nVocê escolheu: {escolha_usuario}")
    print(f"A máquina escolheu: {escolha_maquina}")

    if jogada_usuario == jogada_maquina:
        print('Empate\nNinguém pontuou!\n')
        return 0
    elif (jogada_usuario == 1 and jogada_maquina == 3) or \
         (jogada_usuario == 2 and jogada_maquina == 1) or \
         (jogada_usuario == 3 and jogada_maquina == 2):
        print("Você venceu esta rodada!\n")
        return 1
    else:
        print("Você perdeu esta rodada!\n")
        return -1

def exibir_placar(pontos):
    print(f'Placar: Você {pontos[0]} x {pontos[1]} Máquina\n')

def jogo():
    pontos = [0, 0]  # [usuário, máquina]
    print("Bem-vindo ao pedra, papel e tesoura! Melhor de 3.")

    while pontos[0] < 2 and pontos[1] < 2:
        jogada_usuario = obter_jogada_usuario()
        jogada_maquina = gerar_jogada_maquina()
        resultado = determinar_resultado(jogada_usuario, jogada_maquina)

        if resultado == 1:
            pontos[0] += 1
        elif resultado == -1:
            pontos[1] += 1

        exibir_placar(pontos)

    if pontos[0] == 2:
        print("Parabéns! Você venceu!")
    else:
        print("A máquina venceu. Tente novamente!")

    print("Fim de jogo.")

jogo()

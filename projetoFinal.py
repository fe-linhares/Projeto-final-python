from random import randint
import time

def obter_nome_jogador():
    nome = input("Digite o seu nome: ").strip()
    if nome == "":
        nome = "Jogador"
    return nome

def obter_modo_jogo():
    while True:
        try:
            modo = int(input("Escolha o modo de jogo:\n1 - Melhor de 3 🥉\n2 - Melhor de 5 🏅\n"))
            if modo == 1:
                return 2 
            elif modo == 2:
                return 3  
            else:
                print("Opção inválida. Escolha 1 ou 2.")
        except ValueError:
            print("Entrada inválida. Digite 1 ou 2.")

def obter_jogada_usuario(nome):
    while True:
        try:
            jogada = int(input(f'\n{nome}, qual é a sua jogada?\n1 - ✂️ Tesoura\n2 - 🪨 Pedra\n3 - 📄 Papel\n'))
            if jogada in [1, 2, 3]:
                return jogada
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def gerar_jogada_maquina():
    print("\n🤖 A máquina está escolhendo...")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(0.5)
    return randint(1, 3)

def determinar_resultado(jogada_usuario, jogada_maquina, nome):
    opcoes = ['✂️ Tesoura', '🪨 Pedra', '📄 Papel']
    escolha_usuario = opcoes[jogada_usuario - 1]
    escolha_maquina = opcoes[jogada_maquina - 1]

    print(f"\n{name_emoji(nome)} escolheu: {escolha_usuario}")
    print(f"🤖 Máquina escolheu: {escolha_maquina}")

    if jogada_usuario == jogada_maquina:
        print('😐 Empate! Ninguém pontuou!\n')
        return 0
    elif (jogada_usuario == 1 and jogada_maquina == 3) or \
         (jogada_usuario == 2 and jogada_maquina == 1) or \
         (jogada_usuario == 3 and jogada_maquina == 2):
        print(f"🎉 {name_emoji(nome)} venceu esta rodada!\n")
        return 1
    else:
        print("😈 A máquina venceu esta rodada!\n")
        return -1

def exibir_placar(pontos, nome):
    print(f'📊 Placar: {name_emoji(nome)} {pontos[0]} x {pontos[1]} 🤖 Máquina\n')

def perguntar_jogar_novamente():
    while True:
        resposta = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if resposta in ['s', 'n']:
            return resposta == 's'
        else:
            print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

def name_emoji(nome):
    return f"{nome} 🧑" 

def jogo():
    print("🎮 Bem-vindo ao Pedra, Papel e Tesoura! 🎮")

    while True:
        nome = obter_nome_jogador()
        pontos_para_vencer = obter_modo_jogo()
        pontos = [0, 0]  # [jogador, máquina]

        print(f"\n🙌 Vamos lá, {name_emoji(nome)}! Quem fizer {pontos_para_vencer} pontos primeiro vence!\n")

        while pontos[0] < pontos_para_vencer and pontos[1] < pontos_para_vencer:
            jogada_usuario = obter_jogada_usuario(nome)
            jogada_maquina = gerar_jogada_maquina()
            resultado = determinar_resultado(jogada_usuario, jogada_maquina, nome)

            if resultado == 1:
                pontos[0] += 1
            elif resultado == -1:
                pontos[1] += 1

            exibir_placar(pontos, nome)

        if pontos[0] == pontos_para_vencer:
            print(f"🏆 Parabéns {name_emoji(nome)}! Você venceu o jogo!")
        else:
            print("💀 A máquina venceu. Tente novamente!")

        print("🔚 Fim de jogo.")

        if not perguntar_jogar_novamente():
            print("👋 Até a próxima!")
            break

jogo()

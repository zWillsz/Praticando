from random import choice

maquina_vitorias = jogador_vitorias = empates = 0

def opcao_jogador():
    esc_jogador = input('Escolha Pedra, Papel ou Tesoura: ').lower()
    if esc_jogador == 'pedra':
        return esc_jogador
    elif esc_jogador == 'papel':
        return esc_jogador
    elif esc_jogador == 'tesoura':
        return esc_jogador
    else:
        print('Opção Inválida. Tente novamente')
        opcao_jogador()


def opcao_maquina():
    esc_maquina = choice(['pedra', 'papel', 'tesoura'])
    return esc_maquina


while True:

    print(50 * '-')
    esc_jogador = opcao_jogador()
    esc_maquina = opcao_maquina()
    print(50 * '-')

    if (esc_jogador == 'pedra') and (esc_maquina == 'tesoura') \
        or (esc_jogador == 'papel') and (esc_maquina == 'pedra') \
            or (esc_jogador == 'tesoura') and (esc_maquina == 'papel') :

        print(f'O jogador escolheu {esc_jogador} e a Máquina escolheu {esc_maquina}'  
        ' Resultado: Você venceu!')
        jogador_vitorias += 1

    elif (esc_jogador == 'pedra') and (esc_maquina == 'pedra')\
         or (esc_jogador == 'papel') and (esc_maquina == 'papel')\
            or (esc_jogador == 'tesoura') and (esc_maquina == 'tesoura'):
        print(f'O jogador escolheu {esc_jogador} e a Máquina escolheu {esc_maquina}'  
        ' Resultado: Empate!')
        empates += 1

    else:
        print(f'O jogador escolheu {esc_jogador} e a Máquina escolheu {esc_maquina}'  
        ' Resultado: Você perdeu!')
        maquina_vitorias += 1

    print(50 * '-')
    print(f'Empates: {empates}')
    print(f'Vitórias do Jogador: {jogador_vitorias}')
    print(f'Vitórias da Máquina: {maquina_vitorias}')
    print(50 * '-')

    vai_jogar = input('Você quer jogar novamente? ')

    if vai_jogar in ['SIM', 'sim', 's', 'S', 'Sim']:
        pass
    else:
        break
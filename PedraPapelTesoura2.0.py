from random import choice

playerVitorias = maqVitorias = empates = 0

def opcaoPlayer():
    escPlayer = input('Escolha Pedra, Papel ou Tesoura: ').lower()

    if escPlayer == 'pedra':
        return escPlayer
    elif escPlayer == 'papel':
        return escPlayer
    elif escPlayer == 'tesoura':
        return escPlayer
    else:
        print('Opção Inválida, tente novamente.')
        opcaoPlayer()


def opcaoMaq():
    escMaq = choice(['pedra', 'papel', 'tesoura'])
    return escMaq


while True:
    escPlayer = opcaoPlayer()
    escMaq = opcaoMaq()

    if (escPlayer == 'pedra') and (escMaq == 'tesoura')\
        or (escPlayer == 'papel') and (escMaq == 'pedra')\
            or (escPlayer == 'tesoura') and (escMaq == 'papel'):
                print(f'O Jogador escolheu {escPlayer} e a Máquina escolheu {escMaq}' 
                      ' Resultado: Você ganhou!')
                playerVitorias += 1

    elif escPlayer == escMaq:
         print(f'O Jogador escolheu {escPlayer} e a Máquina escolheu {escMaq}' 
                      ' Resultado: Empate!')
         empates += 1

    else:
         print(f'O Jogador escolheu {escPlayer} e a Máquina escolheu {escMaq}' 
                      ' Resultado: Derrota!')
         maqVitorias += 1
         
    print(f'Vitórias do Jogador: {playerVitorias}')
    print(f'Empates: {empates}')
    print(f'Vitórias da Máquina: {maqVitorias}')

    
    vai_jogar = input('Você quer jogar novamente? ').lower()

    if vai_jogar == ['s', 'sim']:
        pass
    else:
        break
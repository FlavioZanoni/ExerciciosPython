from random import randint
jogadas = ('Pedra','Papel','Tesoura')
jogadapc = randint(0,2)
print(' (0) Pedra \n (1) Papel \n (2) Tesoura')
jogador = int(input('Escolha uma das alternativas '))
print(f'O computador jogou {jogadas[jogadapc]}')
print(f'Você jogou {jogadas[jogador]}')
if jogadapc == 0:
    if jogador == 0:
        print('Empate!!')
    elif jogador == 1:
        print('Você venceu!!')
    elif jogador == 2:
        print('Você perdeu!!')
    else:
        print('Jogada invalida!!')
elif jogadapc == 1:
    if jogador == 0:
        print('Você perdeu!!')
    elif jogador == 1:
        print('Empate!!')
    elif jogador == 2:
        print('Você ganhou!!')
    else:
        print('Jogada invalida!!')
elif jogadapc == 2:
    if jogador == 0:
        print('Você ganhou!!')
    elif jogador == 1:
        print('Você perdeu!')
    elif jogador == 2:
        print('Empate!!')
    else:
        print('Jogada invalida!!')
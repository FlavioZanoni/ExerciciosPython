# ex07 - numero inteiro e diz se ele é primo
num = int(input('Entre um numero inteiro: '))
cont = 0
for c in range(1, num + 1 ):
    if num % c == 0:
        print('\033[36m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print(f'\n\033[m O numero {num} foi dividido {cont} vezes')
if cont > 2:
    print('Não é primo')
else:
    print('É primo')

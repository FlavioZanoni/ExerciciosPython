# ex02 - conversão de base numérica 
num = int(input('entre um numero inteiro '))
print('Leia a tabela: \n (1) Binario \n (2) Octal  \n (3) Hexadecimal ')
base = int(input('Levando em consideração a tabela, qual base numerica o numero deve ser convertido? '))
if base == 1:
    print(f'O numero {num} convertido para Binário é {bin(num)[2:]}')
elif base == 2:
    print(f'O numero {num} convertido para Octal é {oct(num)[2:]}')
elif base == 3:
    print(f'O numero {num} convertido para Hexadecimal é {hex(num)[2:]}')
else:
    print('Número invalido, escolha uma opção entre os numeros dados na tabela')
    
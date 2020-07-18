# ex03 - entra 2 numeros e mostra o maior valor
val0 = int(input('Coloque um valor '))
val1 = int(input('Coloque outro Valor '))
if val0 > val1:
    print(f'Valor 1 "{val0}"" é maior')
elif val0 < val1:
    print(f'Valor 2 "{val1}" é maior')
else:
    print('Os valores são iguais')
# ex03 soma de impares multiplos de 3
num = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        num += c # += é uma forma menor de escrever (num = num + 1)
print(f'A soma dos {cont} valores impares divisiveis por 3 é {num}')

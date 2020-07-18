# ex06 - encontrar os 10 primeiros termos de uma progressão aritimética
pt = int(input('Entre o primeiro termo da PA: '))
razao = int(input('Entre a razão dessa PA: '))
contagem = pt
for c in range(1, 11):
    contagem += razao
    print(contagem, end='-')
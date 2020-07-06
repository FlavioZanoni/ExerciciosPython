# velocidade = int(input('qual velocidade ? '))
# if velocidade >=80:
#     print('ae se fudeu em fiote, deixa eu calcular a multa aq')
#     velm = velocidade - 80
#     velmu = velm * 7
#     print('Calculando...')
#     time.sleep (0.5)
#     print(f'Sua multa sera de {velmu} reais.')
# else:
#     print('ta de boa fiote o limite era 80km/h')

# ex03 - digite um numero e separe ele em par ou impar
# num1 = int(input('Entre um numero '))
# num2 = num1 % 2
# if num2 == 0:
#     print('É par')
# else:
#     print('É impar')

# ex04 - viagem preço por km >200 .5 <200 .45
# km = int(input('A viagem é de quantos quilometros? '))
# km1 = km * .5
# km2 = 200*.5 + (km-200)*.45
# if km <= 200:
#     print(f'sua viagem de {km} quilometros vai custar {km1} reais')
# else:
#     print(f'Sua viagem de {km} quilometros ira custar {km2} reais')

# ex05 - descobrir se o ano é ou nao bissexto
# from datetime import date
# ano = int(input('Coloque o ano em mente, ou coloque 0 para o ano atual '))
# if ano == 0:
#     ano = date.today().year
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print('ano bissexto')
# else:
#     print('Ano normal')

# ex06 - numero maior
# num1 = int(input('Coloque um numero '))
# num2 = int(input('Coloque outro numero '))
# num3 = int(input('Coloque mais um numero '))

# ex07 - aumento de salario
# sal = float(input('Qual seu salario? '))
# sal1 = (sal * 15) / 100
# sal2 = (sal * 10) / 100
# if sal > 1250:
#     print(f'Seu aumento é de {sal2} ')
# else:
#     print(f'Seu aumento é de {sal1} ')

# ex08 - tres retas, descobrir se e possivel formar um triangulo a partir delas
# l1 = int(input('Entre um lado para o triangulo '))
# l2 = int(input('Entre outro lado para esse triangulo '))
# l3 = int(input('Entre o ultimo lado desse triangulo '))
# if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
#     print('Impossivel')
# else:
#     print('Possivel')
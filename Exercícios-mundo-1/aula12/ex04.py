# ex04 - ano de alistamento
from datetime import date
ano = int(input('Coloque o ano de nascimento. '))
anohoje = date.today().year
idade = anohoje - ano
if idade == 18:
    print('Está no ano de se alistar')
elif idade < 18:
    falta = 18 - idade
    if falta == 1:
        print('Falta 1 ano para voce se alistar')
    else:
        print(f'Faltam {falta} anos para se alistar')
if idade > 18:
    print('Você ja se alistou ou ja deveria ter sido alistado')

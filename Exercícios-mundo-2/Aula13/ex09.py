# ex 09 - ano de nascimento e idicar qual esta na maioridade
from datetime import date
maiorid = 0
menorid = 0
for c in range(1, 8):
    ano = int(input(f'Qual ano de nascimento da {c}ª pessoa? '))
    if date.today().year - ano < 18:
        menorid += 1
    else:
        maiorid += 1
print(f'Das datas apontadas, {menorid} pessoas são menores de idade \ne {maiorid} pessoas são maiores de idade')
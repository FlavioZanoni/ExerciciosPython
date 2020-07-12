# ex06 - categioria por idade
idade = int(input('Qual sua idade? '))
if idade <= 9:
    print('Mirim')
elif idade > 9 and idade <=14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Junior')
elif idade == 20:
    print('Master')
else:
    print('Sênior')
# ex04 - tabuada do numero escolhido pelo usuário 
num = int(input('Qual numero você gostaria de saber a tabuada? '))
for c in range(1, 11):
    print(f'{num} x {c} = {num * c} ')
# ex01 = emprestimo bancario 
valorcasa = int(input('Qual o valor da casa a ser comprada? '))
sal = int(input('Qual o seu salário médio mensal? '))
anosp = int(input('Em quantos anos você prentende pagar essa casa ? '))
print('Calculando ...')
parcelas = anosp * 12
salpc = (sal * 30) / 100
val1 = valorcasa / parcelas
print(f'O valor de cada parcela usando 30% de seu salário será de :{val1} reais')
if val1 > salpc:
    print('O valor de prestação exede 30% do seu salario')
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo aceito')
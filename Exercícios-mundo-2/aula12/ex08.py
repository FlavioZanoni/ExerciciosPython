# ex08 - calcular imc e classficar
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura * altura)
print(f'Seu IMC vale {imc}')
if imc < 18.5:
    print('Baixo peso!')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal!')
elif imc >= 25 and imc < 30:
    print('Sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Obesidade mórbida')
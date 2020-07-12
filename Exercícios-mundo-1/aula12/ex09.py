# ex09 - calcular porcentagem 
preço = float(input('Qual o preço do produto? '))
print('Qual o metodo de pagamento dentre estes?\n (1) à vista, (2) à vista no cartao, (3) 2x no cartão, (4) 3 vezes mais no cartão ')
metodo = int(input('Responda usando os numeros do lado da do metodo'))
if metodo == 1:
    avista = preço - ((preço * 10) / 100)
    print(f'O preço será {avista}')
elif metodo == 2:
    avc = preço - ((preço * 5) / 100)
    print(f'O preço será {avc}')
elif metodo == 3:
    print(f'O preço não terá alteraçoes, {preço}')
elif metodo == 4:
    tres = preço + ((preço * 20) / 100)
    print(f'O preço será de {tres}')
else:
    print('Metodo de pagamento nao existe')

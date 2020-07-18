# ex08 - algoritimo ára verificar palindromos
frase = str(input('Entre a frase ')).strip().upper()
palavras = frase.split()
junçao = ''.join(palavras)
inverter =''
for letras in range(len(junçao) - 1, -1, -1):
    inverter += junçao[letras]
print(f'A frase {junçao} ao contrario fica {inverter}')
if inverter == junçao:
    print('Palíndromo!!')
else:
    print('Não é um palíndromo')

# como pensado antes, da pra fazer sem o for, colocando inverso = junto[::-1] de começo a fim negativo, fazendo-o ficar ao contrario


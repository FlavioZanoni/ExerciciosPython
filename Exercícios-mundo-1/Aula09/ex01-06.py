# ex01 - leia o nome e mostre modificaçoes
# frase = str(input('seu nome completo ')).strip()
# print(f' seu nome todo em maiusculo é {frase.upper()}')
# print(f'seu nome todo em minusculo é {frase.lower()}')
# print(f'seu nome tem ao todo {len(frase) - frase.count(" ") } letras')
# print(f'seu primeiro nome tem {frase.find(" ")} letras')
# separado = frase.split()
# print(f'seu primeiro nome tem {len(separado[0])} letras')

# ex02 - numero  ate 9999 para separar as unidades
# num = int(input('numero de 00 a 9999 '))
# n = str(num)
# print(f'unidade: {n[0]}')
# print(f'dezena: {n [1]}')
# print(f'centena: {n[2]}')
# print(f'milhar: {n[3]}')

# ex03 - entre a cidade e diz se tem santo ou nao
# cidade = str(input('Sua Cidade? '))
# print(cidade[:5].upper == 'SANTO')

# ex04 - silva no nome
# nome = str(input('Seu nome ')) .strip()
# print(f"Seu nome tem Silva? {'SILVA' in nome.upper()}")

# ex05 - ocorrencia da letra 'a'
# frase = str(input('coloque uma frase ')) .strip() .upper()
# print(f"a letra a aparece {frase.count('A')} vezes")
# print(f"a primeira apariçao de 'a' foi na posiçao {frase.find('A') +1 }")
# print(f"a ultima apariçao de 'a' foi na posiçao {frase.rfind('A') +1 }")

# ex06 - nome da pessoa, separar primeiro e ultimo nome
# nome = str(input('Seu nome completo ')) .strip()
# n = nome.split()
# print(f"seu primeiro nome é {n[0]}")
# print(f"seu ultimo nome é {n[len(n)-1]}")

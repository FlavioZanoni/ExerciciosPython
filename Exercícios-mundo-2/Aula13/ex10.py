# ex10 - dados 5 pesos qual o maior e qual o menor
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Qual o peso da {c}ª pessoa? '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior} e o menor peso é {menor} ')
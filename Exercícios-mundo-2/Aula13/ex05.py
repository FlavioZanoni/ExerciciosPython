# 05 - programa que leia 6 int e conte somente os pares
num1 = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Entre o {c}º numero '))
    if num % 2 == 0:
        num1 += num 
        cont += 1
print(f'Você colocou {cont} números pares, e a soma foi {num1}')

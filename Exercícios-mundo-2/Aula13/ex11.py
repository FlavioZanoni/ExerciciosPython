    # ex11 - leia nome idade e sexo de 4 pessoas e mostre meida de idade do grupo nome do homem mais velho e quantas mulheres menores de 20 anos
idade1 = 0
idadeh = 0
mulher = 0
velho = ''
for c in range(1, 5):
    print(f'--- {c}ª pessoa---')
    nome = str(input('Nome dessa pessoa? '))
    idade = int(input('Qual a idade dessa pessoa? '))
    sexo = str(input('Qual o sexo dessa pessoa (M/F)? ')).upper()
    idade1 += idade
    if sexo == 'F' and idade <= 20:
        mulher += 1
    elif sexo == 'M' and idade > idadeh:
        idadeh = idade 
        velho = nome.capitalize()
print(f'O homem mais velho é {velho}, com {idadeh} anos \na media de idade é {idade1 / 4} \ne tem {mulher} mulher/mulheres com menos de 20 anos.')
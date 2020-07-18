nota0 = float(input('Coloque 1ª nota; '))
nota1 = float(input('Coloque sua 2ª nota; '))
media = (nota0 + nota1) / 2
print(f'Sua média foi de {media}')
if media < 50:
    print('Reprovado!')
elif media >= 50 and media <= 69:
    print('Recuperação!')
elif media >= 85:
    print('Parabéns pelas boas notas! Você Passou!!!')
else:
    print('Parabéns, você passou')
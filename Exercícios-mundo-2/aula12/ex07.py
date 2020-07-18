# ex07 - lados do triangulo separando em classes
l1 = int(input('Entre um lado do triangulo '))
l2 = int(input('Entre outro lado do triangulo '))
l3 = int(input('Entre o ultimo lado do triangulo '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('Possivel')
    if l1 == l2 and l2 == l3:
         print('Equilátero')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Isóceles')
    else:
     print('Escaleno')
else:
    print('Impossivel')

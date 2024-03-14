'''
Exercício 
Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como:
a) Equilátero (3 lados iguais)
b) Isósceles (2 lados iguais)
c) Escaleno (3 lados diferentes)
'''

lado_01 = int(input('Qual o valor do primeiro lado do triangulo: '))
lado_02 = int(input('Qual o valor do segundo lado do triangulo: '))
lado_03 = int(input('Qual o valor do terceiro lado do triangulo: '))

if (lado_01 > 0) and (lado_02 > 0) and (lado_03 > 0):
    if (lado_01 + lado_02 > lado_03) and (lado_01 + lado_03 > lado_02) and (lado_02 + lado_03 > lado_01):
        if lado_01 == lado_02 == lado_03:
            print('É um triângulo equilátero')
        elif lado_01 == lado_02 or lado_01 == lado_03 or lado_02 == lado_03:
            print('É um triângulo isósceles')
        elif lado_01 != lado_02 != lado_03:
            print('É um triângulo escaleno')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo!')    
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo!')

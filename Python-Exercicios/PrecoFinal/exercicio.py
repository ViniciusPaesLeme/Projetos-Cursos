""" 
Exercicio 

Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto ao ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto.
"""


preco = float(input('Digite o preço do produto: '))
p = float(input('Digite o percentual de desconto (0 - 100%): '))
desconto = preco * (p / 100)
final = preco - desconto
print(f'O valor do produto é {preco:.2f}, o desconto foi de {desconto:.2f}, referente a {p}% do desconto. Valor final do produto é {final:.2f}')
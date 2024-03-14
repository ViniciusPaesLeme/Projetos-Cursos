'''
Exercício 3
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.

calcule o preço de acordo com a tabela:

tipo residencial:
ate 500kWh 0.40; acima de 500 0.65

tipo comercial:
até 1000kWh 0.55; acima de 1000 0.60

tipo industrial:
até 5000kWh 0.55; acima 5000 0.60

'''

print('Escolha o tipo de instalação: ')
print('R para residencial.')
print('C para comercial.')
print('I para industrial')
kwh = float(input('Quanto de kWh foi consumido? '))
tipo = input('Qual o tipo de instalação (R, C ou I)')

if tipo == 'R':
    if kwh <= 500:
        res = kwh * 0.40
        print('Você é do tipo residencial e gastou {}kWh, e o valor da sua conta é de R${}'.format(kwh, res))
    elif kwh > 500:
        res = kwh * 0.65
        print('Você é do tipo residencial e gastou {}kWh, e o valor da sua conta é de R${}'.format(kwh, res))
    else:
        print('Por favor, digite um valor válido!')
elif tipo == 'C':
    if kwh <= 1000:
        res = kwh * 0.55
        print('Você é do tipo comercial e gastou {}kWh, e o valor da sua conta é de R${}'.format(kwh, res))
    elif kwh > 1000:
        res = kwh * 0.60
        print('Você é do tipo comercial e gastou {}kWh, e o valor da sua conta é de R${}'.format(kwh, res))
    else:
        print('Por favor, digite um valor válido!')
elif tipo == 'I':
    if kwh <= 5000:
        res = kwh * 0.55
        print('Você é do tipo industrial e gastou {}kWh, e o valor da sua conta é de R${}'.format(kwh, res))
    elif kwh > 5000:
        res = kwh * 0.60
        print('Você é do tipo industrial e gastou {}kWh, e o valor da sua conta é de R${}'.format(kwh, res))
    else:
        print('Por favor, digite um valor válido!')
else:
    print('Digite o Valor válido')
print('CALCULADORA')
print(' + para adição')
print(' - para subtração')
print(' * para multiplicação')
print(' / para divisão')
print('Pressione outra tecla para sair!')
OP = input('Qual operação deseja fazer? ')
if OP == '+' or OP == '-' or OP == '*' or OP == '/':
    A = int(input('Digite o primeiro valor: '))
    B = int(input('Digite o segundo valor: '))

    if OP == '+':
        res = A + B 
        print('Resultado: {} + {} = {}'.format(A, B, res))
    elif OP == '-':
        res = A - B 
        print('Resultado: {} - {} = {}'.format(A, B, res))
    elif OP == '*':
        res = A * B 
        print('Resultado: {} * {} = {}'.format(A, B, res))
    elif OP == '/':
        res = A / B 
        print('Resultado: {} / {} = {}'.format(A, B, res))
    else:
        print('Operação inválida')
    
else:
    print('Opção invalida! Saindo...')

print('Saindo da Calculadora')

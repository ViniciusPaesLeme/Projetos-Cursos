print("Bem-vindo a Loja de Gelados do Vinícius Gall Paes Leme")

# funções criadas para criar o menu com opções e valores do cardápio
def cardapio():
    print('-'*23, 'Cardápio', '-'*24)
cardapio()

def tamanho():
    print('-'*6, '|', ' Tamanho ','|' ,' Cupuaçu (CP) ', '|', ' Açai (AC)', '|', '-'*6)
tamanho()

def tamanhoP():
    print('-'*6, '|', '    P    ','|' ,'   R$10.00    ', '|', '  R$12.00 ', '|', '-'*6)
tamanhoP()

def tamanhoM():
    print('-'*6, '|', '    M    ','|' ,'   R$15.00    ', '|', '  R$17.00 ', '|', '-'*6)
tamanhoM()

def tamanhoG():
    print('-'*6, '|', '    G    ','|' ,'   R$19.00    ', '|', '  R$21.00 ', '|', '-'*6)
tamanhoG()

print('-'*57)

total_pedido = 0

while True: 
    sabor = input("Entre com o sabor desejado (CP/AC)): ").upper()
    # condicionais para verificar o sabor escolhido
    if sabor not in ['CP', 'AC']:
        print("Sabor inválido. Tente novamente.")
        continue  

    tamanho = input("Entre com o tamanho desejado(P/M/G): ").upper()

    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido. Tente novamente.")
        continue  
    # apos verificar o sabor, a condicional seleciona o tamanho do produto para atribuir valor
    if sabor == 'CP':
        if tamanho == 'P':
            valor_pedido = 9.00
        elif tamanho == 'M':
            valor_pedido = 14.00
        else:
            valor_pedido = 18.00
    else:  
        if tamanho == 'P':
            valor_pedido = 11.00
        elif tamanho == 'M':
            valor_pedido = 16.00
        else:
            valor_pedido = 20.00
    #adiciona valor 
    total_pedido += valor_pedido

    continuar_pedido = input("Deseja mais alguma coisa (s/digite outra tecla)? ").lower()
    # se for diferente de s, encerrar o loop
    if continuar_pedido != 's':
        break  

print("Total do pedido: R${:.2f}".format(total_pedido))
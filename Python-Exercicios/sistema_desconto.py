print("Bem-vindo a Loja do Vinícius Gall Paes Leme, RU: 4665342 ")

# variáveis para armazenar input do valor unitário e da quantidade
valor_unitario = float(input("Entre com o valor unitário do produto: R$"))
qtd = int(input("Entre com a quantidade do produto: "))

# Variável para armazenar o calculo
valor_sem_desconto = valor_unitario * qtd

#Condicional para definir o desconto que será aplicado
if valor_sem_desconto < 2500.00:
    desconto = 0
elif 2500.00 <= valor_sem_desconto < 6000.00:
    desconto = 4
elif 6000.00 <= valor_sem_desconto < 10000.00:
    desconto = 7
else:
    desconto = 11

# variável do valor total com o desconto
valor_com_desconto = valor_sem_desconto * (1 - desconto / 100)

print("Valor total sem desconto: R$ {:.2f}".format(valor_sem_desconto))
print("Valor total com desconto: R$ {:.2f} (desconto {}%)".format(valor_com_desconto, desconto))



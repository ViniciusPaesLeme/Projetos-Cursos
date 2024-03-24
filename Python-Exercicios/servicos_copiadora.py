#função que solicita ao usuário que escolha um tipo de serviço e retorna o custo.
def escolha_servico():
    while True:
        try:
            servico = input('Entre com o tipo de serviço desejado: \nDIG - Digitalização \nICO - Impressão Colorida\nIBO - Impressão Preto e Branco \nFOT - Fotocópia \n>> ').upper()
            if servico == 'DIG':
                return 1.10
            elif servico == 'ICO':
                return 1.00
            elif servico == 'IBO':
                return 0.40
            elif servico == 'FOT':
                return 0.20
            else:
                print('Opção de serviço inválida. Tente novamente.')
        except KeyboardInterrupt:
            print('\nPrograma encerrado.')
            exit()
        except Exception as e:
            print('Erro: {}'.format(e))

# função que pede para o usuário inserir o número de páginas e retorna este valor.           
def num_pagina():
    while True:
        try:
            paginas = int(input('Entre com o número de páginas: '))
            if paginas <= 0:
                print('Número de páginas inválido. Tente novamente!')
            elif paginas >= 20000 :
                print('Não aceitamos pedidos com mais de 20000 páginas!')
            else:
                return paginas
            
        except ValueError:
            print('Por favor, digite um valor numérico para o número de páginas.')
        except KeyboardInterrupt:
            print('\nPrograma encerrado.')
            exit()
        except Exception as e:
            print('Erro: {}'.format(e))

# Adiciona serviço extra e retorna o custo            
def servico_extra():
    while True:
        try:
            extra = int(input('Deseja adicionar mais algum serviço: \n1 - Encadernação Simples;\n2 - Encadernação Capa Dupla;\n0 - Nenhum.\n>> '))  
            if extra in [0, 1, 2]:
                if extra == 1:
                    return 15.00 
                elif extra == 2:
                    return 40.00
                else:
                    return 0.00
            else:
                print('Opção de serviço adicional inválida. Tente novamente.')
        except ValueError:
            print('Por favor, Digite um número correspondente à opção desejada.')
        except KeyboardInterrupt:
            print('\nPrograma encerrado.')
            exit()
        except Exception as e:
            print('Erro: {}'.format(e))
            
# Try except utilizado para lidar com os erros de entrada do usuário.
            

print('Bem-vindo aos serviços de copiadora, do Vinícius Gall Paes Leme.')


servico = escolha_servico() 
num_paginas = num_pagina()
extra = servico_extra()

# Condicional do calculo total a pagar com o desconto
if num_paginas > 2000:
    total_sem_desconto = servico * num_paginas + extra
    desconto = total_sem_desconto * 0.25
    total = total_sem_desconto - desconto
elif num_paginas >= 200:
    total_sem_desconto = servico * num_paginas + extra
    desconto = total_sem_desconto * 0.20
    total = total_sem_desconto - desconto
elif num_paginas >= 20:
    total_sem_desconto = servico * num_paginas + extra
    desconto = total_sem_desconto * 0.15
    total = total_sem_desconto - desconto
else:
    total = servico * num_paginas + extra

# Apresenta o total a pagar com desconto, o serviço escolhido, o número de páginas e o custo adicional.Também mostra o valor total sem o desconto aplicado.
print("\nTotal com desconto (R$): {:.2f} (serviço: R${:.2f} * páginas: {} + extra: R${:.2f})".format(total, servico, num_paginas, extra))
print('Valor sem o desconto (R$): {:.2f}'.format(total_sem_desconto))

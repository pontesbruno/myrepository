menu = '''
Escolha sua Operação\n
[d] depositar
[s] sacar
[e] extrato
[q] sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Valor do depósito:' ))
               
        if valor>0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print('Não foi possível realizar a operação, o valor informado é inválido.')
        
    elif opcao == 's':
        valor = float(input('Qual valor que deseja sacar? '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITES_SAQUES
        
        if excedeu_saldo:
            print('O valor excedeu o seu saldo em conta.')
    
        elif excedeu_limite:
            print('Você excedeu o limite do valor de saques diários')
        
        elif excedeu_saques:
            print('Você exedeu o limite do valor para saques diários!')

        elif valor>0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques+=1
    
        else:
            print('Não foi possível realizar a operação, o valor informado é inválido.')
 
     
    elif opcao == 'e':
        print('EXTRATO\n')
        if saldo == 0:
            print('Não foram realizadas operações bancárias') 
        else:
            print(extrato)
            print(f'\nsaldo: R$ {saldo:.2f}')
       
    elif opcao == 'q':
        break

    else:
        print('\n(Operação não pode ser realizada. por favor colocar uma opção válida.)')
    
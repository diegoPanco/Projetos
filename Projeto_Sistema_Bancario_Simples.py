menu="""

[d]Depositar
[s]Sacar
[e]Extrato 
[q]Sair

=> """
saldo=0
limite=500
extrato=''
numero_de_saques=0
LIMITE_DE_SAQUES=3

while True:

    opcao= input(menu)
    if ((opcao!= ('d')) and (opcao!=('q'))) and ((opcao!=('s')) and (opcao!=('e'))):
        print('opção inválida')
    
    if opcao=="d":
        print('Digite o valor do Depósito')
        deposito=int(input())

        if deposito>0:
            saldo+=deposito
            print('foi depositado R${} na sua conta'.format(deposito))
    if opcao=='e':
        print ("Você tem R${}".format(saldo))
    if opcao=='s':
        saque=int(input())
        
        if (saque<=saldo) and (saque<=limite) and (numero_de_saques<LIMITE_DE_SAQUES):
            saldo=saldo-saque
            numero_de_saques+=1

            print("Você sacou R${}".format(saque))
        else:
            print("Erro na operação")

    if opcao=="q":
        break


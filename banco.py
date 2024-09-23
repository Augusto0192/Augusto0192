LIMITE_SAQUES = 3
LIMITE_VALOR = 500
MENU = """
MENU:
[D]Depositar
[S]Sacar
[E]Extrato
[Q]Sair

=> """
erro = "operação inválida"

def validar_valor(valor):
    if valor>0:
        print("valor válido... Continuando Operação...")
        return True
    else:
        print(erro)
        return False

def deposito(valor,saldo,extrato):
    if validar_valor(valor):
        saldo+= valor
        extrato += f'Depósito: R${valor}\nSaldo apos essa operação: {saldo:.2f}\n'
        return (extrato,saldo)
    else:
        return (extrato,saldo)

def saque(valor,saldo,extrato,qtd_saques):
    validar_saque = saldo>=valor and valor <= LIMITE_VALOR and qtd_saques<LIMITE_SAQUES
    if validar_valor(valor) and validar_saque:
        saldo -= valor
        extrato+= f'Saque: R${valor}\nSaldo apos essa operação: {saldo:.2f}\n'
        qtd_saques+=1
        return extrato,saldo,qtd_saques
    else:
        print(erro+' verifique a plausabilidade da sua transação')
        return extrato,saldo,qtd_saques

extrato_atual=''
saldo=0.00
resp=''
qtd_saques=0
while resp.lower()!='q':   
    resp = input(MENU).lower()
    match resp:
        case 'd':
            valor = int(input("Valor: "))
            extrato_atual,saldo = deposito(valor,saldo,extrato_atual)
        case 's':
            valor = int(input("Valor: "))
            extrato_atual,saldo,qtd_saques = saque(valor,saldo,extrato_atual,qtd_saques)
            
        case 'e':
            print(extrato_atual)
        case 'q':
            continue
        case _:
            print("Resposta invalida!\nescolha uma opção valida no menu: ")
"""Desafio didático de sistema bancário em terminal.""" 

from math import isfinite

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500.0
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3


def ler_valor(prompt):
    """Lê um valor numérico finito sem encerrar o programa em entradas inválidas."""
    while True:
        entrada = input(prompt).strip().replace(",", ".")
        try:
            valor = float(entrada)
        except ValueError:
            print("Entrada inválida. Digite um valor numérico, por exemplo 125.50.")
            continue

        if not isfinite(valor):
            print("Entrada inválida. Digite um valor finito.")
            continue

        return valor


while True:
    opcao = input(menu).strip().lower()

    if opcao == "d":
        valor = ler_valor("Digite o valor a ser depositado: ")

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso.")
        else:
            print("Operação falhou! O valor deve ser maior que zero.")

    elif opcao == "s":
        valor = ler_valor("Informe o valor do saque: ")

        if valor <= 0:
            print("Operação falhou! O valor deve ser maior que zero.")
        elif valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print(f"Operação falhou! O limite por saque é R$ {limite:.2f}.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Você atingiu o número máximo de saques.")
        else:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1
            print("Saque realizado com sucesso.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("\n".join(extrato) if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=============================")

    elif opcao == "q":
        print("Obrigado por utilizar o sistema. Até logo!")
        break

    else:
        print("Opção inválida. Selecione d, s, e ou q.")

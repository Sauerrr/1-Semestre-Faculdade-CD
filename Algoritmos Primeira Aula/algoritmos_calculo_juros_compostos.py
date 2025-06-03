capital_inicial = int(input("Digite o capital inicial: "))
taxa_juros = int(input("Digite a taxa de juros: "))
tempo_meses = int(input("Digite o tempo em meses: "))

m = capital_inicial * (1 + taxa_juros/100)**tempo_meses
print(f" O resultado é de:  {m:.2f}")
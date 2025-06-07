import random, time

dados = list(range(1, 100001))
random.shuffle(dados)

comparacoes = 0
trocas = 0

inicio = time.perf_counter()

contagem = [0] * 100000
for n in dados:
    contagem[n - 1] += 1
    comparacoes += 1  
i = 0
for valor, qtd in enumerate(contagem):
    for _ in range(qtd):
        dados[i] = valor + 1
        i += 1
        trocas += 1

fim = time.perf_counter()

print(f"Tempo: {fim - inicio:.4f}s | Comparações: {comparacoes} | Trocas: {trocas}")

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

# Programa principal
frase = input("Digite um texto: ")
total_vogais = contar_vogais(frase)
print(f"O texto contém {total_vogais} vogais.")

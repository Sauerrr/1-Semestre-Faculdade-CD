# Primeiro, vou definir todas as variáveis do meu código, onde:
# C representa Celsius, K representa Kelvin, F representa Fahrenheit e R representa Rankine.
# Na variável C, vou solicitar que o usuário informe um valor em graus Celsius.
# Defini a variável como float, pois o valor pode ter casas decimais.

C = float(input("Digite a temperatura em Graus Celcius: "))

# Dentro de cada variável, vou colocar o cálculo necessário para converter graus Celsius 
# para cada respectiva unidade de medida de temperatura apresentada no código.


K = C + 273.15
F = (9/5) * C + 32
R= (C + 273.15) * (9/5)

# Nesta parte, é bem simples. Vou exibir um print para cada unidade de medida, 
# que será mostrado quando o usuário inserir um valor. 
# Assim, ele saberá como o número que digitou fica em cada unidade de temperatura.

print(f'{C} em Celcius é: {C:.2f}')
print(f'{C} em Kelvin é: {K:.2f}')
print(f'{C} em Fahrenheit é: {F:.2f}')
print(f'{C} em Rankine é: {R:.2f}')

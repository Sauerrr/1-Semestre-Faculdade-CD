#raio = 5
#altura = 10
#pi = 3.14

#area_base = pi * (raio ** 2)
#volume = area_base * altura

#print("Área da base: ", area_base)
#print("Volume: ", volume)

import math

raio = float(input("Digite o raio: "))
altura = float(input("Digite a altura: "))


area_base = math.pi * (raio ** 2)
volume = area_base * altura

print(f"Área da base: {area_base:.2f}")
print(f"Volume:  {volume:.2f}")

# Programa para contar múltiplos de 7 y 9 entre 1000 y 5000

cont7 = 0
cont9 = 0

for i in range(1000, 5001):
    
    if i % 7 == 0:
        cont7 += 1
        
    if i % 9 == 0:
        cont9 += 1

print("Cantidad de múltiplos de 7:", cont7)
print("Cantidad de múltiplos de 9:", cont9)

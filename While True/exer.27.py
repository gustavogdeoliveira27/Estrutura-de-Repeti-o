pares = 0

while True:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares += 1
    elif num < 0:
        break
    
print("O número total de pares é:", pares)
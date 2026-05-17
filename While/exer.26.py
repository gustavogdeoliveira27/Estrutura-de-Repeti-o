cont = 0
i = 1

while i <= 10:
    num = int(input("Digite um número de 1 a 10: "))
    if num > 5:
        cont += 1
    i += 1
    
print(cont)
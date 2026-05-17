cont = 0

for i in range(5):
    n = int(input("Digite um número: "))
    if n < 0:
        cont += 1
        
print(cont)
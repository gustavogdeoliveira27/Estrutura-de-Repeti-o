cont = 0

quant = int(input("Quantos números você vai digitar? "))
i = 0

while i < quant:
    num = float(input(f"Digite o {i+1}° número: "))
    if num < 0:
        cont += 1
    i += 1
    
print("quantidade de números negativos:", cont)
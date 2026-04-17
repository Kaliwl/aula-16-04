num = input("Digite um número binário: ")
n = len(num) - 1
decimal = 0

for i in num:
    decimal = decimal + int(i) *2**n
    n = n - 1

print("o binário %s equivale a %d na base decimal: " %(num,decimal))
    





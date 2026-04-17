contador = 1
soma = 0
resp = "S"
while resp == "S" or resp == "s":
    num = int(input("Digite um número: "))
    soma = soma + num
    contador = contador + 1
    resp = input("deseja continuar?:S/N ")
    
media = soma/contador
print(f"a média dos números digitados é {media} ")

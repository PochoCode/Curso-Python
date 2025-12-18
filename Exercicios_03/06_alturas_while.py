# %%
soma = 0 # Valor final
count = 4 #  contador de alturas

while count > 0:
    altura = input("Entre com a altura ")
    altura = float(altura)

    soma += altura
    count -= 1

print ("A soma das alturas é",soma)

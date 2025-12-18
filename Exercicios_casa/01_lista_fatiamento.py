# %%

lista = [1,1,2,3,5,8,6,1,2,5,4,8,3]

numero = input("Entre com o numero ")
numero = int(numero)

count = 0

for i in lista :
    if i == numero :
        count += 1

print("O numero",numero,"se repete:",count,"vezes")
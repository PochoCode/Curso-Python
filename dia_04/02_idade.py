# %%
idades = []

while True :
    idade = input("Entre com a idade ")

    if idade == "" :
        break

    idades.append(int(idade))

<<<<<<< HEAD
print(idades)
=======
media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)



print("Media :",media)
print("Minimo :",minimo)
print("Maximo :",maximo)
print("Qtde de elementos :",qtde)
# %%
>>>>>>> 998aecddb963928860436e78a8747fcd3063acd0

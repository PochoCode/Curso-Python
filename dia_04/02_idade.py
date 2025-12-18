# %%
idades = []

while True :
    idade = input("Entre com a idade ")

    if idade == "" :
        break

    idades.append(int(idade))

print(idades)
# %%
arquivo = "lista.csv"

with open(arquivo) as open_file:
    lista = open_file.readlines()



print(lista)
# %%
for l in lista:
    print(l)
# %%
dados = dict()

chaves = lista[0].strip("\n").split(";")
for c in chaves:
    dados[c] = []


# %%
for l in lista[1:]:

    valores = l.strip("\n").split(";")

    for i in range(len(valores)):

        dados[chaves[i]].append(valores[i])

dados
# %%
idades = []
for i in dados["idade"]:
    idades.append(int(i))


media = sum(idades) / len(idades)
media
# %%

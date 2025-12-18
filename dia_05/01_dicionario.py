# %%
#dicionarios são pares de chave valor

dados_robin = {"sobrenome":"Rodriguez","nome":"Robin","filhos":True}

print(dados_robin)
# %%
dados_robin["nome"]
# %%
dados_robin = {"sobrenome":"Rodriguez",
               "nome":"Robin",
               "filhos":True,
               "formação":["Analises desenvolvimento","Administração"],
               "cargos":[{"nome":"Administrador","empresa":"grcar"},
                         {"nome":"dev jr","empresa":"Superdia"},
                         {"nome":"ds sr.","empresa":"Boticario"},
                         {"nome":"ds especialista","empresa":"viavarejo"}]}

dados_robin["cargos"][-1]["nome"]
ultima_empresa = dados_robin["cargos"][-1]["empresa"]
print(ultima_empresa)
# %%
dados_robin["estado civil"] = "solteiro"

dados_robin
# %%
print("chaves :",dados_robin.keys())
print(dados_robin.values())
print("Items :",dados_robin.items())
# %%

for i in dados_robin :
    print(i,"->",dados_robin[i])
# %%

for chave, valor in dados_robin.items():
    print(chave,":",valor)
# %%

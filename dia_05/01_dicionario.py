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

dados_robin["cargos"][-1]["empresa"]

# %%
dados_robin["Estado Civil"] = "Casado"
dados_robin

# %%
dados_robin["filhos"] = False
dados_robin
# %%
dados_robin.items()
# %%
dados_robin.keys()
# %%
for i, j in dados_robin.items():
    print(1,"->",j)
# %%

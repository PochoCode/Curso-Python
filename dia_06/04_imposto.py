# %%
def calc_imposto(preço:float, tx_base = 0.1, **kwargs):
    imposto = preço * tx_base

    for i in kwargs:
        print(i,kwargs[i])
        imposto += preço * kwargs[i]

    return imposto



# %%
impostos_gerais = {
"Municipal" : 0.02,
"estadual" : 0.2
}



#calc_imposto(1.0, 0.1, Municipal = 0.02, estadual = 0.2)
calc_imposto(1.0, 0.1, **impostos_gerais, internacional = 0.1)
# %%

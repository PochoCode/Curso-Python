# %%
#def juros_compostos(anos):
   # return 1000 * 1.13 ** anos
def juros_compostos(aporte:int, taxa:float, anos:int)-> float:
    """juros compostos serve para calcular o retorno financeiro a partir de um aporte
    Deve se considera o valor , a taxa de juros atual e o tempo em anos para calculo do rendimento

    aporte: 
    um numero inteiro que represente o valor em R$

    taxa:
    um numero float entre 0 e 1 que represente o valor das taxas de juros
    
    anos:
    um numero inteiro >= 1 que represente o tempo que o investimento tera liquidez
"""
    return aporte * (1 + taxa) ** anos

 
# %%
juros_compostos(1000 , 0.13, 4)

# %%

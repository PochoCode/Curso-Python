# %%
def par_impar(numero:int):
    if numero % 2 == 0:
        print("O numero",numero,"é par")

    else :
        print("O numero",numero,"é impar")



numero = input("Entre com um numero inteiro: ")
numero = int(numero)

par_impar(numero)
# %%

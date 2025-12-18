# %%
#def soma(valores:list)->float:
#    return sum(valores)


#def media(valores:list)->float:
#    return soma(valores) / len(valores)



#a = float(input("Entre com o valor de a: "))
#b = float(input("Entre com o valor de b: "))
#c = float(input("Entre com o valor de c: "))



#print("Media:",media([a,b,c]))

# %%
def soma(a:float, b:float, *args)->float:
    valores = [a,b] + list(args)
    return sum(valores)


def media(a:float, b:float, *args)->float:
    return soma(a, b, *args) / (len(args)+2)



a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))



print("Media:",media(a, b, c))
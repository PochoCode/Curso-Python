# %%
#Escreva um programa que registre as frases digitadas
#pelo usuario,pare com um enter e exiba o numero de vezes
#que uma frase repitiu

frases={}

while True:
    frase = input("Entre com a frase: ")
    if frase == "" :
        break

    if frase not in frases:
        frases[frase] = 1

    else :
        frases[frase] += 1


for i, j in frases.items():
    print(i,"->",j)
# %%
#Faça um programa que receba 4 alturas usando um laço
#de repetição e realice a soma
soma = 0 #total de alturas
count = 4 #contador de alturas

for i in range(count):
    altura =  input("Digite a altura ")
    altura = float(altura)
    soma += altura
print("Altura total:",soma)
# %%

# %%

# uma maneira de definir lista
idade = [18,25,48,38,28,33]

print(idade)
# %%
robin = ["robin","Rodriguez",23,1.73,"solteiro",2400]

print(robin)
# %%
type(robin)
# %%
robin[0]
# %%
print(robin[3])

# %%
idade = [18,25,48,38,28,33]

print("Soma das idades:",sum(idade))

print("Tamanho idade:",len(idade))
#Aprendendo a acessar a quantidade de elementos da lista
print("Media das idades:",sum(idade)/len(idade))

#Acessar o valor menor e o maior da lista
print("O maior valor da lista é:",min(idade))


print("O maior valor da lista é:",max(idade))
# %%
robin = ["Robin Anner",23,True,"solteiro",["Trabalha","Estuda","Joga"]]

robin[4][0]

dados = robin[4]
dados_pessoais = dados[0]

print(dados_pessoais)
# %%

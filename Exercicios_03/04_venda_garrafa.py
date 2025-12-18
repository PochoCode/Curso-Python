# %%

texto = """
Escolha a sua compra:
(1) Agua mineral natural
(2) Agua mineral com gas

"""

opção =  input(texto)

conta = 0

if opção == "1":
    conta = 1.50
elif opção == "2":
    conta = 2.50


if conta == 0:
    print("Entre a opção correta")
else:
    print("Sua conta é: $R",conta)
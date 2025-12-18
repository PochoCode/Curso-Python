# %%

texto = """
Escolha a sua compra:
(1) Agua mineral natural  1.5 $R
(2) Agua mineral com gas  2.5 $R

"""

opção =  input(texto)

valor_item = 0

if opção == "1":
    valor_item = 1.50
elif opção == "2":
    valor_item = 2.50


if valor_item == 0:
    print("Entre a opção correta")
else:
   
    qtde = input("Quantas garrafas")
    qtde = int(qtde)
    conta = valor_item * qtde
    print("Sua conta é: $R",conta)
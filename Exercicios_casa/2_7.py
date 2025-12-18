# %%
#Programa para comprar frutaas usando diccionario
# Pera: R$1,25
# Goiaba:  R$2,15
# Abacaxi: R$3,20
# Jaca: R$5,80
# Laranja: R$0,65
# Limão: R$1,25
# Maçã: R$1,50
# Banana: R$2,75
# Uva: R$1,90

fruta = input("""Escolha a fruta a comprar:
            (1)Pera: 
            (2)Goiaba: 
            (3)Abacaxi: 
            (4)Jaca:
            (5)Laranja:
            (6)Limão: 
            (7)Maçã:
            (8)Banana:
            (9)Uva:
              """)


frutas = {
    "1" : "R$1,25" ,
    "2" : "R$2,15",
    "3" : "R$3,20",
    "4" : "R$5,80",
    "5" : "R$0,65",
    "6" : "R$1,25",
    "7" : "R$1,50",
    "8" : "R$2,75",
    "9" : "R$1,90"
}

if fruta in frutas:

    


    print(frutas[fruta])

else:
    print("Entre com um valor certo")
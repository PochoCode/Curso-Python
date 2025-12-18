#Realize um programa que sorteie um numero entre 1 e 15
#o usuario tera 3 chances para acertar
#a cada tentativa deve informar se o chute foi maior ou menor

# %%
import random

def get_input():

    while True:
        
        try :
          
            numero_usuario = int(input("Entre com um numero: "))

        except ValueError as err :
            print("Valor invalido")
            continue
      

        if 1 <= numero_usuario <= 15 :
            return numero_usuario
      
        print("Valor invalido!.O valor deve estar entre 1 e 15")


def check_numbers(sorteio,usuario):
    if  usuario == sorteio :
        print("Parabens voce se tornou um milhonario")
        return True

    elif usuario > sorteio :
        print("Numero muito alto.Tente novamente!!")
        return False

    else:
        print("numero muito baixo tente novamente!!")
        return False

    

numero_sorteio = random.randint(1,15)

for i in range(3) :

    numero_usuario =  get_input()

    if check_numbers(sorteio = numero_sorteio,usuario = numero_usuario):
        break
    
else:
    print("Suas tentativas acabaram")
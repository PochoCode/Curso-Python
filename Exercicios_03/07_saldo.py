# %%
saldo_total = 0

while True:
    saldo = input("Digite seu saldo ")

    if saldo == "":
        break
    saldo_total += float(saldo)


print("Seu saldo final é",saldo_total)
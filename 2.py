cont = 0
cont2 = 0
medaltura = 0

for i in range(3):
    idade = int(input("Digite a idade da "+str(i+1)+"º pessoa: "))
    altura = float(input("Digite a altura da "+str(i+1)+"º pessoa: "))

    medaltura += altura

    if idade >=20 and idade <=35:
        cont += 1
    if idade>=18 and altura >=1.6 and altura >=1.8:
        cont2 += 1
    
medalt = medaltura / 3
print("A quantidade de pessoas entre 20 a 35 anos é: ", cont)
print("A quantidade de pessoas maiores de idade entre 1.6m à 1.8m é: ", cont2)
print("A média da altura é: ", medalt)

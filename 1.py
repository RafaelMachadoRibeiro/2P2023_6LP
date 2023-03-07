k = int(input("Digite o valor de K: "))
m = int(input("Digite o valor de M: "))
n = int(input("Digite o valor de N: "))

mult = 0

if(k<m or m<n):
    for i in range(m,n):
        if(i%k==0):
            mult = mult + 1

    print("Existem ", mult, " números múltiplos de ", k, " entre ", m," e ", n)

else:
    print("Valor informados não são validos.")

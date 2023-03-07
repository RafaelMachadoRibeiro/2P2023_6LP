#Entrada usuário
hora_ini = float(input("Digite a hora inicial do jogo: "))
min_ini = float(input("Digite o minuto inicial do jogo: "))
hora_fim = float(input("Digite o hora final do jogo: "))
min_fim = float(input("Digite o minuto final do jogo: "))

#Condições de início
if (hora_ini > 24 or hora_fim > 24):
    print("Entrada de dados não é valida.")
elif (min_ini > 59 or min_fim > 59):
    print("Entrada de dados não é valida.")

#Se hora de início for maior
elif (hora_ini > hora_fim):
    duracao_h = hora_fim - hora_ini + 24
    if(min_ini > min_fim):
        duracao_h = duracao_h - 1
        duracao_m = min_fim - min_ini + 60
        print("Se passaram: ", duracao_h, "horas,", duracao_m, "minutos.")
    else:
        duracao_m = min_fim - min_ini
        print("Se passaram: ", duracao_h, "horas,", duracao_m, "minutos.")

#Se hora de inicio for menor
elif (hora_ini < hora_fim):
    duracao_h = hora_fim - hora_ini
    if(min_ini > min_fim):
        duracao_h = duracao_h - 1
        duracao_m = min_fim - min_ini + 60
        print("Se passaram: ", duracao_h, "horas,", duracao_m, "minutos.")
    else:
        duracao_m = min_fim - min_ini
        print("Se passaram: ", duracao_h, "horas,", duracao_m, "minutos.")
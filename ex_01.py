while True:
    print("Digite um ano acima de 2000 para conferir se é bissexto e suas festividades", end="\n")
    ano = int(input("- "))

  #BISSEXTO
    resto100 = ano % 100
    resto4 = ano % 4
    resto400 = ano % 400
    bissexto = False

  #HULUCULU
    resto15 = ano % 15
    huluculu = False

  #BULUKULU
    resto55 = ano % 55
    bulukulu = False

    if ano >= 2000:
        if(resto4 == 0 and resto100 != 0) or resto400 == 0:
            bissexto = True
            if resto55 == 0:
                bulukulu = True

        if resto15 == 0:
            huluculu = True

      #PRINT
        if bissexto or huluculu or bulukulu:
            if(bissexto == True):
                print("This is a leap year.", end="\n")
            if(huluculu == True):
                print("This year we have a Huluculu Festival.", end="\n")
            if(bulukulu == True):
                print("This year we have a Bulukulu Festival.", end="\n")
            continue
        else:
            print("This is an ordinary year.")
            continue
    else:
        print("Por favor digite um ano maior que 2000")
        continue
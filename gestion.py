def factorielle(a):

    if (type(a) == str):
        print(" Il est impossible de saisir une chaine de caractére")
        print(" veuillez saisir des valeurs numérique")

        if (type(a) == str):
            a = int(input('Entrez une valeur numérique pour a ='))

    elif (type(a) == complex):
        print(" Nous ne pouvons pas choiri un nombre complexe")
        while (type(a) == complex):

            a = int(input(" Veuillez saisir un nombre numérique pour a"))

    elif (a < 0):
        print(" nous ne pouvons pas choisir un numéro négatif")

        if (a < 0):
            a = int(input("veuillez entrer un nombre positif pour a "))


    elif (len(str(a)) > 1000):
        print (" Nous ne pouvons pas choisir un nombre trop grand")
        
        while len(str(a) > 1000):
            a = int(input("LA valeur que vous avez tapez est supérieur au factorielle de 1000 "))
   
    c = factorielle(a)
    

    return c
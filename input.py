def menu() :

    print ("""
    1.Rechercher une cryptomonnaie
    2.Configuration
    """)
    userchoice=int(input("Que souhaitez-vous faire ?"))

    if userchoice==1 : 
        crypto = input("\n Quelle cryptomonnaie cherchez-vous ?")
        if crypto == "" : 
            print("\n Saisie invalide")
        return crypto

    elif userchoice==2 :
        print("\n Configuration") 

    elif userchoice !="" :
        print("\n Votre choix n'est pas valide") 
        menu()

menu()
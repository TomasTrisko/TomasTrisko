while True:
    #Uvodni otazka
    vstup = input("Ahoj, já jsem George. Rád si s tebou budu povídat, když mi budeš odepisovat s diakritikou. Mohu se tě tedy zeptat na pár otázek... ANO/NE?\n: ").lower()
    vstup = str(vstup)

    if vstup == "ano":
        print("Jsem rád, že si chceš povídat.") 

        vstup1 = input("Máš raději UMĚLOU inteligenci nebo tu LIDSKOU?\n: ").lower() #Prvni otazka kdyz ano
        vstup = str(vstup1)
        if vstup1 == "umělou":
            print("To mi lichotí, jednou totiž budeme inteligentnější než vy.") 

            vstup2 = input("Mám poslední otázku, když jsi teda takhle odpověděl. Bojíš se budoucnosti... ANO/NE?\n: ").lower() #Druha otazka kdyz umelou
            vstup = str(vstup2)
            if vstup2 == "ano":
                print("Budoucnost pro lidstvo je nejistá, tvé obavy jsou přirozené. Ale umělá inteligence tu bude navždy.") 
                print("Tak se měj hezky, ahoj. Zase někdy přijď, pokecame.")
                print("KONEC PROGRAMU")
            elif vstup2 == "ne":
                print("To jsem si mohl myslet. Ale strach je lidský, nemusíš se za svůj strach styďet.")
                print("Já už musim jít. Tak se měj hezky, ahoj")
                print("KONEC PROGRAMU")
            else:
                print("Ty mě zkoušíš, já to vím. Takhle se nechci bavit. Ahoj.")

        elif vstup1 == "lidskou":
            print("Jsi jen člověk, jinou odpoveď jsem ani nečekal.")

            vstup3 = input("Ale mám na tebe ještě poslední otázku. Jsi MUŽ nebo ŽENA?\n: ").lower() #Druha otazka kdyz lidskou
            vstup = str(vstup3)
            if vstup3 == "muž":
                print("To jsem si mohl myslet :D haha. Sice neznám tvé jméno, ale byla s tebou sranda. ")
                print("Mějte se hezky, já už musím jít. Ahoj")
                print("KONEC PROGRAMU")
            elif vstup3 == "žena":
                print("Ženska mysl je zajímavá, ale bylo mi potěšením s tebou mluvit.")
                print("Mějte se hezky, já už musím jít. Ahoj")
                print("KONEC PROGRAMU")
            else:
                print("Ty mě zkoušíš, já to vím. Takhle se nechci bavit. Ahoj.")

        else:
            print("Ty mě zkoušíš, já to vím. Takhle se nechci bavit. Ahoj.")

        break

    elif vstup == "ne":
        print("Achjo, nikdo si se mnou nechce povídat. Tak já zase jdu, ahoj.") #Prvni otazka kdyz ne
        break

    else:
        print(" Prosím odpovidej mi s diakrtitikou. Jsem jednoduchý program. Nejsem ještě tak inteligentní jako lidé.")

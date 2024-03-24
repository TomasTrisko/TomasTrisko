type = input("jaký chcete typ telefonu? Možnosti: normal, super, premium\n")

if type != "normal":
    print(f"Cena telefonu typu {type} je 15.000 Kč")
else:
    print(f"Cena telefonu typu {type} je 25.000 Kč")
year = int(input("Jaký rok chcete zkontrolovat?: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Tento rok je přestupný")
        else:
            print("Tento rok není přestupný")
    else:
        print("Tento rok je přestupný")
else:
    print("Tento rok není přestupný")

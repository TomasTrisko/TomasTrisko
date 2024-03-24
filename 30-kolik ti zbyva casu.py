vek = int(input("Kolik ti je let?\n"))
zbyva = 90 - vek
mesic = 12 * zbyva
tyden = 52 * zbyva
dny = 365 * zbyva
print(f"Zbývá ti\n{dny} dnů\n{tyden} týdnu\n{mesic} měsíců\nneboli {zbyva} let")

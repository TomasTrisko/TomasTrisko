type = input("Jakou chcete velikosit pizzy? S, M nebo L? \n")
bill = 0
if type == "S":
    bill = 100
if type == "M":
    bill = 150
if type == "L":
    bill = 200

feferonky = input("Chcete na pizzu přidat feferonky - A/N?\n")
if feferonky == "A":
    if type == "S":
        bill = bill + 20
    else:
        bill = bill + 30

cheese = input("Chcete přidat i sýr - A/N?\n")

if cheese == "A":
    bill = bill + 15

print (f"Cena Vaší pizzy je {bill} Kč")
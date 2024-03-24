print("Kalkulačka")
cost = int(input("Zadejte cenu: "))
pertentage = int(input("Kolik chcete dát spropitného v %: "))
people = int(input("Mezi kolik lidí se má částka rozdělit? "))

one_paynment = (cost + (cost*pertentage/100))/people	
final_paynment = "{:.2f}".format(one_paynment)
print(f"Každý člověk by měl zaplatit {final_paynment} Kč")

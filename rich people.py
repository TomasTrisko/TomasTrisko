import random 

names = input("Napiš mi jména všech, ale oddělené čárkou\n")

list_people = names.split(", ")
random_number = random.randint(0, len(list_people)-1)

print(f"{list_people[random_number]} bude dneska platit")
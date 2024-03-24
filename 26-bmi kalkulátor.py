height = input("Zadejte svojí výšku v metrech:\n")
weight = input("Zadejte svoji váhu v kg:\n")

bmi = int(weight) / (float(height) ** 2)
bmi = int(bmi)
print("Vaše BMI je", str(bmi))

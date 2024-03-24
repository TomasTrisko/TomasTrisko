# muze byt zvetseno #
n = 6 
for i in range(1, n+1):
    for j in range(i-1):
        print(".", end=" ")
    for k in range(n-i):
        print("#", end=" ")
    print("")

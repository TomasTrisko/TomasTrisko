def product_list(arr):
    total = 1
    for num in arr:
        total *= num
    return total

num = [1, 2, 3, 4, 5]
produkt = product_list(num)
print(produkt)

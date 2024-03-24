def sum_everyother(arr):
    total = 0
    for i in range(0, len(arr), 2):
        total += arr[i]
    return total

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = sum_everyother(num)
print(total)
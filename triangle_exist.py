list1 = [4,5,6]
triangle = True
for k in list1:
    if (sum(list1)-k) <= k:
        triangle = False
        break
print(triangle)
number = int(input("Введите число: "))

mlist = [0] * 10
while number>0:
    digit=number%10
    for k in range(len(mlist)):
        if digit == k:
            mlist[k] += 1
    number=number//10

for k in range(len(mlist)):
    if mlist[k]!=0:
        print(k, ": ", mlist[k])
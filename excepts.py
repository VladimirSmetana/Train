try:
    a = int(input("first:"))
    b = int(input("second:"))

    if a==b:
        res = str(a)+"="+str(b)
    else:
        res = (str(a) + ">" + str(b)) if a>b else (str(a) + "<" + str(b))
    print(res)
except ValueError:
    print("V!")
except TypeError:
    print("T!")
except SyntaxError:
    print("S!")
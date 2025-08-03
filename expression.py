# Ax = B - A -1
try:
    A = float(input("Введите А:"))
    B = float(input("Введите В:"))

    flr = 0.001

    x = 0
    if A!=0:
        x = (B-1)/A - 1
        print(x)
    elif A==0 and B==1:
        print("any")

    elif A==0 and B!=1:
        print("no solve")
    else:
        print("U!")
        raise SystemExit(0)
except ValueError:
    print("V!")
except TypeError:
    print("T!")
except SyntaxError:
    print("S!")
except NameError:
    print("N!")
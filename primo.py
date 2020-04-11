x = int(input())
v = True
if x > 2:
    for i in range (2, x):
        if (x % i) == 0:
            v = False
if v == True:
    print(x, "es primo")
else:
    print(x, "no es primo")

x = 0
y = 10

if (x<=10):
    for i in range(1, y-x+1):
        print(" "*(y-i),("*") * (i * 2 - 1))
    x=x+1

import random
x = random.sample('0123456789',4)
print(x)

a = 0
b = 0
while a != 4:
    a = 0
    b = 0
    y = list(input())
    if (len(y) != 4) | (len(y) != len(set(y))):
        print("Wrong input")
    for i in range(len(y)):
        if y[i] in x:
            if y[i] == x[i]:
                a += 1
            else:
                b += 1
    if a == 4:
        print("%d A %d B" % (a, b))
        print("Correct!! You are excellent!!")
    else:
        print("%d A %d B" % (a, b))
        print("Try again!")

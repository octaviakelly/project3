def fibfunc(num):
    num1 = 0
    num2 = 1
    num3 = 0
    val = 0

    for i in range(2, num + 1):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        val = num3
        yield (val)


x = [0, 1]
num=8
y = list(fibfunc(num-1))
z = x + y
print(z)
a = len(z)
for i in range(a-1):
    print(str(z[i]) + ",", end="")
print(z[-1])
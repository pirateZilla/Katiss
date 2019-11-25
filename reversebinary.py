
x = int(input())
y = "{0:b}".format(x)
y = y[::-1]
z = int(y, 2)
print(z)	
import sys

for line in sys.stdin:
	a = line.split()
	x = int(a[0])
	y = int(a[1])
	z = int(a[2])
	for k in range(1, z+1):
		if k % x == 0 and k % y == 0:
			print("FizzBuzz")
			continue
		elif k % x == 0:
			print("Fizz")
			continue
		elif k % y == 0:
			print("Buzz")
			continue
		print(k)

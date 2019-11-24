import sys

test_case = 0
output = "null"

for i in sys.stdin:
	if test_case == 0:
		test_case = i
	else:
		r, e, c = [int(q) for q in input().split()]
		if e-c == r:
			output == "does not matter"
		elif e-c > r:
			output == "advertise"
		else:
			output == "do not advertise"
		print(output)

import math

n, w, h = [int(q) for q in input().split()]
hyp = math.sqrt(w*w + h*h)

for i in range(n):
	if int(input()) > hyp:
		print("NE")
	else:
		print("DA")

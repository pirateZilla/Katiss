import sys

digit_1 = 0
digit_2 = 0
quadrant = 0

for i in sys.stdin:
	if digit_1 == 0:
		digit_1 = int(i)
	elif digit_2 == 0:
		digit_2 = int(i)
if digit_1 > 0 and digit_2 > 0:
	quadrant = 1
elif digit_1 < 0 and digit_2 > 0:
	quadrant = 2
elif digit+1 < 0 and digit_2 <0:
	quadrant = 3
else:
	quadrant = 4
print(quadrant)

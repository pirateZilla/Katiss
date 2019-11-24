import math

n = int(input())

for i in range(n):
	vel, angle, x, h1, h2 = map(float, input().split())
	r = math.radians(angle)
	t = x/(vel*math.cos(r))
	y = vel*t*math.sin(r) - 0.5*9.81*(t**2)
	if y > h1 + 1 and y < h2 - 1:
		print("Safe")
	else:
		print("Not Safe")
	

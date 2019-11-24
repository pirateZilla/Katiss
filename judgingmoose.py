r, l = map(int, input().split())

if r == l:
	if r ==0:
		print("Not a moose")
	else:
		print(f"Even {r*2}")
else:
	print(f"Odd {max(r, l)*2}")
	

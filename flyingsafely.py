N = int(input()) #number of test cases

for i in range(N): # cycle through number of test cases
	n, m = list(map(int, input().split())) # define number of cities and pilots
	for j in range(m): # cycle through each pilot's flights
		a, b = list(map(int, input().split()))
	print(n - 1) # seems like an imperfect hack solution - please let me know if you find something better

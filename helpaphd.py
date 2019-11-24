n = int(input())

for i in range(n):
	data = input().split("+")
	if data[0] == "P=NP":
		print("skipped")
	else:
		print(int(data[0]) + int(data[1]))

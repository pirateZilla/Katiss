gunnar = list(map(int, input().split()))
emma = list(map(int, input().split()))

if sum(emma) > sum(gunnar):
	print("Emma")
elif sum(gunnar) > sum(emma):
	print("Gunnar")
else:
	print("Tie")


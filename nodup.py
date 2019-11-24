import sys
data = input().split()
check = []
ans = "yes"
for i in data:
	if i not in check:
		check.append(i)
	else:
		ans = "no"
print(ans)

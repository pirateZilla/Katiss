results = []
k = 1
for i in range(5):
	string = input()
	if "FBI" in string:
		results.append(k)
	k = k + 1
	
ans = ' '.join(str(e) for e in results)
if ans == '':
	print("HE GOT AWAY!")
else:
	print(ans)

import math

N = int(input())
answers = input()

a = ("ABC" * math.ceil(N/3))[:N]
b = ("BABC" * math.ceil(N/4))[:N]
g = ("CCAABB" * math.ceil(N/6))[:N]

correct_ans = { "Adrian": 0, "Bruno": 0, "Goran": 0}

for i in range(N):
	if a[i] == answers[i]:
		correct_ans["Adrian"] += 1
	if b[i] == answers[i]:
		correct_ans["Bruno"] += 1
	if g[i] == answers[i]:
		correct_ans["Goran"] += 1
print(max(correct_ans.values()))
for name, score in correct_ans.items():
	if score == max(correct_ans.values()):
		print(name)

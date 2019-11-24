scores = []
for i in range(5):
	data = list(map(int, input().split()))
	scores.append(sum(data))
	
winner_score = max(scores)
winner = scores.index(winner_score) + 1
print(winner, winner_score)
	


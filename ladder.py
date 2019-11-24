import math

h, v = map(int, input().split())
r = math.radians(v)
hyp = h/math.sin(r)

print(math.ceil(hyp))

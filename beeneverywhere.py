import sys

test_case = 0
cities = 0
cities_list = []
for i in sys.stdin:
	input_data = i
	if test_case == 0:
		test_case = int(input_data)
	elif cities == 0:
		cities = int(input_data)
	else:
		if input_data not in cities_list:
			cities_list.append(input_data)
		cities = cities - 1
		if cities == 0:
			print(len(cities_list))
			test_case = test_case - 1
			cities_list = []
			if test_case ==0:
				exit()

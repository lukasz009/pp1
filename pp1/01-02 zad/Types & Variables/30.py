table = [12, 6, 4, 9, 3]
for item in table:
	counter = ''
	for x in range(item):
		counter += '*'
	print(str(item) + ": " + counter + "\n")
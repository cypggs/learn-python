try:
	data = open('sketch.txt')

	for each in data:
		try:
			(role, line) = each.split(':', 1)
			print(role, end='')
			print(' said: ', end='')
			print(line, end='')
		except ValueError:
			pass
		
	data.close()
except IOError:
	print('The data file is missing!')
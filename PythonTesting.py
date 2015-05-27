rows = height = 3
cols = width = 5
array2d = [[1,2,3,4,5],
		   [5,6,7,8,9],
		   [6,3,4,5,2]]

tupleTest = (1, 2)

def searchAtl(arr2d, x, y):
	if (x == (rows - 1) or y == (cols - 1)):
		return True

	if (arr2d[x][y] >= arr2d[x+1][y]):
		if searchAtl(arr2d, x+1, y):
			return True
	
	if (arr2d[x][y] >= arr2d[x][y+1]):
		if searchAtl(arr2d, x, y+1):
			return True

	return None

def searchPac(arr2d, x, y):
	if (x == 0 or y == 0):
		return True

	if (arr2d[x][y] >= arr2d[x-1][y]):
		if searchPac(arr2d, x-1, y):
			return True

	if (arr2d[x][y] >= arr2d[x][y-1]):
		if searchPac(arr2d, x, y-1):
			return True

	return None

def run(arr2d):
 	runOffCells = []
	for row in xrange(rows):
		for col in xrange(cols):
			if searchPac(arr2d, row, col) and searchAtl(arr2d, row, col):
				#Notes appending to list - syntax for Python
				runOffCells.append((row, col))

	return runOffCells

# Using main but you can really just do stuff after function
def main():
	print run(array2d)

if __name__ == '__main__':
    main()
# For parsing cmd line args
# import sys
# print sys.argv

# Having object is unecessary but good for reference of inheritance
class browserHistory(object):

	# Init the self.hist object
	def __init__(self, hist = None):
		if hist is None:
			self.hist = []

	# Add url to the history: O(n)
	# Could make O(1) by adding to back but then would have to add a reverse to retrive URL
	def addUrl(self, url):
		if not type(url) == str: raise AssertionError
		self.hist.insert(0, url)
		return None

	# Retrieve the url from the history: O(n)
	# Could reverse list for faster addUrl so O(n) + O(n)
	# I find this more readable however
	def retrieveUrl(self, n):
		if not n >= 0: raise AssertionError
		tempDict = {}
		retList = []
		lenOfList = len(self.hist)
		# Loop over range n times
		for i in range(n):
			if i >= lenOfList:
				break
			tempUrl = self.hist[i]
			# Check in O(1) time whether we already have tempUrl
			if not tempDict.get(tempUrl):
				retList.append(tempUrl)
				tempDict[tempUrl] = True
		return retList

# Using main but you can really just do stuff after function
def main():
	myHistory = browserHistory()
	while True:
		try:
			myHistory.addUrl(raw_input('> '))
		except EOFError:
			print
			break

	print myHistory.retrieveUrl(int(raw_input('Retrieve? ')))
   
if __name__ == '__main__':
    main()
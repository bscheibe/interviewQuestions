# For parsing cmd line args
# import sys
# print sys.argv

class browserHistory(object):

	# Init the self.hist object
	def __init__(self, hist = None):
		if hist is None:
			self.hist = []

	# Add url to the history
	def addUrl(self, url):
		if not type(url) == str: raise AssertionError
		self.hist.insert(0, url)
		return None

	# Retrieve the url from the history
	def retrieveUrl(self, n):
		if not n >= 0: raise AssertionError
		tempDict = {}
		retList = []
		lenOfList = len(self.hist)
		for i in range(n):
			if i >= lenOfList:
				break
			tempUrl = self.hist[i]
			if not tempDict.get(tempUrl):
				print tempUrl
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
			print '\n'
			break

	print myHistory.retrieveUrl(int(raw_input('Retrieve? ')))
   
if __name__ == '__main__':
    main()
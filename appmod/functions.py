import requests
import json

class getC19:
		def __init__(self):
			self.states()
			return

		def states(self):
			url = "https://covid19-india-adhikansh.herokuapp.com/states"
			self.data = requests.get(url)
			self.data = self.data.text
			self.data = json.loads(self.data)
			self.data = self.data["state"]
			self.statenames = [ i['name'] for i in self.data ]
			return

		def stateData(self,name):
			name = name.title()
			if name in self.statenames:
					indx = self.statenames.index(name)
			else:
					indx = 0
			return self.data[indx]
			

def mainf():
	get1 = getC19()
	kardat = get1.stateData(get1.statenames[0])
	print(kardat)
if __name__ == "__main__" :
		mainf();

from . import webscrapping

# data is dictionary of satename and data as tuple
# ex: { "StateName1": (ActiveCount, Total, Cured, Deaths), 
#       "StateName2": (ActiveCount, Total, Cured, Deaths) ... }

class getC19:
		def __init__(self):
			self.states()
			return

		def states(self):
			url = "https://covid19-india-adhikansh.herokuapp.com/states"
			self.data = webscrapping.scrapeWeb()
			self.statenames = list( self.data.keys() )

		def stateData(self,name):
			if name in self.statenames:
					return self.data[name]
			else:
					return (0, 0, 0, 0)

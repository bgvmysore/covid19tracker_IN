from bs4 import BeautifulSoup as bs
import requests

# making GET request from target site
def scrapeWeb():
	websiteURL = "https://www.mygov.in/corona-data/covid19-statewise-status"
	responseObj = requests.get(websiteURL)

	# parse html from response and store as bs obj
	soupObj = bs(responseObj.text, 'html.parser')

	# 3 to 39 states
	data = [list(map((lambda x: x.text), 
				  soupObj.find_all(class_="content")[i].find_all(class_="field-item")[0:4]))
			for i in range(3,39)]
	
	for i in data:
		tmp = int(i[1]) - int(i[2]) - int(i[3])
		i = i.insert(1, str(tmp))
	data = list(map(tuple, data))
	
	# statename : (active, total, cured, dead)
	data = dict(map((lambda x: (x[0], x[1:])), data))
	return data
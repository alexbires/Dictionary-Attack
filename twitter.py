import urllib
import json
#interface
#spider user
#creates a "web" of different users probably a list at the moment
def spider_user(screen_name):
	url = "http://"
	pass

def friends(person,limit = 500):
	url = "http://search.twitter.com/search.json?"
	url = url + "screen_name=" + person
	results = urllib.urlopen(url)
	#results = json.load(results)
	print results.readlines()
	pass

friends("dc404")

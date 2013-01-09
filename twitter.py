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
def parseTwitter(user):
	"""
	This method is being split up later on but for the moment it is being used
	to scrape tweets from specific usernames and find words that would be good
	candidates for the custom dictionary.
	"""
	url="http://search.twitter.com/search.json?q=%40"
	url = url + user
	results = urllib.urlopen(url)
	results = json.load(results)
	iterator = iter(results)
	switch_dict = {"completed_in":compl,
				   "max_id_str":max_str,
				   "since_id_str":since_str,
				   "page":page,
				   "since_id":since,}
	for i in iterator:
		try:
			if i == "results":
				result(results[i])
			else:
				switch_dict[i]()
		except KeyError:
			pass
		except TypeError:
			pass

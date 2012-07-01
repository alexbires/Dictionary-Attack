import urllib, sys, os, string
import argparse
import json
# sys.argv[1] is the domain
# sys.argv[2] is the relative path name of cewl.rb
# sys.argv[3...] previously existing password list(s) -- preferably unmutated

# diggity the website's name
m=False
end=False
s=False
sub_list = dict()

def parseSubstitution(sub_string):
	"""
	Takes in a string and creates a dictionary to keep track of the mappings
	that the user specifies.  It returns a dictionary of translations
	"""
	begin=0
	second=False
	replace=None
	sub_list
	for i in range(len(sub_string)):
		if sub_string[i]==":" and second==False:
			replace = sub_string[begin:i]
			begin = i+1
			second=True
		elif second:
			if sub_string[i]=='\n':
				rep_with = sub_string[begin:i]
				second=False
				begin = i+1
				sub_list[replace]=rep_with
	return sub_list

def mutateWord(word,fileDict,end=False):
	"""
	This method takes in a single word as a string and mutates it according
	to the dictionary global dictionary that has been populated in a previous 
	method. Adds to the file that is getting saved to.
	"""
	files = open(fileDict,'w')
	iterate = iter(sub_list)
	for x in iterate:
		before = word
		word=word.replace(x,sub_list[x])
		tofile = word+"\n"
		if (not before is word) and not end:
			try:
				files.write(tofile)
			except IOError:
				pass
	if end:
		files.write(word + "\n")
	files.close()

def interactive():
	"""
	This method guides the user through all of the options that this program
	has.  This is going to be put on the backburner until at least the twitter
	part is done with.
	"""
	print "Do you have a base dictionary already? [Y/n]"
	has_dict = raw_input()
	if (has_dict == "yes"):
		print "Enter in a file name"
		raw_file = raw_input()
	print "Do you have a file of substitions? [Y/n]"
	has_sub_file = raw_input()
	if(has_sub_file == "yes"):
		pass

"""methods for parsing through the twitter json object"""
def lang():
	print ""
def user_name():
	pass
def compl():
	pass
def max_str():
	pass
def since_str():
	pass
def page():
	pass
def since():
	pass
def result(intake):
	s_dict={"iso_language_code":lang,
			"to_user_name":user_name,}
	print intake
	for x in intake:
		x_iter = iter(x)
		for i in x_iter:
			print i
			s_dict[i]()

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

#parseTwitter("_teresahu")
parseTwitter("HuskyStarcraft")

def main():
	parser = argparse.ArgumentParser()
	verbinteract = parser.add_mutually_exclusive_group()
	parser.add_argument("-m","--mutate",
		help="mutate the word list",action="store_true")
	parser.add_argument("-s","--substitute",
		help="specifies a file of mutations",action="store_true")
	parser.add_argument("subfiles",nargs='?',
		type=argparse.FileType('r'))
	parser.add_argument("-e","--end",
		help="only add the end result of mutations to the dictionary",
		action="store_true")
	verbinteract.add_argument("-v","--verbose",
		help="display verbose output",action="store_true")
	verbinteract.add_argument("-i","--interactive",
		help="interactive mode", action="store_true")
	arguments = parser.parse_args()
	if arguments.mutate:
		m=True
	if arguments.end:
		end = True
	subs = arguments.subfiles.name
	file=open(subs)
	garbage = file.read()
	parseSubstitution(garbage)
	file.close()
	if arguments.interactive:
		interactive()
	#if argv
	os.system("./" + sys.argv[2] + " " + sys.argv[1] + " -d 1 -w tmp.txt") 

#main()
#mutateWord("sponglea","dict.txt")
#main()
def runCewl():
	print "cewl beginning."
	#fires off cewl
	os.system("./" + sys.argv[2] + " " + sys.argv[1] + " -d 1 -w tmp.txt") 
	print "cewl finished."
	cmd = "cat tmp.txt "
	for x in range(4,len(sys.argv)):
		cmd += sys.argv[x] + " "
	os.system(cmd + "> pass.txt")
def mutate():
	print "Mutations started."
	f = open("pass.txt","r") 
	words = f.readlines()
	f.close()
	print "File read."
	print str(len(words)) + " words from scrapping."
	out = words[:]
	"Numbers appended."
	for word in words:
		for num in (range(0,100) + range(1900,2015)):
			out += [word[:-1] + str(num) + "\n"]
	words = out[:]
	print str(len(words)) + " words from first round mutations."
	for word in out:
		words += [string.upper(word)]
		words += [string.capitalize(word)]
	print str(len(words)) + " words from second round mutations."
	print "Writing to file."
	f = open("pass.txt","w")
	for x in words:
		f.write(x)
	f.close()

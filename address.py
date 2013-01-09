import urllib, sys, os, string
import argparse
import json
import twitter

sub_list = dict()
userlist = [] #This is for a list of users used by the spideruser method
spiderCalls = 0

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


def main():
	file=open(subs)
	garbage = file.read()
	parseSubstitution(garbage)
	file.close()

#mutateWord("sponglea","dict.txt")
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

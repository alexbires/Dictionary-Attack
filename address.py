import urllib, sys, os, string
import json

sub_list = dict()
userlist = [] #This is for a list of users used by the spideruser method
limit = 0

def parseSubstitution(sub_string):
	"""
	Takes in a string and creates a dictionary to keep track of the mappings
	that the user specifiesday 8am-5pm, Thur  It returns a dictionary of translations
	The format of the string is string:whatToReplaceWith
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

def mutateWordold(word,fileDict,end=False):
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

def mutateWord(word,step=False):
	print word
	iterator = iter(sub_list)
	for x in iterator:
		word = word.replace(x,sub_list[x])
		print word

def main():
	sub_list["o"]="derpina"
	mutateWord("hello")
	step = False
	args = sys.argv
	argLength = len(sys.argv)
	for i in range(len(sys.argv)):
		try:
			if args[i] == "-h":
				print "Address.py is made to take in a word list, do mutations on it, and then"
				print "spit you back a new word list with good possible passwords based on"
				print "the input given"
			elif args[i] == "-in":#in is the base word list
				filename = args[i]
				i+=1
				wordlist = open(args[i])
				contents = wordlist.read()
				wordlist.close()
			elif args[i] == "-m":
				mutateFile = args[i]
				i+=1
				mutations = open(args[i])
				contents = mutations.read()
				mutations.close()
			elif args[i] == "-l" or args[i] == "--limit":
				i+=1
				limit = args[i]
		except IOError:
			print "Enter a valid file"
			fileName = raw_input("Enter a valid file\n")
			print fileName
		except IndexError:
			pass#need to just end the execution
main()
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

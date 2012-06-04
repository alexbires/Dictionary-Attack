import urllib, sys, os, string
import argparse
# sys.argv[1] is the domain
# sys.argv[2] is the relative path name of cewl.rb
# sys.argv[3...] previously existing password list(s) -- preferably unmutated
# if sys.argv[-1] is -m, perform mutations on the password list

# diggity the website's name
m=False
s=False
sub_list = dict()


def parseSubstitution(sub_string):
	begin=0
	second=False
	replace=None
	rep_with=None
	for i in range(len(sub_string)):
		if sub_string[i]==":" and second==False:
			replace = sub_string[begin:i]
			begin = i+1
			second=True
		if second:
			if sub_string[i]=='\n':
				rep_with = sub_string[begin:i]
				second=False
				begin = i+1
				toAdd = (replace,rep_with)
				sub_list[replace]=rep_with
	print sub_list

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-m","--mutate",
		help="mutate the word list",action="store_true")
	parser.add_argument("-s","--substitute",
		help="specifies a file of mutations",action="store_true")
	parser.add_argument("substitutionfiles",nargs='?',
		type=argparse.FileType('r'))
	parser.add_argument("-v","--verbose",
		help="display verbose output",action="store_true")
	arguments = parser.parse_args()
	if arguments.mutate:
		m=True
	subs = arguments.substitutionfiles.name
	file=open(subs)
	garbage = file.read()
	parseSubstitution(garbage)
	file.close()
	print garbage

main()
#try:
#	page = urllib.urlopen(sys.argv[1]) # for verification
#except IOError:
#	print "herro"
#except IndexError:
#	print "index error"
#print "Site verified."
"""if sys.argv[-1] == "-m":
	m = True
	sys.argv = sys.argv[:-1]
	if v:print "Mutations enabled."
else:
	m = False
	print "Mutations disabled."
"""
def runCewl():
	print "cewl beginning."
	#fires off cewl
	os.system("./" + sys.argv[2] + " " + sys.argv[1] + " -d 1 -w tmp.txt") 
	print "cewl finished."
	cmd = "cat tmp.txt "
	for x in range(4,len(sys.argv)):
		cmd += sys.argv[x] + " "
	os.system(cmd + "> pass.txt")
	print "cat finished."
#runCewl()
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
#print "Done."

#mutate()

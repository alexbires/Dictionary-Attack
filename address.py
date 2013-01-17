import urllib, sys, os, string
import json

sub_list = dict()
limit = 0
sub_list["o"]="derpina"
sub_list["p"]="asf"

def parseSubstitution(sub_string):
	"""
	Takes in a string and creates a dictionary to keep track of the mappings
	that the user specifies It returns a dictionary of translations
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

def mutateWord(word,step=False):
	"""
	This method takes in a word and returns either one of two things
	If step is true then every step of replacing the word with substitutions
	will be returned.
	If step is false, then only the final word will be returned
	"""
	toReturn = []
	iterator = iter(sub_list)
	if step==False:
		for x in iterator:
			word = word.replace(x,sub_list[x])
		print word
		return word
	else:
		for x in iterator:
			word = word.replace(x,sub_list[x])
			toReturn.append(word)
			return toReturn

def main():
	sub_list["o"]="h"
	mutateWord("hello",False)
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
				contents = wordlist.readlines()#contents is a list
				wordlist.close()
			elif args[i] == "-m":#the mutation list to open
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

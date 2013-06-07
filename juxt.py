#!/usr/bin/python
import sys, random

# "juxtaposer" - Christopher S. Foree
# Takes a series of arguments specifying syntactic categories of English speech
# and generates a random juxtaposition of words resembling a sentence (of sorts)

word_set = []
allowed_syntactic_categories = ['adj','adv','art','nou','pre','pro','ver']

# get syntactic category sequence from command line arguements
args = sys.argv[1:]

# show help if no commang line arguments were provided
if len(args) < 1: 
  print 'USAGE: "python juxt.py ' + ' '.join(allowed_syntactic_categories) + '"'
  sys.exit()

# iterate through each command line argument, select a word at random from
# each specified syntactic category, and append it to our "sentence"
for arg in args:
  if not arg[0:3] in allowed_syntactic_categories: continue
  with open (arg[0:3], "r") as word_list: word_set.append(random.choice(word_list.read().splitlines()))

# output the result
print ' '.join(word_set)
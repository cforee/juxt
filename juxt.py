#!/usr/bin/python
import sys, random

# "juxtaposer" - Christopher S. Foree
# Takes a series of arguments specifying syntactic categories of English speech
# and generates a random juxtaposition of words resembling a sentence (of sorts)

word_set = []
allowed_syntactic_categories = ['adj','adv','art','nou','pre','pro','ver']

args = sys.argv[1:]

# show help if no commang line arguments were provided
if len(args) < 1: 
  print 'USAGE: "python juxt.py ' + ' '.join(allowed_syntactic_categories) + '"'
  sys.exit()

# iterate through each command line argument, select a word at random from
# each specified syntactic category, then append it to our "sentence"
for arg in args:
  short_arg = arg[0:3]
  word_file = './syntactic_categories/' + short_arg + '.txt'
  if not short_arg in allowed_syntactic_categories: continue
  with open (word_file, "r") as word_list: word_set.append(random.choice(word_list.read().splitlines()))

print ' '.join(word_set)
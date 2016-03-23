#!/usr/bin/python

import sys


def is_number(t):
   try:
      int(t)
      return True
   except ValueError:
      return False





#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)


if (len(sys.argv) == 1):
   print "\n  Usage: histogram.py 1 [2 3 4 5...] \n"
   exit (0)


for token in sys.argv:
   #print "Token: %s" % token 
   if (is_number(token)):
      print "* " * int(token)



print "Normal End of Program"

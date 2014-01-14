#!/usr/bin/env python

import argparse
import random
import math

def main(args):
  # Roll a die for each D value.
  for i in args.dval:
    print "%d roll: %d" % (i,int(math.ceil(random.random()*i)))
  return

if __name__ == '__main__':
  # Set up command line arguments.
  parser = argparse.ArgumentParser(description='Dice simulator.')
  parser.add_argument('dval',type=int,nargs='+',
                      help='D value to roll.')

  # Parse arguments and begin execution.
  main(parser.parse_args())


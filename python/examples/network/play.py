#!/usr/bin/env python2.7

import logging
import argparse
import random

import game

def main(args):
  # Set up logging.
  logging.basicConfig(level=args.loglevel,
                      filename=args.logfile,
                      format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',)
  logging.info(args)

  logging.info('Starting game.')
  g = game.Game(args.nodes,args.active,args.neighbours)

  for i in range(args.steps):
    logging.info('Step '+str(i))
    g.step()
    g.clear()

  # Done.
  return

if __name__ == '__main__':
  # Set up command line arguments.
  parser = argparse.ArgumentParser(description='Example template multithreaded Python application.')
  parser.add_argument('--debug',dest='loglevel',action='store_const',const=logging.DEBUG,default=logging.INFO,
                      help='Set logging level to debug.')
  parser.add_argument('--logfile',type=str,default='example.log',
                      help='File in which to store log output. Default: example.log')

  parser.add_argument('nodes',type=int,help='Number of nodes to use.')
  parser.add_argument('active',type=float,help='Fraction of nodes that are active (0.0-1.0)')
  parser.add_argument('neighbours',type=int,help='Number of neighbours to use.')
  parser.add_argument('steps',type=int,help='Number of steps to take.')

  # Parse arguments and begin execution.
  main(parser.parse_args())

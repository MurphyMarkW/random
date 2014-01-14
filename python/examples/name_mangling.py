#!/usr/bin/env python

import logging
try:
  import argparse
  import random
  pass
except (ImportError),err:
  logging.error(err)
  raise

class AClass:
  def __init__(self):
    self.x = random.random()
    return

  def get_x1(self):
    return self.x

  def _get_x2(self):
    return self.x

  def __get_x3(self):
    return self.x

def main(args):
  def do_help(a):
    logging.info('Accessing help for %s...',a)
    raw_input('Enter to continue...')
    help(a)
    return

  def do_public(a):
    logging.info('Accessing help for public get_x1 for %s...',a)
    raw_input('Enter to continue...')
    help(a.get_x1)
    logging.info('Performing public get_x1 for %s...',a)
    raw_input('Enter to continue...')
    logging.info('%s',a.get_x1())
    return

  def do_private(a):
    logging.info('Accessing help for private _get_x2 for %s...',a)
    raw_input('Enter to continue...')
    help(a._get_x1)
    logging.info('Performing private _get_x2 for %s...',a)
    raw_input('Enter to continue...')
    logging.info('%s',a._get_x2())
    return

  def do_mangled(a):
    logging.info('Accessing help for mangled __get_x3 for %s...',a)
    raw_input('Enter to continue...')
    help(a.__get_x3)
    logging.info('Performing mangled _get_x3 for %s...',a)
    raw_input ('Enter to continue...')
    logging.info('%s',a.__get_x3())
    return

  logging.basicConfig(level=args.debug)
  logging.debug('%s called using arguments %s',__file__,args)

  a = AClass()
  try: do_help(a)
  except (AttributeError),err: logging.error(err)
  try: do_public(a)
  except (AttributeError),err: logging.error(err)
  try: do_private(a)
  except (AttributeError),err: logging.error(err)
  try: do_mangled(a)
  except (AttributeError),err: logging.error(err)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Name mangling examples.')
  parser.add_argument('--debug',dest='debug',action='store_const',const='DEBUG',default='INFO',
                      help='Set logging for debugging.')
  main(parser.parse_args())

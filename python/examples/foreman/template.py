#!/usr/bin/env python2

import logging

try:
  import argparse
  import threading
  import time
  pass
except (ImportError) as err:
  logging.error(err)

class Foreman:
  '''
  Foreman - Worker handler.
  '''

  def __init__(self,nthreads=1):
    '''
    Initialization method.
    '''
    self._nthreads = nthreads
    return

  def start(self):
    '''
    Start the Foreman and Workers.
    '''
    logging.debug('Foreman started.')

    # Worker queue
    wlist = []

    # Divy up workload here.
    # TODO

    # Start a worker thread, if any are available. Otherwise, wait.
    # This should be in a loop structure, going over all the units of available work.
    while threading.active_count() > self._nthreads: time.sleep(1)
    wlist.append(Worker())
    logging.debug('Starting thread: '+str(wlist[-1].ident))
    wlist[-1].start()

    # Wait for all workers to terminate.
    for worker in wlist: worker.join()

    # Recombine output here.
    # TODO

    return

class Worker(threading.Thread):
  '''
  Worker thread.
  '''

  def __init__(self):
    '''
    Initialization method.
    '''
    threading.Thread.__init__(self)
    return

  def run(self):
    '''
    Run the Worker.
    '''
    # Do work here.
    # TODO

    # Finished.
    logging.debug('Thread complete: '+str(self.ident))
    return

def main(args):
  # Set up logging.
  logging.basicConfig(level=args.loglevel,
                      filename=args.logfile,
                      format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',)
  logging.debug(args)

  # Instantiate the Foreman and start the workers.
  foreman = Foreman(nthreads=args.nthreads)
  foreman.start()

  # Done.
  return

if __name__ == '__main__':
  # Set up command line arguments.
  parser = argparse.ArgumentParser(description='Example template multithreaded Python application.')
  parser.add_argument('--debug',dest='loglevel',action='store_const',const=logging.DEBUG,default=logging.INFO,
                      help='Set logging level to debug.')
  parser.add_argument('--logfile',type=str,default='example.log',
                      help='File in which to store log output. Default: example.log')

  parser.add_argument('--nthreads',type=int,default=1,help='Number of threads to use.')

  # Parse arguments and begin execution.
  main(parser.parse_args())

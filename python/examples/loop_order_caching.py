#!/usr/bin/env python

import logging

try:
    import random
    import argparse
    import time
    from inspect import stack
    pass
except (ImportError),err:
    logging.error('required modules unavailable')
    raise

def mat(size):
    '''
    Creates a simple square matrix where each element is the row multiplied by the column.
    '''
    m = []
    for i in xrange(size):
        m.append([])
        for j in xrange(size):
            m[-1].append(float(j*i))
    return m

def multij(m):
    '''
    Go through the rows first, columns second.
    '''
    for i in xrange(len(m)):
        for j in xrange(len(m[i])):
            m[i][j] += random.random()
    return

def multji(m):
    '''
    Go through the columns first, rows second.
    '''
    for i in xrange(len(m)):
        for j in xrange(len(m[i])):
            m[j][i] += random.random()
    return

class timer:
    '''
    Just a cheap-o stop-watch timer class.
    '''
    def __init__(self):
        self.on = False
        self.t = 0.0
        return
    def start(self):
        self.on = True
        self.start = float(time.time())
        return
    def stop(self):
        if self.on:
            self.on = False
            self.stop = float(time.time())
            self.t += self.stop-self.start
        return
    def time(self):
        return self.t

def main(args):
    '''
    Simple example of how code structure can affect execution time.
    '''
    try: logging.basicConfig(filename=args.logname[0],level=args.loglevel[0])
    except (TypeError,AttributeError),err: logging.basicConfig(level=args.loglevel[0])

    # Startup information
    print '''
    The following is an example of the differences in execution time that may result
    from improper ordering of looping structures. For increasingly larger sizes of data,
    reversal of even two-dimensional looping may result in significantly different
    timings. This difference in execution time is a direct result of misuse of the caching
    scheme implemented in modern CPU architectures, and is independent of programming
    language - this is a misuse of hardware, not software! For illustration purposes, it
    is suggested to provide a dimensionality of 1000 to 5000.
    '''

    # What is the internal data we will be using
    print 'For this example, we will be using a square matrix.'
    print 'Internally, we will represent the matrix as m[x][y].\n'
    dim = input('Please specify the size of the dimensions of the two-dimensional list: ')
    print 'Please wait while I set up the matrix...'
    m = mat(dim)
    print

    # First loop
    print '''For the first pass over the matrix, we will be looping in the following manner:
    m[x][y]
    for i in 0...{}:
      for j in 0...{}:
        m[i][j] += random()
    '''.format(dim,dim)
    raw_input('Press enter to continue...')
    t = timer()
    t.start()
    multij(m)
    t.stop()
    print 'Finished. Time elapsed: {}s'.format(t.time())
    raw_input('Press enter to continue...')
    print

    print 'Please wait while I reset the matrix...'
    m = mat(dim)
    print

    # Second loop
    print '''For the second pass over the matrix, we will be looping in the following manner:
    m[x][y]
    for j in 0...{}:
      for i in 0...{}:
        m[i][j] += random()
    '''.format(dim,dim)
    raw_input('Press enter to continue...')
    t = timer()
    t.start()
    multji(m)
    t.stop()
    print 'Finished. Time elapsed: {}s'.format(t.time())

    # Done
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Quickie one-shot code optimization example.')
    parser.add_argument('--log',dest='logname',nargs=1,type=str,
                        help='Name of log file to use.')
    parser.add_argument('--debug',dest='loglevel',action='store_const',
                        const=['DEBUG'],default=['INFO'],help='Enable debug logging.')
    args = parser.parse_args()
    main(args)


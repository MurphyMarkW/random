import logging
import argparse

class Test(object):
  @property
  def var(self):
    print 'Property called.'
    return self.var

  @var.getter
  def var(self):
    print 'Getter called.'
    return self.var

  @var.setter
  def var(self,val):
    print 'Setter called.'
    self.var = val

_encoding = {
  0:'0',
  1:'1',
  2:'2',
  3:'3',
  4:'4',
  5:'5',
  6:'6',
  7:'7',
  8:'8',
  9:'9',
  10:'A',
  11:'B',
  12:'C',
  13:'D',
  14:'E',
  15:'F',
}

def Rebase(num,base):
  '''
  Rebase num to base.
  '''
  if num < 0: raise ValueError('num must be greater than 0')
  if base <= 1: raise ValueError('base must be greater than 2')

  if not num: return '0'
  return (Rebase(num/base,base)+_encoding[num%base]).lstrip('0')

def Fibb(n):
  if n == 0: return 0
  if n == 1: return 1
  return Fibb(n-1) + Fibb(n-2)

def FizzBuzz(n):
  for i in [x+1 for x in xrange(n)][::-1]:
    if not (i%3 or i%5):
      print i,'FizzBuzz'
    elif not i%3:
      print i,'Fizz'
    elif not i%5:
      print i,'Buzz'
    else:
      print i
  return

def main(args):
  print Rebase(args.n,args.base)
  #print Fibb(args.n)
  #FizzBuzz(args.n)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A node system.')
    parser.add_argument('--debug',action='store_const',const=logging.DEBUG,default=logging.INFO,
                        help='Enable debugging.')
    parser.add_argument('--logfile',nargs=1,type=str,default='node.log',
                        help='File to which logs will be appended.')
    parser.add_argument('n',type=int,
                        help='Number of nodes to use.')
    parser.add_argument('base',type=int,
                        help='Base in which to represent n.')
    main(parser.parse_args())

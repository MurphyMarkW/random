#!/usr/bin/env python

def Paired(a,x):
  values = set(a)
  for i in values:
    if x-i in values: return i,x-i
  return None

if __name__ == '__main__':
  print Paired([5,2,3,4,5],10)

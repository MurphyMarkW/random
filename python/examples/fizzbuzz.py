#!/usr/bin/env python

def _fizz(n):
  if not n%3: return 'Fizz'
  return ''

def _buzz(n):
  if not n%5: return 'Buzz'
  return ''

def FizzBuzz(n):
  if n-1: FizzBuzz(n-1)
  print _fizz(n)+_buzz(n) or n

if __name__ == '__main__':
  FizzBuzz(100)

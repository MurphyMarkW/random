#!/usr/bin/env python

# Make self-sorting (monotonically increasing) Linked List out of Node
# Should contain insert and print functionality

class Node(object):
  def __init__(self,val):
    self.val = val
    self.nxt = None

class List(object):

  def __init__(self,n=None):
    self.cur = n

  def insert(self,val):
    if not self.cur or self.cur.val >= val:
      node = Node(val)
      node.nxt = self.cur
      self.cur = node
    else:
      subl = List(self.cur.nxt)
      subl.insert(val)
      self.cur.nxt = subl.cur

  def __str__(self):
    if self.cur: return str(self.cur.val) + ',' + str(List(self.cur.nxt))
    else: return ''

l = List()
l.insert(5)
l.insert(3)
l.insert(7)
print l

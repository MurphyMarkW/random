import uuid
import random

import node
import network

class Game:
  def __init__(self,size=1,active=0.0,neighbours=0):
    if size < 1:
      raise ValueError('size of the game must be greater than 0')
    self.size = size

    if active < 0.0 or active > 1.0:
      raise ValueError('active must be in the range [0.0,1.0]')
    self.active = active

    if neighbours < 0 or neighbours > size:
      raise ValueError('neighbours must be in the range [0,size]')
    self.neighbours = neighbours

    self.act = set()
    self.net = network.Network()

    for i in range(self.size):
      self.net.add(node.Node())
    for i in random.sample(self.net.nodes(), int(self.active * self.size)):
      self.act.add(i)

  def step(self):
    self.buildNeighbours();
    self.buildOpinions();

  def buildNeighbours(self):
    for n in self.act:
      for o in random.sample(self.net.nodes(),self.neighbours):
        self.net.connect(n,o)
      while len(self.net[n]) < self.neighbours:
        self.net.connect(n,random.sample(self.net.nodes(),1)[0])

  def buildOpinions(self):
    # TODO Finish this...
    self.opinions = {}
    opcount = 0;
    while len(self.opinions) != 1 or self.opinions.items()[0][0] != len(self.net):
      n = random.choice(self.net.nodes())
      o = random.choice(list(self.net[n]))
      
      try: self.opinions[o.opinion] -= 1
      
      try:
        self.opinions[n.opinion] -= 1
        o.opinion = n.opinion
        self.opinions[n.opinion] += 1
      except (AttributeError):
        n.opinion = opcount;
        o.opinion = opcount;
        self.opinions[n.opinion] = 2
        opcount += 1

  def clear(self):
    self.net.clear()

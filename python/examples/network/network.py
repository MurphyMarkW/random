import uuid

class Network:
  def __init__(self):
    self._network = {}

  def add(self,node):
    self._network[node] = set()

  def remove(self,node):
    for n in self._network[node]:
      self._network[n].remove(node)
    del self._network[node]

  def connect(self,n1,n2):
    if n1 == n2: return
    self._network[n1].add(n2)
    self._network[n2].add(n1)

  def disconnect(self,n1,n2):
    self._network[n1].remove(n2)
    self._network[n2].remove(n1)

  def clear(self):
    for n in self._network:
      self._network[n] = set()

  def nodes(self):
    return self._network.keys()

  def __len__(self):
    return len(self._network)

  def __getitem__(self,node):
    return self._network[node]

  def __str__(self):
    return 'Node id: '+str(self._network.__repr__())

  def __repr__(self):
    return self._network.__repr__()


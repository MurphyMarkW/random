import uuid

class Node:
  def __init__(self):
    self.id = uuid.uuid4()

  def __hash__(self):
    return int(self.id)

  def __eq__(self,other):
    return self.id == other.id

  def __repr__(self):
    return str(self.id)


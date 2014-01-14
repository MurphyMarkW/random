#!/usr/bin/env python3

class Test(object):
  @property
  def var(self):
    print('Property called.')
    return self._var

  @var.getter
  def var(self):
    print('Getter called.')
    return self._var

  @var.setter
  def var(self,val):
    print('Setter called.')
    self._var = val

  @var.deleter
  def var(self):
    print('Deleter called.')
    del self._var

if __name__ == '__main__':
  t = Test()
  t.var = 5
  print(t.var)
  del t.var

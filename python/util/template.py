import string
import collections

class Template(collections.MutableMapping):
  '''
  Template string wrapper.
  Acts like a dictionary.
  String conversions return a template string substitution.
  '''
  def __init__(self,template='',*args,**kwargs):
    # Set up the substitution and template string storage.
    self.subs     = dict()
    self.template = template
    # Update the substitution list with anything passed.
    self.update(dict(*args,**kwargs))

  def __getitem__(self,key):
    return self.subs[key]

  def __setitem__(self,key,val):
    self.subs[key] = val

  def __delitem__(self,key):
    del self.subs[key]

  def __iter__(self):
    return iter(self.subs)

  def __len__(self):
    return len(self.subs)

  def __str__(self):
    return str(string.Template(self.template).safe_substitute(self.subs))

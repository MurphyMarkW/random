class Index:
  '''
  Index - key-protected dictionary
  Behaves as a dictionary without the ability to add or remove new keys.
  '''

  def __init__(self,d):
    '''
    Instantiates Index from a shallow copy of a dict-like structure.
    '''
    self.__dict__['_index'] = d.copy()

  # Override __setitem__ method to disallow creation of new keys
  def __setitem__(self,key,value):
    '''
    Assigns value to key.
    Raises key error if key does not exist.
    '''
    if key in self._index: self._index[key] = value
    else: raise KeyError(key)

  # Override __delitem__ method to disallow removal of keys
  def __delitem__(self,key):
    '''
    Assigns None to key.
    Raises key error if key does not exist.
    '''
    if key in self._index: self._index[key] = None
    else: raise KeyError(key)

  # Delegate unknown functionality to the dict
  def __getattr__(self,attr):
    return getattr(self._index,attr)
  def __setattr__(self,attr,value):
    return setattr(self._index,attr,value)

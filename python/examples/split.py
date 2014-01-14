def nsplit(L,n):
  '''
  Splits a list in to up to n lists, maintaining order.

  Input:
    L - list-like object
    n - number of splits

  Yields:
    l - sub-list

  Raises:
    TypeError - L is not a list-like object
              - n is not an int-like object
    ValueError - n must be greater than or equal to 1
  '''
  for l in (L[i:i+n] for i in xrange(0,len(L),3)): yield l

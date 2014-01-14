#!/usr/bin/env python2

import other # Option 1: Imports other.py and creates a namespace called other.
from other import SomeFunction # Option 2: From other.py, import SomeFunction directly.
from other import * # Option 3: From other.py, import everything it contains directly.

if __name__ == '__main__':
  print other.SomeFunction(5,6) # Following option 1: Call the function within the namespace called other.
  print SomeFunction(5,6) # Following option 2: Call the function directly.
  print SomeOtherFunction(5,6) # Following option 3: Call other functions directly.

#!/usr/bin/env python3

def f():            # outer function
  b=2
  def g():        # inner function
      #nonlocal b # Without this nonlocal statement,
      b=3         # this will create a new local variable
      print(b)
  g()
  print(b)
f()

#!/usr/bin/env python3

class Counter:
  def __init__(self, start: int, step=1, stop=None):
    self.start = start
    self.step = step
    self.stop = stop
    self.position = start

  def __str__(self):
    return str(self.position)

  def do_step(self):
    if self.stop == None or self.position + self.step <= self.stop:
      self.position += self.step
      print(self)
    else:
      raise LookupError('You\'ve reached your destination')

step1 = Counter(18)
for i in range(10):
  step1.do_step()


step2 = Counter(0, 2, 8)

for i in range(5):
  step2.do_step()
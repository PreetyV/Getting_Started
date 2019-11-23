#!/usr/bin/env python
# coding: utf-8


import matplotlib.pyplot as plt
import numpy as np

def plotstart():
  X = np.arange(0,2*np.pi,0.1)
  Y = np.sin(X) #add
  Z = np.cos(X)
  b = 5 # cutoff for the tan graph. Otherwise, the y axis is much too big.
  T = [min(b, max(-b, np.tan(x))) for x in X]
  plt.plot(X,Y,X,Z,X,T)
  plt.show()

  if __name__ == '__main__':
    plotstart()

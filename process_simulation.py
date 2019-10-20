import numpy as np
import random

def process_simulator(M,S,fname):
  f = open(fname,"w")
  C = (random.randint(0,M)*4096)+2048
  L = random.randint(512,4096)
  a = 1
  for i in range(0,M):
    s1 = np.random.normal(C,S,int(0.9*L))
    C = (random.randint(0,M)*4096)+2048
    s2 = np.random.uniform(0,C,int(0.1*L))
    #f.write("0.9*L\n")
    for item in s1:
      if(item < 0):
          item = 0
      f.write(str(int(item)))
      f.write("\n")
    for item in s2:
      if(item < 0):
          item = 0
      f.write(str(int(item)))
      f.write("\n")
    a = a + 1
  f.close()

M = int(input("M = "))
S = float(input("S = "))
process_simulator(M,S,"data.txt")

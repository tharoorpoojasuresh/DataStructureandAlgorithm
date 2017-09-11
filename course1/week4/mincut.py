import math
import random
import copy
n=0
m=0
gr={}

def readfile():
 global n,m
 fp=open("KargerMinCut.txt","r")
 for l in fp:
  l=l.strip()
  e=l.split("\t")
  v1=int(e[0])
  gr[v1]={}
  for i in range(1,len(e)):
   v2=int(e[i])
   gr[v1][v2]=1
   m=m+1
 n=n+1
 
 fp.close()

def mincut(g):
 random.seed()
 while len(g) > 2:
  v1= random.choice(list(g.keys()))
  v2= random.choice(list(g[v1].keys()))
  for v in g[v2]:
    g[v].pop(v2)
    if v != v1:
     g[v][v1] = g[v].setdefault(v1, 0) + g[v2][v]
     g[v1][v] = g[v1].setdefault(v, 0) + g[v2][v]
             
   g.pop(v2)
        
        
        
  
  v1 = list(g.keys())[0]
  
  v2 = list(g[v1].keys())[0]
 
  return g[v1][v2]
 

def main():
 readfile()
 mincuts=0
 input=10000
 for j in range(input):
  graph=copy.deepcopy(gr)
  mcut = mincut(graph)
  if mincuts == 0:
   mincuts = mcut
  elif mincuts > mcut:
   mincuts = mcut
  print("KargerMinCut = ", mincuts)

if __name__=="__main__":
 main()



 






 



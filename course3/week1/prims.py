import sys
# n,m denote number of vertices and edges
n=0
m=0
gr = {}
mincost = 0
mst = []
adj = {}

def readfile():
 fp = open("edges.txt","r")
 input = fp.readline().split(" ")
 n = int(input[0])
 m = int(input[1])
 for i in range( 1, n+1):
 
       gr[i] = {}
  
 for l in fp:
  
      edge = l.split(" ")

      v1 = int(edge[0])
  
      v2 = int(edge[1])
   
      ecost = int(edge[2])
 
      gr[v1][v2] = ecost
  
      gr[v2][v1] = ecost
 
 fp.close()
 

def prims(st):
 global mincost
 adj[st] = 0

 for i in range(1, n+1):
   
     adj[i] = 999999 
 min = 999999
 for i in range(1,n+1):
  if min > adj[i] and i not in mst:
    min = near[i]
    j = i
    mincost = mincost + adj[j]
 mst.append(j)
 for i in range(1,n+1):
  if i in gr[j]:
   if adj[i] > gr[j][i] and i not in mst:
    adj[i] = gr[j][i]  

def main():
 readfile()
 prims(1)
 print("cost of Minimum Spanning Tree = ", mincost)

if __name__ == "__main__":
 main()




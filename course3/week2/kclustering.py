import sys
n = 0
edges = []
head = []

def readfile():
 fp = open("clustering1.txt","r")
 l1 = fp.readline().split("\n")
 n = int(l1)
 for l in fp:
  edge = l.split(" ")
  v1 = int(edge[0])
  v2 = int(edge[1])
  ecost = int(edge[2])
  edges.append([ecost , v1 ,v2])
 fp.close()
edges = sorted(edges)

def union(a, b):
 for i in range(1,n+1):
  if head[i] == a:
   head[i] = b
 head[a] = b
 return true

def cluster():
 for i in range(1,n+1):
  head.append(i)
 clusters = n
 i = 0
 while clusters > 4:
  ecost = edges[i][0]
  v1 = edges[i][1]
  v2 = edges[i][2]
  a = head[v1]
  b = head[v2]
  if a != b:
   if union(a, b):
    clusters = clusters - 1
  i = i + 1
  mspace = 99999999
  while (i < len(edges)):
   ecost = edges[i][0]
   v1 = edges[i][1]
   v2 = edges[i][2]
   if head[v1] != head[v2]:
    if mspace > cost:
     mspace = cost
     break
   i = i + 1
  return mspace

def main():
 readfile()
 mspace = cluster()
 print("max spacing = ", mspace)

if __name__ == "__main__":
 main()
 


 


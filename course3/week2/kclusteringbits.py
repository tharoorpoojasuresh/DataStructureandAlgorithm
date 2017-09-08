import sys
n = 0
m = 0
nodes = []
head = {}

def readfile():
 fp = open("clustering_big.txt","r")
 l1 = fp.readline().strip().split(" ")
 n = int(l1[0])
 m = int(l1[1])
 for l in fp:
  b= l.strip().split(" ")
  nodes.append("".join(b))
fp.close()

def complement(ch):

    if ch == '1':
 
       return '0'
 
    else:
     
      return '1'



def closest(node):

  
  closer = []
   
 for i in range(l):
 
       closer.append(node[:i] + complement(node[i]) + node[i+1:])
  
      for j in range(l):
     
       closer.append(node[:i] + complement(node[i]) + node[i+1:j] + complement(node[j]) + node[j+1:])

    return closer



def find(v):
 
   while parent[v] != v:
  
      v = parent[v]
  
  return v




def union(j , k):
 
   parent[k] = j


def clusterbits():
 for i in nodes:
  
   head[i] = i
    
   clusters = len(head)

  
  for i in nodes:
   
     j = find(i)
   
     for c in closest(i):
  
          if head.get(c):
  
              k = find(c)
    
            if j != k:
               
     union(j , k)
             
       clusters = clusters - 1
 return clusters

def main():
 readfile()
 c = clusterbits()
 print("clusters = ", c)
 

if __name__ == "__main__":
 main()
 
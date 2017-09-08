import heapq
import os

n = 0
w = []
tree = []

class HeapNode:
   def __init__(self, ch = None, lchild = None, rchild = None):
    self.ch = ch
    self.lchild = lchild
    self.rchild = rchild

def readfile():
 fp = open ("huffman.txt","r")
 l1 = fp.readline()
 n = int(l1)
 for i in range(1,n+1):
  w.append([0])
 i = 1
 for l in fp:
  w[i] = int(l.strip("\n")
  i = i + 1
fp.close()

def huffmantree():
 while len(tree) > 1:
 w1, n1 = heapq.heappop(tree)
 w2, n2 = heapq.heappop(tree)
 nn = HeapNode('$',n1,n2)
 heapq.heappush(tree,(w1 + w2),nn))

def traverse(rt):
 l =0
 r = 0
 if rt.lchild == None and rt.rchild == None:
  return 0
 if rt.lchild != None:
  l = traverse(rt.lchild)
 if rt.rchild != None:
  r = traverse(rt.rchild)
 return 1 + max(l , r)
 

def main():
 readfile()
for i in range(1,n+1):
 heapq.heappush(tree,(w[i],HeapNode(ch=i)))
huffmanntree()
head = heapq.heappop(tree)
root = head[1]
print(" Max length = ", traverse(root))

if __name__ == "__main__":
 main()
 
 
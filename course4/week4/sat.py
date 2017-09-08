import sys
g1 = {}
g2 = {}
n = 0
vis = {}
stack = []
c = 0
sets = {}
count = 0

def readfile():
 fp = open("2sat1.txt","r")
 l1 = fp.readline().strip()
 n = int(l1)
 for i in range(-n,n+1):
  g1[i] = []
  g2[i] = []
 for l in fp:
  edge = l.split(" ")
  v1 = int(edge[0])
  v2 = int(edge[1])
  g1[-v1].append(v2)
  g1[-v2].append(v1)
  g2[v1].append(-v2)
  g2[v2].append(-v1)
  c = c + 1
fp.close()

def depth(i,gr):
 vis[i] = 1
 for j in gr[i]:
  if vis[j] ==0:
   depth(j,gr)
 stack.extend([i])

def add(i,gr):
 vis[i] == 1
 for j in gr[i]:
  if vis[j] == 0:
   add(j,gr)
 sets[i] = count

def traverse(gr):
 for i in range(-n,n+1):
  vis[i] = 0
 for j in range(-n,n+1):
 if(vis[j] ==0 and j != 0:
 depth(j,gr)

def scc():
 for i in range(-n,n+1):
  vis[i] = 0
 while stack:
  node = stack.pop();
  if vis[node] ==0:
   count = count + 1
   add(node,gr)

def satisfy():
 for i in range(1, n+1):
  if sets[-i] == sets[i]:
   return 0
return 1

def main():
 readfile()
traverse(g1)
scc()
if satisfy():
 print("satisfiable")
else:
 print("unsatisfiable")

if __name__ == "__main__":
 main()
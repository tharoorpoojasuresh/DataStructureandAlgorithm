import sys
import resource
sys.setrecursionlimit(2 ** 20)

hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]

resource.setrlimit(resource.RLIMIT_STACK,(hardlimit,hardlimit))


gr = {}
n = 875714
vis = {}
c = 0
g2 = {}
size = []
stk = []

def readfile:
 global c
 for i in range(1,n+1):
  gr[i], g2[i] = [], []
 fp = open("scc.txt" , "r")
 for l in fp:
  e = l.split(" ")
 v1 = int(e[0])
 v2 = int(e[1])
 gr[v1].append(v2)
 g2[v2].append(v1)
 c = c+1
fp.close()

def dfs(u,graph):
 k = 1
 vis[u] = 1
for v in graph[u]:
 if vis[v] == 0:
  k = k + dfs(v,graph)
  stk.extend([u])
return k
  
def scc():
 for i in range(1,n+1):
  vis[i] == 0
 while stk:
  v = stk.pop()
  if vis[v] == 0:
   size.extend([dfs(v,g2)])

def traverse(g):
 for i in range(1,n+1):
  vis[i] = 0
 for v in range(1,n+1):
  if vis[v] == 0:
   dfs(v,g)

def main():
 readfile()
 traverse(gr)
 scc()
 print("The Strongly Connected Components in the decreasing order are)
 size.sort()
 print(size[-5:])

if __name__ == "__main__":
 main()
 

  
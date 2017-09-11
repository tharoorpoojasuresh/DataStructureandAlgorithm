n = 200
gr = {}
vis = {}
dist = {}

def readfile():
 for i in range(1,n+1):
  gr[i] = {}
 fp = open("dijkstraDate.txt", "r")
 for l in fp:
  l = l.strip()
  e = l.split("\t")
  v1 = int(e[0])
 for i in range(1,len(e)+1):
  cost = e[i].split(",")
  gr[v1][int(cost[0])] = int(cost[1])
 fp.close()

def min(dist):
 min = 1000000
 in = 0
 for i in range(1,n+1):
  if dist[i] < min and vis[i] == 0:
    min = dist[i]
    in = i
 return in


def dij(st):
 for i in range(1,n+1):
  vis[i] = 0
  dist[i] = 1000000
 edge = gr[st]
 for key in edge.keys():
  dist[key] = edge[key]
 dist[st] = 0
 vis[st] = 1
 for i in range(2,n+1):
  u = min(dist)
  vis[u] = 1
  e = gr[u]
  for v in e.keys():
   if vis[v] == 0:
    if dist[v] > dist[u] + gr[u][v]:
     dist[v] = dist[u] + gr[u][v]
 

def main():
 readfile()
 dij(1)
 print(dist)

if __name__ == "__main__":
 main()
  
  

import sys
n = 0
m = 0
gr = {}
p = []

def readfile():
 fp = open("g1.txt", "r")
 l1 = fp.readline().strip().split(" ")
 n = int(l1[0])
 m = int(l1[1])
for i in range(1,n+1):
 gr[i] = {}
 for l in fp:
 edge = fp.strip().split(" ")
 v1 = int(edge[0])
 v2 = int(edge[1])
 ecost = int(edge[2])
 gr[v1][v2] = ecost
fp.close()

def shortest():
 for i in range(1,n+1):
  p.append([0])
 for i in range(1,n+1):
  for j in range(1,n+1):
   if i == j:
    p[i].append(0)
   else:
    if i in gr and j in gr[i]:
     p[i].append(gr[i][j])
    else:
     p[i].append(999999)
 for k in range(1,n+1):
  for i in range(1,n+1):
   for j in range(1,n+1):
    p[i][j] = min(p[i][j], p[i][k] + p[k][j])

def path():
 sh = 9999999
 for i in range(1,n+1):
  for j in range(1,n+1):
   if i != j and p[i][j] < sh:
     sh = p[i][j]
 return sh


def main():
f = 0
 readfile()
 shortest()
 for i in range(1,n+1):
  if p[i][i] < 0:
   f == 1
   break
 if f == 0:
  s= path()
  print(s)
 else
  print("negative cycle")

if __name__ == "__main__":
 main()
   
 

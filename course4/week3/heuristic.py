import sys
import math
c = 0
vis = {}
cost = 0
coord = []

def readfile():
 fp = open("nn.txt", "r")
 l1 = fp.readline().strip()
 c = int(l1)
 for i in range(1,n+1):
  vis[i] = 0
 for l in fp:
  xy = l.strip().split(" ")
  x = float(xy[0])
  y = float(xy[1])
  coord.append(x,y)
fp.close()

def caldist(i, j):
 x1 = coord[i][0]
 y1 = coord[i][1]
 x2 = coord[j][0]
 y2 = coord[j][1]
 d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
return d

def htsp():
 n = 0
 curr = 1
 vis[curr] = 1
 while( n < c-1):
  min = 99999999
  next = 0
  for i in range(2,n+1):
   if vis[i] ==0:
    dist = caldist(curr, i)
    if min > dist:
     min = dist
     next = i
   vis[i] = 1
   cost = cost + min
   curr = next
   n = n + 1
 #back to first city
 cost = cost + caldist(curr,1)
 print(cost)
 

def main():
 readfile()
 htsp()

if __name__ == "__main__":
 main()
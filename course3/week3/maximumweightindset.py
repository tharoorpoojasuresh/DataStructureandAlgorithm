import sys
n = 0
weights = []

def readfile():
 fp = open("mwis.txt", "r")
 l1 = fp.readline()
 n = int(l1)
 for l in fp:
  weights.append(int(l))
fp.close()

def mwis():
 A = [0, weights[1]]
 for i in range(2, n+1):
  A.append(max(A[i-1] , A[i-2]+ weights[i]))
 i = n
 vertices = set()
 while i >= 1:
  if A[i-1] >= A[i-2] + weights[i]:
   i = i-1
  else:
   i=i-2
 return vertices

def main():
 readfile()
 vertices = mwis()
 ver = [1, 2, 3, 4, 17, 117, 517, 997]
 for v in ver:
  if v in vertices:
   print("1")
  else
   print("0")

if __name__ == "__main__":
 main()
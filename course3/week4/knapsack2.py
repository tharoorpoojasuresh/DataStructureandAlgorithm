import sys
n = 0
M = 0
weights = []
values = []
#iterations
iterprev = []
itercurr = []

def readfile():
 fp = open("knapsack1.txt","r")
 l1 = fp.readline().strip().split(" ")
 M = int(l1[0])
 n = int(l1[1])
 i = 1
for l in fp:
 obj = l.strip().split(" ")
 values[i] = int(obj[0])
 weights[i] = int(obj[1])
 i = i + 1
fp.close()

def knapsack2():
 for j in range(1,M+1):
  iterprev.append(0)
for i in range(1,n+1):
 for w in range(M+1):
  if weights[i] > w:
   itercurr.append(iterprev[w])
  else:
   itercurr.append(max(iterprev[w], values[i] + iterprev[w-weights[i]))
 iterprev = itercurr
print ("knapsack big solution = ", iterprev[M])


def main():
 readfile()
 knapsack2()

if __name__ == "__main__":
 main()

 
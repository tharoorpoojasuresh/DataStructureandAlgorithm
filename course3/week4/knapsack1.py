import sys
n = 0
M = 0
weights = []
values = []
profit = []

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

def knapsack1():
 for i in range(1,n+1):
  profit.append([0])
 for j in range(1,M+1):
  profit[0].append(0)
for i in range(1,n+1):
 for w in range(M+1):
  if weights[i] > w:
   profit[i].append(profit[i-1][w])
  else:
   profit[i].append(max(profit[i-1][w], values[i] + profit[i-1][w-weights[i]))
 print ("knapsack solution = ", profit[n][M])


def main():
 readfile()
 knapsack1()

if __name__ == "__main__":
 main()

 
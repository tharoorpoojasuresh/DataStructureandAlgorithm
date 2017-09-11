import sys
A = {}
 
def readfile():
 fp = open("input.txt", "r")
 for l in fp:
  num = int(l.rstrip("\n"))
  A[num] = 1
 fp.close()

def target(t):
 for x in A:
   y = t - x
   if y in A and y != x:
 #such that x+y=t and x!=y
     return 1
   else:
    return 0

def main():
 readfile()
 count = 0
 low = -10000
 high = 10000
 for i in range(low, high +1):
  if target(i):
   count = count + 1
 print count

if __name__ == "__main__":
 main() 
 
 

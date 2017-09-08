import heapq
n = 0
median = []
lower = []
higher = []

def readfile():
 fp = open("Median.txt","r")
 for l in fp:
  add(int(l))
 balance()
 median.append(calMedian())
 n=n+1
fp.close()

def calMedian():
 low = len(lower)
  
 high = len(higher)
    
 
 if low == high:
  
     return -lower[0]
 
 elif low < high:
   
     return higher[0]
  
 else:
    
    return -lower[0]
 

def add(num):
 if len(lower) == 0:
  heapq.heappush(lower, -num)
 elif num <= -lower[0]:
  heapq.heappush(lower, -num)
 else:
  heapq.heappush(higher, num)

def balance():
 low = len(lower)
 high = len(higher)
 if low < high and high - low >= 2:
  ele = heapq.heappop(higher)
  heapq.heappush(lower, -ele)
 elif low > high and low - high >= 2:
  ele = -heapq.heappop(lower)
  heapq.heappush(higher,ele)
 else:
  return 

def main():
 readfile()
 sum = 0
for i in range(1,n+1):
 sum = sum + int(median[i])
print ("overall median = ", sum % 10000)

if __name__ == "__main__":
 main()

A = []

count = 0




def median(low, high):
   
   mid = int((low + high)/2)
 
   x = A[low]
   y = A[mid]
   z = A[high]

   if x > y:
      
    x,y = y,x
  
   if x > z:
   
     x,z = z,x 
   if y > z:
   
     y,z = z,y 
   if A[low] == y:
   
     return low
   
   elif A[mid] == y:
   
     return mid
 
   else:
     
     return high


def partition(low, high):
  
  pivot = low
  
  i = low + 1
   
  global count
 
  for j in range(low+1, high+1):
 
       if A[j] < A[pivot]:
          
        A[i], A[j] = A[j], A[i]
       
        i = i + 1
       
        count = count + 1
 
    A[pivot], A[i-1] = A[i-1], A[pivot]
  
  return i-1


def quicksort(low, high):
  
  if low < high:
      
       pivot = median(low, high)
 
       A[low], A[pivot] = A[pivot], A[low]
 
       j = partition(low, high)
   
       quicksort(low, j-1)
     
       quicksort(j+1, high)
  

 

def readfile():

   fp = open("input.txt", "r")
 
   for l in fp:
      
     m = l.rstrip('\n')
 
     A.append(int(m))
  
  fp.close()


def main():
 
readfile()


 quicksort(0, len(A)-1) 
 print("count = ", count)

if __name__ == "__main__":
 main()
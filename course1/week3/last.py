A = []

count = 0


def quicksort(low, high):
 
   if low < high:
  
      A[low], A[high] = A[high], A[low]
     
   j = partition(low, high)
    
   quicksort(low, j-1)
 
   quicksort(j+1, high)



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

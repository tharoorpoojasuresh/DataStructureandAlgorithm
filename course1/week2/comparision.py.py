A = []

B = []

count=0


def merge( low, mid, high ):
  
  i = low
  
  j = mid + 1
  

  k = low
  
  while i <= mid and j <= high:
  
      if A[i] < A[j]:
          
        B[k] = A[i]
           
        i = i + 1
        
    
  else:
   
        count = count + mid - i + 1
  
        B[k] = A[j]
     
        j = j + 1
      
      k = k + 1 
    
  
  while i <= mid :
        
      B[k] = A[i]
      
      i = i + 1
   
      k = k + 1
  
  while j <= high:
    
      B[k] = A[j]
       
      j = j + 1
      
      k = k + 1
     
 return
 

def mergesort( low, high ):
  
  if low < high:
      
      mid = int((low + high)/2)
  
      mergesort ( low, mid )
  
      mergesort ( mid+1, high )
    
      merge ( low, mid, high)
   
 return

           
     
def readfile():
  
 fp = open("input.txt", "r")
 
 for m in fp:
 
    l = m.rstrip('\n')
   
    A.append(int(l))
    
    B.append(0)
   
 fp.close()
 


def main():
 readfile()

 n = len(A)

 mergesort( 0, n-1 )

 print("count = ",count)


if __name__ == "__main__":
 main()
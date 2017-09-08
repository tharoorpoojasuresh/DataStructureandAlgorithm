import sys
weights = []
lengths = []
n=0
diff = []
compltimes = []

def readfile():
 fp = open("jobs.txt","r")
 #first line is no. of jobs
 n = int(fp.readline().split(" "))
for i in range(1, n+1):
  
      weights.append(0)
 
      lengths.append(0)

i=1
 for l in fp:
  ln = l.split(" ")
   weights[i] = int(ln[0])
   lengths[i] = int(ln[1])
  i=i+1
fp.close()


def sortweights():
    
      
   
 for i in range(1, n+1):
 
       for j in range(i+1, n+1):
   
         if weights[i] < weights[j]:
  
              t1 = weights[i]
     
              weights[i] = weights[j]
      
              weights[j] = t1
           
              t2 = lengths[i]
             
              lengths[i] = lengths[j]
      
              lengths[j] = t2
 

def difference():
 
   
    for i in range(1, n+1):
  
      d = weights[i] - lengths[i]
    
    if d in diff:
    
        diff[d].append(i)
  
    else:
  
          diff[d] = []
     
          diff[d].append(i)
 

def order():
   

  ls = []
  
  time = 0
  
  for i in diff.keys():
  
      ls.append(int(i))
  
  ls.sort()
   
  ls.reverse()
 
  for i in range(1, n+1):
 
       compltimes.append(0)
  
  
 for d in ls:
    
    
    for job in diff[d]:
  
          time = time + lengths[job]
  
          compltimes[job] = time
            
  

 
def main():
 readfile()
 sortweights()
 difference()
 order()
 sumweighted = 0
  
 for i in range(1, n+1):
 
       sumweighted = sumweighted + ( compltimes[i] * weights[i])
   
  print("Sum of weighted completion times = ", sumweighted)

if __name__ == "__main__":
 main()



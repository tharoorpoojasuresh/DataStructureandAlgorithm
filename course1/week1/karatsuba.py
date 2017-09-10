

import math

def karatsuba(x, y, n):
 
   n1 = int(n / 2)

   if n1 == 1:
  
      return x * y
 
   a = int(x / (10 ** n1))
 
   b = int(x - (a *(10 ** n1)))
  
   c = int(y / (10 ** n1))
   
   d = int(y - (c *(10 ** n1)))
   
   ac = karatsuba(a, c, n1)
   
   ad = karatsuba(a, d, n1)
    
   bc = karatsuba(b, c, n1)
  
   bd = karatsuba(b, d, n1)
   

   return int((ac*(10 ** n1)) + ((10 ** (n1))*(ad + bc)) + bd)
  


print(int(karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627, 64)))


class OverloadDemo:

   def multiply(self,a,b):
       print(a*b)

   def multiply(self,a,b,c):
       print(a*b*c)


mul = OverloadDemo()
mul.multiply(5,10)
mul.multiply(2,3,4)
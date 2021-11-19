import math
n=int(input())
q=math.sqrt(n)
if int(q+0.5)**2==n:
 print("perfect square")
else:
 print("not perfect square")
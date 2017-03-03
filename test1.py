import math
import numpy as np
from numpy import *
def perp( a ) :
    b = empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

# line segment a given by endpoints a1, a2
# line segment b given by endpoints b1, b2
# return 
def seg_intersect(a1,a2, b1,b2) :
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = perp(da)
    denom = dot( dap, db)
    num = dot( dap, dp )
    return (num / denom.astype(float))*db + b1

A = array( [0.0, 0.0] )
B = array( [1.0, 2.0] )
C = array( [4.0, 3.0] )
D = array( [4.0, -5.0] )


E = seg_intersect(A,B,C,D)
F = seg_intersect(D,A,B,C)


P = seg_intersect(B,C,E,K)
Q = seg_intersect(C,D,E,K)


R = seg_intersect(A,B,F,K)
S = seg_intersect(D,C,F,K)

h1=math.fabs(np.linalg.norm(K - Q))
h2=math.fabs(np.linalg.norm(Q - P))

h3=math.fabs(np.linalg.norm(K - S))
h4=math.fabs(np.linalg.norm(S - R))

x= math.fabs(((h1-h2)/h2)*1366)
y= math.fabs(((h3-h4)/h4)*720)
print (x)
print (y)

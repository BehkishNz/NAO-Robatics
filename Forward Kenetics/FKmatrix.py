# Template for multiplying two matrices
def matprint(mat, fmt="g"):
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
        print("")

import numpy.matlib as npm
import math
# Use help(math) to see what functions
# the math library contains

i = 1
AfiRow = [math.cos(theta[i]*(math.pi)/180), -math.sin(theta[i]*(math.pi)/180)*math.cos(alpha[i]*(math.pi)/180), math.sin(theta[i]*(math.pi)/180)*math.sin(alpha[i]*(math.pi)/180), a[i]*math.cos(theta[i]*(math.pi)/180)]
ASRow = [math.sin(theta[i]*(math.pi)/180), math.cos(theta[i]*(math.pi)/180)*math.cos(alpha[i]*(math.pi)/180), -math.cos(theta[i]*(math.pi)/180)*math.sin(alpha[i]*(math.pi)/180), a[i]*math.sin(theta[i]*(math.pi)/180)]
ATRow = [0,math.sin(alpha[i]*(math.pi)/180), math.cos(alpha[i]*(math.pi)/180), d[i] ]
AFoRow = [0,0,0,1]
A = [AfiRow, ASRow, ATRow, AFoRow]

C = npm.matmul(C, A)
print('RShoulderRoll=')

matprint(C)


i = 2
AfiRow = [math.cos(theta[i]*(math.pi)/180), -math.sin(theta[i]*(math.pi)/180)*math.cos(alpha[i]*(math.pi)/180), math.sin(theta[i]*(math.pi)/180)*math.sin(alpha[i]*(math.pi)/180), a[i]*math.cos(theta[i]*(math.pi)/180)]
ASRow = [math.sin(theta[i]*(math.pi)/180), math.cos(theta[i]*(math.pi)/180)*math.cos(alpha[i]*(math.pi)/180), -math.cos(theta[i]*(math.pi)/180)*math.sin(alpha[i]*(math.pi)/180), a[i]*math.sin(theta[i]*(math.pi)/180)]
ATRow = [0,math.sin(alpha[i]*(math.pi)/180), math.cos(alpha[i]*(math.pi)/180), d[i] ]
AFoRow = [0,0,0,1]
A = [AfiRow, ASRow, ATRow, AFoRow]

C = npm.matmul(C, A)
print('RElbowYaw=')

matprint(C)


i = 3
AfiRow = [math.cos(theta[i]*(math.pi)/180), -math.sin(theta[i]*(math.pi)/180)*math.cos(alpha[i]*(math.pi)/180), math.sin(theta[i]*(math.pi)/180)*math.sin(alpha[i]*(math.pi)/180), a[i]*math.cos(theta[i]*(math.pi)/180)]
ASRow = [math.sin(theta[i]*(math.pi)/180), math.cos(theta[i]*(math.pi)/180)*math.cos(alpha[i]*(math.pi)/180), -math.cos(theta[i]*(math.pi)/180)*math.sin(alpha[i]*(math.pi)/180), a[i]*math.sin(theta[i]*(math.pi)/180)]
ATRow = [0,math.sin(alpha[i]*(math.pi)/180), math.cos(alpha[i]*(math.pi)/180), d[i] ]
AFoRow = [0,0,0,1]
A = [AfiRow, ASRow, ATRow, AFoRow]

C = npm.matmul(C, A)
print('RElbowRoll=')

matprint(C)

i = 4
AfiRow = [math.cos(theta[i]*(math.pi)/180), -math.sin(theta[i]*(math.pi)/180)*math.cos(alpha[i]*(math.pi)/180), math.sin(theta[i]*(math.pi)/180)*math.sin(alpha[i]*(math.pi)/180), a[i]*math.cos(theta[i]*(math.pi)/180)]
ASRow = [math.sin(theta[i]*(math.pi)/180), math.cos(theta[i]*(math.pi)/180)*math.cos(alpha[i]*(math.pi)/180), -math.cos(theta[i]*(math.pi)/180)*math.sin(alpha[i]*(math.pi)/180), a[i]*math.sin(theta[i]*(math.pi)/180)]
ATRow = [0,math.sin(alpha[i]*(math.pi)/180), math.cos(alpha[i]*(math.pi)/180), d[i] ]
AFoRow = [0,0,0,1]
A = [AfiRow, ASRow, ATRow, AFoRow]

C = npm.matmul(C, A)
print('RWrist=')

matprint(C)

A = [[1,0,0,0.113],[0,1,0,-0.015],[0,0,1,-0.01231],[0,0,0,1]]
C = npm.matmul(C, A)
print('REnd=')

matprint(C)
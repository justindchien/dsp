# Matrix Algebra

import numpy as np
A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1,-1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([[1],[8],[0],[5]])

print(A.shape)
'''
#1.1
A = 2x3
'''

print(B.shape)
'''
#1.2
B = 2x2
'''

print(C.shape)
'''
#1.3
D = 3x2
'''

print(D.shape)
'''
#1.4
D = 2x3
'''

print(u.shape)
'''
#1.5
u = 1x4
'''

print(w.shape)
'''
#1.6
w = 4x1
'''

print(u+v)
'''
#2.1
u+v = (9,7,-4,9)
'''

print(u-v)
'''
#2.2
u-v = (3,-3,-2,1)
'''

print(6*u)
'''
#2.3
6*v = (36,12,-18,30)
'''

print(np.dot(u,v))
'''
#2.4
u.v = 51
'''

print(np.sqrt(np.sum(np.square(u))))
'''
#2.5
||u|| = 8.6023
'''

print(A+C)
'''
#3.1
A+C = undefined
'''

print(A- C.transpose())
'''
#3.2
A-C^T =
[-4 -7 -3]
[ 3  6  4]
'''

print(C.transpose() + 3*D)
'''
#3.3
C^T+3D =
[14 3 3]
[ 2 7 9]
'''

print(B*A)
'''
#3.4
BA =
[-1 -5 -1]
[ 2  7  4]
'''

print(B*A.transpose())
'''
#3.5
BA^T = undefined
'''

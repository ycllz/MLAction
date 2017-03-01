from numpy import *
res = mat(random.rand(4, 4))
print res.I * res - eye(4)
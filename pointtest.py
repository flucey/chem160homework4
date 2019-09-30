#Also write a test script called pointtest.py that creates 2
#points p1=(1., 2., 3.) and p2=(6.,7.,8.),
#and then adds p2 to p1 using your add() function and calculates
#the square magnitude of the
#resulting p1 using your sqmag() function. 

from point import*
p1=point(3,[1.,2.,3.])
p2=point(3,[6.,7.,8.])
print(p1.add(p2))
print(p1.sqmag(p2))

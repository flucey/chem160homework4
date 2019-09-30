#Modify the multidimensional point class that we worked on in Module 6 to include 2 new functions.
#You’ll find the point.py file in GitHub repository you downloaded for this homework. Edit the
#class definition to add these two functions (keep the file name point.py):
#a. add(p2): This function has one argument that is a multidimensional point object which is
#added to the current object. That is:
#p1.add(p2)
#Adds each component of p2 to the corresponding component of p1, but doesn’t print or return
#any other output.
#b. sqmag(): The function returns the sum of the squares of each component in the current object.
#That is: p1.sqmag()
#returns the sum of the squares of each component in point p1. Specifically, the numerical value
#of the square magnitude is the return value of the function. 



class point:
    def __init__(self, dim, data):
        self.dim=dim
        self.data=[]
        for i in range(dim):
            self.data.append(float(data[i]))
            
    def __repr__(self):
        output=""
        for i in self.data:
            output+=str(i)+" "
        return output
    
    def scale(self, x):
        for i in range(self.dim):
            self.data[i]*=x
            
    def dot(self, apoint):
        sum=0
        for i in range(self.dim):
            sum+=self.data[i]*apoint.data[i]
        return sum
    
    def add(self, p2):
        sum=0
        for i in range(self.dim):
            add=self.data[i]+p2.data[i]
        return sum
    
    def sqmag(self,p1):
        mag=0
        for i in range(self.dim):
            mag=(self.data[i])**2+(p1.data[i])**2
        return mag
        




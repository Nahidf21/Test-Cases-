class test:
    def __init__(self,x=10,y=100):
        self.x=x
        self.y=y
    
    def testEqual(self,m,n):
        if m==n:
            return 'Pass'
        else:
            return '{} is not equal to {}'.format(m,n)
    def __str__(self):
        return '{} is printed'.format(self.x)

def square(z):
    ''' raise x to the second power'''
    return z*z
test1=test()

print('Testing square function')
print(test1.testEqual(square(10),101))
print(test1)
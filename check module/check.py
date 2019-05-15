class s(object):
    def __init__(self,pa1=1,pa2=2):
        pass
        print 1
        self.pa1 = pa1
        self.pa2 = pa2
    def output(self,pa1,pa2):
        print self.pa1
        print self.pa2
        print pa1
        print pa2
    def an(self,p3):
        print p3 - 1
        self.output(p3,p3)

print 111
print __name__
if __name__=="__main__":
    print 2

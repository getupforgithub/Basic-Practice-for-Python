
import easygui
class newfile(object):
    def __init__(self):
        pass
        self.filename = easygui.enterbox("PLZ enter your filename:")
    def create(self):
        pass

        content = easygui.enterbox("PLZ enter your content:")
        with open(self.filename,"w+") as obj:
            obj.write(content+"\n")
        with open(self.filename,"r") as obj:
            t = obj.read()
            print "your content is "+ t
    def add(self):
        pass
        addcontent = easygui.enterbox("PLZ add your content:")
        with open(self.filename,'a') as obj:
            obj.write(addcontent)
    def printout(self):
        pass
        with open(self.filename,'r') as obj:
            print obj.read()


A = newfile()
A.create()
A.add()
A.printout()

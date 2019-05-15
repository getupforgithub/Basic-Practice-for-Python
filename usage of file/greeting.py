
import easygui
class greeting(object):
    def __init__(self):
        pass
        self.filename = easygui.enterbox("which file to save your message?")
    def clear(self):
        with open(self.filename+".txt",'w') as obj:
            obj.write("")
    def inputname(self):
        pass
        name = easygui.enterbox("please enter your name")
        print "Hello!" + name + ", welcome come to python world."
        with open(self.filename+".txt",'a') as obj:
            obj.write(name + "\n")

ss = greeting()
ss.clear()
for i in range(3):
    ss.inputname()

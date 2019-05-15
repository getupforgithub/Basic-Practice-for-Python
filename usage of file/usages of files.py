# -*- coding: cp936 -*-
'''
创建两个文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。编写一个程序，尝试读取这些文件，
并将其内容打印到屏幕上。将这些代码放在一个try-except 代码块中，以便在文件不存在时捕获FileNotFound 错误，并打印一条友好的消息。将其中一个文件
移到另一个地方，并确认except 代码块中的代码将正确地执行。'''

import easygui
class twofiles(object):
    def __init__(self):
        pass
    def create(self,j):
        for i in range(j):
            if i == 0:
                with open("cats.txt","w") as obj:
                    obj.write("")
            else:
                with open("dogs.txt","w") as obj:
                    obj.write("")
    def writein(self):
        self.create(2)
        for i in range(2):
            for j in range(3):
                if i == 0:
                    with open("cats.txt","a") as obj:
                         obj.write(easygui.enterbox("PLZ input cats' name")+"\n")
                else:
                    with open("dogs.txt","a") as obj:
                         obj.write(easygui.enterbox("PLZ input dogs' name")+"\n")

    def checkin(self,name1,name2):
        try:
            with open(name1+".txt","r") as obj1:
                print obj1.readlines()   
            with open(name2+".txt","r") as obj2:
                print obj2.readlines()
        except IOError:
            print "Sorry, the files cannot be found" 
    def checkname(self):
        name1 = raw_input("cats' file name:")
        name2 = raw_input("dogs' file name:")
        self.checkin(name1,name2)
    def whole(self):
        self.writein()
        self.checkname()
test = twofiles()
test.whole()

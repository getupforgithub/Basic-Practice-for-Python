# -*- coding: cp936 -*-
'''
编写一个while 循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。'''

import easygui
class whylike(object):
    def __init__(self):
        pass
        self.filename = easygui.enterbox("Input your filename:")
        with open(self.filename+".txt",'w') as obj:
            obj.write("")
##        self.A = []
    def reason(self):
        pass
        reasons = easygui.enterbox("why do you like program?")
        flag = self.check(reasons)
        if flag:
            with open(self.filename+".txt",'a') as obj:
                obj.write(reasons + "\n")
    def check(self,reasons):
        with open(self.filename+".txt",'r') as obj: 
            A = obj.readlines()
            for i in A:
                if i.strip() == reasons.strip():
                    return False
                    break
                else:
                    pass
            return True

myreason = whylike()
i = 0
while i <= 5:
    myreason.reason()
    i += 1

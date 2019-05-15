# -*- coding: cp936 -*-
"""
10-12 记住喜欢的数字 ：将练习10-11中的两个程序合而为一。如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。
运行这个程序两次，看看它是否像预期的那样工作。
"""
import json
class num(object):
    def __init__(self):
        self.filename = raw_input("Enter your filename please:")
    def inp(self,filename):
        a = raw_input("What is you favourite number:")
        with open(self.filename+".json","w") as obj:
            json.dump(a,obj)
    def outp(self,filename):
        with open(filename+".json","r") as obj1:
            b = json.load(obj1)
            print "I know your favourite number is",b
    def aa(self):
        try:
            self.outp(self.filename)
        except IOError:
            print "The file cannot be found."
            self.inp(self.filename)
            self.outp(self.filename)
test = num()
test.aa()

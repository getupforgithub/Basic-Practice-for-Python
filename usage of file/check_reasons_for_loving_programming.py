# -*- coding: cp936 -*-
'''
��дһ��while ѭ����ѯ���û�Ϊ��ϲ����̡�ÿ���û�����һ��ԭ��󣬶�������ӵ�һ���洢����ԭ����ļ��С�'''

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

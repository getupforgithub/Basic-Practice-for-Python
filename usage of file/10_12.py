# -*- coding: cp936 -*-
"""
10-12 ��סϲ�������� ������ϰ10-11�е���������϶�Ϊһ������洢���û�ϲ�������֣������û���ʾ����������ʾ�û�������ϲ�������ֲ�����洢���ļ��С�
��������������Σ��������Ƿ���Ԥ�ڵ�����������
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

# -*- coding: cp936 -*-
'''
���������ļ�cats.txt��dogs.txt���ڵ�һ���ļ������ٴ洢��ֻè�����֣��ڵڶ����ļ������ٴ洢�����������֡���дһ�����򣬳��Զ�ȡ��Щ�ļ���
���������ݴ�ӡ����Ļ�ϡ�����Щ�������һ��try-except ������У��Ա����ļ�������ʱ����FileNotFound ���󣬲���ӡһ���Ѻõ���Ϣ��������һ���ļ�
�Ƶ���һ���ط�����ȷ��except ������еĴ��뽫��ȷ��ִ�С�'''

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

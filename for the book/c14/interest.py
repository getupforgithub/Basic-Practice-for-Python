"""2. ����һ����������Ϣ���࣬��ΪInterestAccount����Ӧ����BankAccount
��һ�����ࣨ���Ի�̳�BankAccount �����Ժͷ�������InterestAccount
��Ӧ����һ����Ӧ��Ϣ�ʵ����ԣ�������һ��������������Ϣ��Ϊ�������
��������ÿ������һ��addInterest() ����������Ϣ��������"""
class BankAccount(object):
    def __init__(self):
        self.account = ""
        self.num = 0
        self.remaining = 100000
        self.indrawnum = 0
        self.withdrawnum = 0
    def inputaccount(self):
        self.num = int(raw_input("Input your account number please:"))

    def withdraw(self,withdrawnum):
        if withdrawnum > self.remaining:
            print "sorry, you don't have so much money"
        else:
            self.remaining = self.remaining - withdrawnum
    def indraw(self,indrawnum):
        self.remaining = self.remaining + indrawnum
    def show(self):
        print "your account number:",self.num
        print "your remaining:",self.remaining



class InterestAccount(BankAccount):
    def __init__(self):
        super(InterestAccount,self).__init__()
        self.rate = 0.06
        self.interest = 0
##        self.remaining = 100000
        
    def interest1(self,rate):
        self.interest =  rate * self.remaining
##
##    def rate1(self):
##        self.interest()
##        print self.interest

    def rate1(self,years):
        for i in range(years):
            print "No",i+1," year:"
            rate = float(raw_input("What the interest rate of this year:"))
            self.interest1(rate)
            print self.interest
            

    def showinterest(self):
        k = int(raw_input("How many years:"))
        self.rate1(k)

myaccount = InterestAccount()
myaccount.inputaccount()
myaccount.withdraw(1000)
myaccount.show()
myaccount.showinterest()
####print myaccount.remaining

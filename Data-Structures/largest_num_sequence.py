class out1(object):
    def __init__(self,list=[],max=0,start=0,end=0):
        self.list = list
        self.max = max
        self.start = start
        self.end = end
    def main(self):
        for i in range(len(self.list)):
            add = 0
            for j in range(len(self.list)-i):
                k = i + j
                add = add + self.list[k]
                if add <= 0:
                    break
                if add >= self.max:
                    self.max = add
                    self.start = i + 1
                    self.end = i + j + 1
        print self.max
        print self.start
        print self.end
list11 = [1, 7, -23, 1, 4, -2, 5, -1, -2, 12,-17]
raw = out1(list11)
raw.main()

# list1 = [1, 7, -23, 1, 4, -2, 5, -1, -2, 12,-17]
# add = 0
# max = 0
# start = 0
# end = 0
# for i in range(len(list1)):
#     add = 0
#     print 1
#     for j in range(len(list1)-i):
#         k = i+j
#         add = add + list1[k]
#         print add
#         if add <= 0:
#             break
#         if add >= max:
#             max = add
#             start = i + 1
#             end = i + j + 1
# print max
# print start
# print end
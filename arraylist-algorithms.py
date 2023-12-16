import numpy as np
class list1:
    def __init__(self):
        self.n=0
        self.a=np.zeros([10], dtype='int')
    #---------------insertion-------------#
    def insrt_strt(self, item):
        for i in range(self.n, 0, -1):
            self.a[i]=self.a[i-1]
        self.a[0]=item
        self.n+=1
    def insrt_last(self,item):
        self.a[self.n]=item
        self.n+=1
    def insrt_loc(self, loc, item):
        if loc<self.n and loc>-1:
            for i in range(self.n, loc-1, -1):
                self.a[i]=self.a[i-1]
            self.a[loc]=item
            self.n+=1
        else:
            print(f"Index Number {loc} not in list")
    #-------------Delete-------------#
    def delt_strt(self):
        for i in range(1, self.n):
            self.a[i-1]=self.a[i]
        self.n-=1
    def delt_loc(self, loc):
        for i in range(loc+1, self.n):
            self.a[i-1]=self.a[i]
        self.n-=1
    def delt_last(self):
        self.n-=1

    #----------Searching-----------#
    #1   -------Linear Search------  #
    def lin_search(self,item):
        self.x=0
        for i in range(0, self.n):
            if self.a[i]==item:
                print(f"{item} found at index at {i}")
                self.x+=1
        if self.x==0:
            print(f"{item} not exit in list")
    #--------Traversing---------#
    def traverse(self):
        for i in range(0, self.n):
            print(self.a[i], end=' ')
        print(" ")
    #--------Binary Search-------#
    def bin_search(self,item):
        self.lb=0
        self.ub=self.n-1
        self.mid=int((self.lb+self.ub)/2)
        while self.lb <= self.ub and self.a[self.mid] != item:
            if self.a[self.mid]<item:
                self.lb=self.mid+1
            else:
                self.ub=self.mid-1
            self.mid=int((self.lb+self.ub)/2)
        if self.a[self.mid]==item:
            print(f"{item} found at index number {self.mid}")
        else:
            print(f"{item} not found in this array")
#---------------Buble Sorting-----------#
    def bub_srt(self):
        for i in range(0, self.n-1):
            self.temp=0
            for j in range(0, (self.n-1)-i):
                if self.a[j]>self.a[j+1]:
                    self.temp=self.a[j]
                    self.a[j]=self.a[j+1]
                    self.a[j+1]=self.temp

    
            




AL=list1()
#--------insersation Functions--------#
AL.insrt_strt(4)
AL.insrt_strt(7)
AL.insrt_strt(8)
AL.insrt_last(5)
AL.insrt_last(6)
AL.insrt_last(3)
AL.insrt_last(2)
AL.insrt_last(11)
AL.traverse()
#----------Delete Functions---------#
'''AL.delt_loc(1)
AL.delt_strt()
AL.delt_last()
print("After Delete Elements")
AL.traverse()'''
#-------Linear Search-------#
AL.lin_search(5)
AL.lin_search(8)
#------- Binrary Search-------#
AL.bin_search(4)
#--------Buble Sorting-------#
AL.bub_srt()
AL.traverse()
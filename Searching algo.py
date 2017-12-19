# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 22:42:25 2017

@author: Trupti
"""
class Person:
    def __init__(self,num):
        self.num=num
        self.list1=[]
        
    def take_num(self):
       print("please Enter numbers")
       for i in range(0,self.num):
           num1=input()
           self.list1.append(int(num1))
           
    def choose_action(self):
        print("What do you want to do with this number give choice from below!")
        print("1.Linear Search")
        print("2.binary Search")
        print("3.Bubble sort")
        print("4.Selection sort")
        print("5.End")
        
        self.choice=input("please enter valid choice")
        self.choice=int(self.choice)
        if self.choice==1:
            n=self.linear_search()
            if n!=-1:
                print("number is on ",n+1,"position")
            else:
                print("number not in list")
                  
                    
            self.choose_action()
        elif self.choice==2:
            
            n=self.binary_search()
            if n==True:
                print("number found")
            else:
                print("number not in list")
            self.choose_action()
        elif self.choice==3:
            
            list3=[]
            list3= self.bubble_sort()
            print("Sorted list:")
            print(list3)
            self.choose_action()
        elif self.choice==4:
            
            list2=[]
            list2=self.selection_sort()
            print("Sorted list:")
            print(list2)
            self.choose_action()   
        elif self.choice==5:
            print("Thank you!! Bye Bye")
        else:
            {
                print("please enter valid choice!!!")        
            }
        
    def linear_search(self):
          print("you are searching number with help of linear search algo")
          n=input("Enter the number which u want to search")
          n=int(n)
          for i in range(0,len(self.list1)):
              if self.list1[i]==n:
                  return i
          return -1
                  
    
    def binary_search(self):
        print("you are searching number with help of binary search algo")
        n=input("Enter the number which u want to search")
        n=int(n)
        self.list1.sort()
        print(self.list1)
        l=0;
        h=len(self.list1)-1;
        for i in range(l,h):
            mid_no=(l+h)//2
            mid=self.list1[mid_no]
            if mid==n:
                return True;
            elif n>mid:
                l=mid+1;
            elif n<mid:
                h=mid-1;
                
    def bubble_sort(self):
       
       for i in range(0,len(self.list1)):
           flag=0
           for j in range(0,len(self.list1)-i-1):
               if(self.list1[j]>self.list1[j+1]):
                   flag+=1;
                   self.list1[j],self.list1[j+1]=self.list1[j+1],self.list1[j]
           if flag==0:
               break;
              
       return self.list1;
                   
           
       return self.list1        
    def selection_sort(self):
        print("you are sorting list with selection sort")
        for i in range(0,len(self.list1)):
            for j in range(i+1,len(self.list1)):
                if self.list1[j]<self.list1[i]:
                    self.list1[i],self.list1[j]=self.list1[j],self.list1[i]
   
        return self.list1;
if __name__ == "__main__":
    
    n=input("how many number you want to enter?")
    n=int(n)
    p=Person(n)
    p.take_num()
    print("these are the number which u have entered!!")
    print(p.list1)
    p.choose_action()
    
    
#array=[[1,2,3,4],[5,1,7,8]]
#
#j=len(array)-1
#while j>=0:
#    i=len(array[j])-1
#    while i>=0:
#        print(array[j][i])
#        i-=1
#    j-=1
#
#arr=[[1,2,3,4],[5,6,7,8]]
#arra=array+arr
#print(arra)
#
#list={}
#for j in array:
#    for i in j:
##        if i  in list:
##            list[i]+=1
##        else:
##            list[i]=1
##for value,key in list.items():
##    if key>1:
##        print(f'{value}:{key}') 
#array=[1,2,3,4,5,5]
#maxx=0
#for num in array:
#    if num>maxx:
#        maxx=num
#print(maxx)
#evens=0
#for even in array:
#    if even%2==0:
#        evens+=even
#print(evens)
#text='hello how are you'
#chars=0
#for char in text:
#    if char!=' ':
#        chars+=1
#print(f'number of characters is :{chars}')
#list=[1,2,1,3,2]
#nums={}
#for i in list:
#    if i  in nums:
#        nums[i]+=1
#    else:
#        nums[i]=1
#for key, value in nums.items():
#    if value>1:
#        print(f'{key}:{value}')
#word='hello'
##print(word[::-1])
#class Node:
#    def __init__(self,value,next=None):
#        self.value=value
#        self.next=next
#def print_l(head):
#    p=head
#    while p!=None:
#        print(p.value)
#        p=p.next  
#def add_l(head,value):
#    node=Node(value)
#    p=head
#    while p.next!=None:
#        p=p.next
#    if p==None:
#        node.next=head
#        head=node
#    else:
#        p.next=node
#    return head
#def get_l(head,index):
#    if index<0:
#        print('enter valaid number')
#    p=head
#    i=0
#    while p!=None and i<index:
#        p=p.next
#        i+=1
#    if p==None:
#        print('value does not exist')
#    else:
#        print(p.value)
#def remove_l(head,v):
#    p=head
#    q=None
#    while p is not None :
#        if p.value==v:
#            if p==head:
#                head=p.next
#                p=head
#            else:
#                q.next=p.next
#                p=p.next
#        else:
#            q=p
#            p=p.next
#    return head
#
#
#n=Node(2)
#n1=Node(3)
#n2=Node(5)
#
#n.next=n1
#n1.next=n2
#head=n
#
##head=add_l(head,5)
#get_l(head,8)
#head=remove_l(head,3)
#print_l(head)
#class Stack:
#    def __init__(self):
#        self.s=[]
#    def push(self,value):
#        self.s.append(value)
#    def pop(self):
#        if self.isempty:
#            return None
#        self.s.pop()
#    def top(self):
#        if self.isempty:
#            return None
#        return self.s[-1]
#    def isempty(self):
#        if len(self.s)==0:
#            return True
#        else:
#            return False
#s1=Stack()
#s1.push(3)
#s1.pop()
#print(s1.top())
#class Queue:
#    def __init__(self):
#        self.q=[]
#    def enqueue(self,value):
#        self.q.append(value)
#    def dequeue(self):
#        self.q.pop(0)
#    def front(self):
#        print(self.q[0])
#    def isempty(self):
#        if len(self.q)==0:
#            return True
#        else:
#            return False
#q1=Queue()
#q1.enqueue(3)
#q1.dequeue()
#q1.enqueue(4)
#q1.front()
#def f(x):
#    if x==0:
#        return 1
#    result=x*f(x-1)
#    print(f'{x}:{result}')
#    return result
#
#print(f(5))
def binary(list,value):
    l=0
    h=len(list)-1
    while l<=h:
        m=(h+l)//2
        if list[m]==value:
            return True
        elif list[m]<value:
            l=m+1
        else:
            h=m-1
    return False
a=[1,3,5,6,7,8,99,255,777]

v=binary(a,1)
print(v)







            





    
               

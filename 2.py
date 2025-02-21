class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
def print_l(head):
    p=head
    while p!=None:
        print(p.value)
        p=p.next
    print()
def add_l(head,value):
    node=Node(value)
    p=head
    while p.next!=None:
        p=p.next
    if p==None:
        node.next=head
        head=node
    else:
        p.next=node
    return head
def get(head,index):
    if index<0:
        print('error')
    p=head
    i=0
    while p!=None and i<index:
        p=p.next
        i+=1
    if p==None:
        print('do not exist')
def rimove(head,v):
    p=head
    q=None
    while p!=None:
        if p.value==v:
            if p==head:
                head=head.next
                p=head
            else:
                q.next=p.next
                p=p.next
        else:
            q=p
            p=p.next
    return head

    

    
n1=Node(1)
n2=Node(2)
n3=Node(1)
n1.next=n2
n2.next=n3
head=n1
head=add_l(head,3)
head=rimove(head,1)
print_l(head)
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
def add_first(head,value):
    node=Node(value)
    node.next=head
    head=node
    return head
def add_last(head,value):
    node=Node(value)
    p=head
    while p.next!=None:
        p=p.next
    p.next=node
    return head
def get_l(head,index):
    if index<0:
        print('error')
        return
    p=head
    i=0
    while p!=None and i<index:
        p=p.next
        i+=1
    if p==None:
        print('value does not exist')
    else:
        print(p.value)
    return head
def remove(head,v):
    p=head
    q=None
    while p!=None and p.value!=v:
        q=p
        p=p.next
    if p==None:
        print('error')
    else:
        if p==head:
            head=head.next
        else:
            q.next=p.next
    return head   
def delete_r(head,v):
    p=head
    a=None
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
n3=Node(3)
n1.next=n2
n2.next=n3
head=n1
head=add_first(head,1)
head=add_last(head,1)
print_l(head)
head=get_l(head,5)
head=remove(head,1)
head=delete_r(head,1)
print_l(head)

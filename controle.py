#def selection_sort(list):
#    n=len(list)
#    for i in range(n):
#        index_min=i
#        for j in range(i,n):
#            if list[j]<list[index_min]:
#                index_min=j
#        list[i],list[index_min]=list[index_min],list[i]
#arr=[1,0,24,56,7,8]
##selection_sort(arr)
##print(arr)
#def bubble_sort(list):
#    n=len(list)
#    permition=True
#    while permition:
#        permition=False
#        for i in range(n-1):
#            if list[i]>list[i+1]:
#                list[i+1],list[i]=list[i],list[i+1]
#                permition=True
##bubble_sort(arr)
##print(arr)
#def insertion_sort(list):
#    n=len(list)
#    for i in range(n):
#        j=i
#        while j>0 and list[j]<list[j-1]:
#            list[j],list[j-1]=list[j-1],list[j]
#            j=j-1
##insertion_sort(arr)
##print(arr)
#def binary_search(list,value):
#    l=0
#    h=len(list)-1
#    while l<=h:
#        m=(h+l)//2
#        if list[m]==value:
#            return True
#        elif list[m]<value:
#            l=m+1
#        else:
#            h=m-1
#    return False
#a=sorted(arr)
#r=binary_search(a,8)
#print(r)
#
#def selection_sort(list):
#    n=len(list)
#    for i in range(n):
#        index_min=i
#        for j in range(i,n):
#            if list[j]<list[index_min]:
#                index_min=j
#        list[index_min],list[i]=list[i],list[index_min]
#def bubble_sort(list):
#    n=len(list)
#    p=True
#    while p:
#        p=False
#        for i in range(n-1):
#            if list[i]>list[i+1]:
#                list[i],list[i+1]=list[i+1],list[i]
#                p=True
#def insertion_sort(list):
#    n=len(list)
#    for i in range(n):
#        j=i
#        while j>0 and list[j]<list[j-1]:
#            list[j],list[j-1]=list[j-1],list[j]
#            j=j-1
#a=[1,2,4,4,5,45,54]
#b=[3,21,3,42,5,4,5]
#c=[2,3,5,7,4,35,53]
#insertion_sort(a)
#bubble_sort(b)
#selection_sort(c)
#print(a,b,c)
#def binary(list,value):
#    l=0
#    h=len(list)-1
#    while l<=h:
#        m=(l+h)//2
#        if list[m]==value:
#            return True
#        elif list[m]<value:
#            l=m+1
#        else:
#            h=m+-1
#    return False
#print(binary(a,54))
#class Linked:
#    def __init__(self,value,next=None):
#        self.value=value
#        self.next=next
#def print_l(head):
#    p=head
#    while p!=None:
#        print(p.value)
#        p=p.next
#def add_l(head,value):
#    node=Linked(value)
#    p=head
#    while p.next!=None:
#        p=p.next
#    if p==None:
#        node.next==head
#        head=node
#    else:
#        p.next=node
#    return head
#n1=Linked(1)
#n2=Linked(2)
#n3=Linked(3)
#n1.next=n2
#n2.next=n3
#head=n1
#def selection_sort(list):
#    for i in range(len(list)):
#        index_min=i
#        for j in range(i,len(list)):
#            if list[j]<list[index_min]:
#                index_min=j
#        list[index_min],list[i]=list[i],list[index_min]
#a=[1,4,6,8,9,3,2]
#selection_sort(a)
#print(a)
#def bubble_sort(arr):
#    n=len(arr)
#    p=True
#    while p:
#        p=False
#        for i in range(n-1):
#            if arr[i]>arr[i+1]:
#                arr[i+1],arr[i]=arr[i],arr[i+1]
#                p=True
#        
#a=[3,2,1]
#bubble_sort(a)
#print(a)
#def merg_tow_sorted(a,b):
#    n=len(a)
#    m=len(b)
#    i=0
#    j=0
#    r=[]
#    while i<n and j<m:
#        if a[i]<b[j]:
#            r.append(a[i])
#            i+=1
#        else:
#            r.append(b[j])
#            j+=1
#    while i<n:
#            r.append(a[i])
#            i+=1
#    while j<m:
#          r.append(b[j])
#          j+=1
#    return r
#def merge_sort(arr):
#     n=len(arr)
#     if n==1:
#          return arr
#     mid=n//2
#     a=merge_sort(arr[0:mid])
#     b=merge_sort(arr[mid:n])
#     r=merg_tow_sorted(a,b)
#     return r
#array=[2,425,5453,55,56,1,45]
#r=merge_sort(array)
#print(r)
#class nodeTree:
#    def __init__(self,value):
#        self.value=value
#        self.left=None
#        self.right=None
#def in_order(root):
#    if root==None:
#        return
#    in_order(root.left)
#    print(root.value)
#    in_order(root.right)
#
#root=nodeTree(4)
#t2=nodeTree(2)
#t3=nodeTree(5)
#t4=nodeTree(1)
#t5=nodeTree(3)
#t6=nodeTree(6)
#root.left=t2
#root.right=t3
#t2.left=t4
#t2.right=t5
#t3.right=t6
#in_order(root)
#def adj_list(n,edges):
#    graph=[[] for _ in range(n)]
#    for e in edges:
#        a=e[0]
#        b=e[1]
#        graph[a].append(b)
#        graph[b].append(a)
#    return graph
#def dfs(graph,visited,current_node):
#    visited[current_node]=True
#    print(current_node)
#    for node in graph[current_node]:
#        if visited[node]:
#            continue
#        dfs(graph,visited,node)
#n=5
#edges=[(0,1),(0,2),(1,2),(1,3),(2,3)]
#graph=adj_list(n,edges)
#print(graph)
#visited=[False for i in range(n)]
#for i in range(n):
#    if visited[i]:
#        continue
#    dfs(graph,visited,i)
def adj_list(n,edges):
    graph=[[] for i in range(n)]
    for e in edges:
        a=e[0]
        b=e[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph
#def dfs(graph,visited,current_node):
#    visited[current_node]=True
#    print(current_node)
#    for node in graph[current_node]:
#        if visited[node]:
#            continue
#        dfs(graph,visited,node)
#dfs(graph,visited,0)

#n=5
#edges=[(0,1),(0,2),(0,4),(1,2),(1,3),(2,3)]
#graph=adj_list(n,edges)
#visited=[False]*n
#bfs(graph,visited)
#
#def dfs(graph,visited,current_node):
#    visited[current_node]=True
#    print(current_node)
#    for node in graph[current_node]:
#        if visited[node]:
#            continue
#        dfs(graph,visited,node)
#def Bfs(graph, visited):
#    q=Queue()
#    q.enqueue(0)
#    visited[0]=True
#    while not q.isempty():
#        current_node=q.front()
#        print(current_node)
#        q.dequeue()
#        for node in graph[current_node]:
#            if visited[node]:
#                continue
#            q.enqueue(node)
#            visited[node]=True
#Bfs(graph,visited)   
class Queue:
    def __init__(self):
        self.q=[]
    def enqueue(self,value):
        self.q.append(value)
    def dequeue(self):
        self.q.pop(0)
    def front(self):
        return self.q[0]
    def isempty(self):
        return len(self.q)==0
def bfs(graph,visited):
    q=Queue()
    q.enqueue(0)
    visited[0]=True
    while not q.isempty():
        current_node=q.front()
        print(current_node)
        q.dequeue()
        for node in graph[current_node]:
            if visited[node]:
                continue
            q.enqueue(node)
            visited[node]=True
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
        if len(self.q)==0:
            print('Empty')
        else:
            print('Not empty')
qu=Queue()
qu.enqueue(2)
qu.enqueue(9)
qu.enqueue('hello')
qu.dequeue()
qu.dequeue()

qu.isempty()
a=qu.front()
print(a[::-1])
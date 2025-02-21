class Stack:
    def __init__(self):
        self.s=[]
    def push(self,value):
        self.s.append(value)
    def pop(self):
        if self.isempty():
            print('error')
            return None
        self.s.pop()
        return True
    def top(self):
        if self.isempty():
            print('error')
            return None
        else:
            return self.s[-1]
    def isempty(self):
        return len(self.s)==0


def check(text):
    stack=Stack()
    for char in text:
        if char=='(':
            stack.push(char)
        elif char==')':
            if stack.isempty():
                return False
            stack.pop()
    return stack.isempty()
print(check('(())'))
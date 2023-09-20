class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, val):
        #write code here
        self.inStack.append(val)

    def pop(self):
        #write code here
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()

    def peek(self):
        #write code here
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self):
        # write code here
        return len(self.inStack) == 0 and len(self.outStack) ==0
# cate
# 19.3.23
# 用python实现栈


class Stack(object):
    def __init__(self):
        self.data_stack =[]

    def init_stack(self):
        self.data_stack = []

    def insert(self,data):
        self.data_stack.append(data)

    def pop(self):
        if len(self.data_stack) == 0:
            return None
        data = self.data_stack[-1] # 返回最后插入的那个元素
        del self.data_stack[-1]
        return data

    def size(self):
        return len(self.data_stack)


stack = Stack()
stack.insert(1)
stack.insert(2)
stack.insert(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())





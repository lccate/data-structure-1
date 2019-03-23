# cate
# 19.3.23
# 用python实现队列


class Queue(object):
    def __init__(self):
        self.data_list = []

    def init_queue(self):
        self.data_list = []

    def insert(self,data):
        self.data_list.append(data)

    def pop(self):
        if len(self.data_list) == 0:
            return None
        data = self.data_list[0]
        del self.data_list[0]
        return data

    def size(self):
        return len(self.data_list)

queue = Queue()
print(queue.size())
queue.insert(1)
queue.insert(2)
queue.insert(3)
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
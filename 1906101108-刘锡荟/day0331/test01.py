class Stack(object):
    def __init__(self,limit = 10):
        self.stack = []
        self.limit = limit
    def is_empty(self):
        return len(self.stack) == 0
    def push(self,data):
        if len(self.stack)>=self.limit:
            print("栈溢出")
        else:
            self.stack.append(data)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("空栈不能被弹出")
    def top(self):
        if self.stack:
            return self.stack[-1]
    def size(self):
        return len(self.stack)

stack = Stack()
print(stack.size())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.size())
print(stack.is_empty())
print(stack.pop())
print(stack.top())
class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack(object):
    def __init__(self):
        self.node = Node(Node)
        self.head = self.node
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def get_size(self):
        return self.size
    def push(self,data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size +=1
    def pop(self):
        if not self.is_empty(): #判断是否为空
            current_node = self.head.next #保存栈顶元素
            if self.get_size() == 1:
                self.head.next = Node
                self.size-=1
            else:
                self.head.next = self.head.next.next #头节点指向栈顶的下一个节点
                self.size -= 1
                return current_node.data
        else:
            print("栈为空")
    def top(self):
        if not self.is_empty():
            return self.head.next.data
        else:
            print("栈为空")
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.is_empty())
print(s.top())
s.pop()
s.pop()
s.pop()
print(s.is_empty)


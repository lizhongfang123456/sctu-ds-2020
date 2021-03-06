class Node:
    def __init__(self,value):
        self.value=value#当前节点的值
        self.next=Node#下一个节点

class list:
    def __init__(self):
        #头节点
        self.head=Node(-1)
        #前插法创建单链表
    def insert_before(self,data):
        for i in data:
            node=Node(i)#创建新节点
            #判断节点的下一个节点是否为空
            if self.head.next is None:#如果为空，则将新节点加入到next
                self.head.next=node
            else:
                node.next=self.head.next#将头节点的下一个节点加入到当前节点
                self.head.next=node

#尾插法创建单链表
    def insert_tail(self,data):
        tail=self.head.next

        for i in data:
            node=Node(i)#创建新节点
#判断尾节点的下一个节点是否为空
            if tail is None:#如果为空，将新节点加入到tail
                self.head.next=node
                tail=node
            else:
                tail.next=node#将尾节点的下一个节点加入当前节点
                tail=next


#删除重复元素
    def clear_repetition(self):
        cur=self.head
        while cur:#遍历元素
            while cur.next and cur.value==cur.next.value:
                cur.next=cur.next.next#重复进行循环删除
            cur=cur.next#循环完全部

    #第i个节点前插入值为value的节点
    def list_element_add(self,i,value):
        node_new=Node(value)#创建新节点
        index=0
        node=self.head.next
        while node:#找位置
            index=index+1
            if index==i-1:
                break
            node=node.next
        if node is None:
            return False
        node_new.next=node.next#插入节点
        node.next=node_new
#交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59]要求被置换的俩个位置需要input输入
l=[14,25,98,75,23,1,4,56,59]
a,b=map(int,input('请输入需要置换的俩数位置数(两数见用空格隔开)：').split())
l[a],l[b]=l[b],l[a]
print(l)
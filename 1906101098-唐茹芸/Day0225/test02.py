num = int(input("请输入一个数字："))
if num % 2 ==0:
    if num % 3 ==0:
        print("这个数字技能被2也能被3整除")
    else：
        print("这个数字能被2整除不能被3整除")
else：
    if num % 3 == 0:
        print("这个数字可被3整除，2不行")
    else：
        print("3和2不行")

        
        
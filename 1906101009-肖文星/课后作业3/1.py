class Person():
    def __init__(self):
        self.name = "肖文星"
        self.age = 19
        self.gender = "male"
    def personInfo(self):
        return self.name,self.age,self.gender
a = Person()
print(a.personInfo())
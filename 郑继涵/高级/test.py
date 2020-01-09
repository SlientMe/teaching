class Student():
    time = 0
    def __init__(self,name):
        self.name = name
        self.time +=1
    def study(self):
        print("study")

s = Student("tim")
s1 = Student("Jack")
print(s.time)
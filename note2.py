print("hello")

print(1,2,3)

a = [1,2,3,4]
print(a)


# single inheritance

class student:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname =ln
        
    def displayname(self):
            print(self.firstname + self.lastname)
            
class teacher(student):
    def __init__(self,fn,ln,sl):
        super().__init__(fn,ln)
        self.salary = sl
        
    def displaysalary(self):
            print(self.salary)
            
d = teacher("ramesh","jadhav",25000)
print(d.firstname)
print(d.lastname)
print(d.salary)
d.displayname()
d.displaysalary()

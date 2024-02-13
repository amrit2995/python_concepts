class Employee:
    def __init__(self, name='', age=None):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age<other.age
    
    def __str__(self):
        return self.name
    
    def __repr__(self) -> str:
        return f"Employee({self.name},{str(self.age)})"
    
    def __add__(self,other):
        return self.age + other.age
    
    def __len__(self):
        return len(self.name)
        
    
employee_list = [Employee('a', 2), Employee('b', 1), Employee('f', 9), Employee('c',3), Employee('l', 5)]
# print(employee_list[0])
sorted_employee_list = sorted(employee_list)

for i in sorted_employee_list:
    print(str(i))
    print(repr(i))
    print(len(i))

print(sorted_employee_list[-1] + sorted_employee_list[-2])
# print(sorted_employee_list) 
    

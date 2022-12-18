class School: 
    def __init__(self, id, name, age, home_address, phone_number) :
        self.id = id 
        self.name = name
        self.age = age
        self.home = home_address
        self.number = phone_number

Ahmed = School(id= '100A', name = 'Ahmed', age= 9, home_address= 'Jeddah-Palestine street', phone_number= '058465014')  

Khaled = School(id= '150B', name= 'Khaled', age=13, home_address= 'Jeddah-Prince Mohammed Street', phone_number= '0535768648')


print(Ahmed)
print(Khaled.home)
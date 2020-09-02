class school():
    def __init__(self,name,lastname,salary,department):
        print("school init")
        self.name=name
        self.lastname=lastname
        self.salary=salary
        self.department=department
    def show_information(self):
        print("school information")
        print("name:{} \nlast_name:{} \nsalary:{} \ndepartment:{}".format(self.name,self.lastname,self.salary,self.department))
    def changing_department(self,new_department):
        self.department=new_department
    def rise(self, amount):
            self.salary += amount
class teacher(school):
    def __init__(self,name,lastname,salary,department,lesson):
        super().__init__(name,lastname,salary,department)
        print("teacher init")
        self.lesson=lesson
    def show_information(self):
        print("teacher information")
        print("name:{} \nlast_name:{} \nsalary:{} \ndepartment:{} \nlesson:{}".format(self.name, self.lastname, self.salary, self.department,self.lesson))
class principal(school):
    def __init__(self, name, lastname, salary, department, lesson,person_number):
        self.name = name
        self.lastname = lastname
        self.salary = salary
        self.department = department
        self.lesson=lesson
        self.number_people=person_number

    def show_information(self):
        print("principal information")
        print("name:{} \nlast_name:{} \nsalary:{} \ndepartment:{} \nlesson:{} \nperson_number:{}".format(self.name, self.lastname,self.salary, self.department,self.lesson,self.number_people))


teacher1=teacher("yusuf","eryılmaz",5000,"teacher","math")
teacher1.show_information()
principal1=principal("ali","cam",6000,"principal","eng",1000)
principal1.changing_department("head_principal")
principal1.show_information()
teacher1.rise(250)
teacher1.show_information()
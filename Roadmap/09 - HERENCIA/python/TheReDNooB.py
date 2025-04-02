#09 HERENCIA Y POLIMORFISMO

class Animal:
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self) -> str:
        return f"{self.name} is a {self.age} years old {self.gender} {type(self).__name__}"
    
    def sound(self) -> None:
        print(f"the {self.name} is making a sound")

lion: Animal = Animal("Simba", 5, "Male")
print(lion)
lion.sound()

class Dog(Animal):
    def __init__(self, name, age, gender, race: str) -> None:
        super().__init__(name, age, gender)
        self.race = race

    def sound(self) -> None:
        print(f"the {self.name} is barking")

    def __str__(self) -> str:
        return f"{super().__str__()} and is a {self.race}"

dog: Dog = Dog("Firulais", 3, "Male", "Labrador")
print(dog)
dog.sound()

class Cat(Animal):
    def __init__(self, name, age, gender, race: str) -> None:
        super().__init__(name, age, gender)
        self.race = race

    def sound(self) -> None:
        print(f"the {self.name} is meowing")

    def __str__(self) -> str:
        return f"{super().__str__()} and is a {self.race}"
    
cat: Cat = Cat("Garfield", 2, "Male", "Persian")
print(cat)
cat.sound()

class Employee:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.employees = []

    def add(self, employee) -> None:
        self.employees.append(employee)
        print(f"{self.employee} is adding an employee")

    def print_employees(self) -> None:
        for employee in self.employees:
            print(employee.name)

    def __str__(self) -> str:
        return f"{self.name} is an employee with id {self.id}"
    

class Developer(Employee):
    def __init__(self, id, name, area: str) -> None:
        super().__init__(id, name)
        self.area = area

    def code(self) -> None:
        print(f"{self.name} is coding")

    def add(self, employee) -> None:
        print("A developer can't add an employee")

    def __str__(self) -> str:
        return f"{super().__str__()} and is a {self.area} developer"
    
class Project_Manager(Employee):
    def __init__(self, id, name, project: list) -> None:
        super().__init__(id, name)
        self.project = project

    def add_project(self, project) -> None:
        self.project.append(project)

    def print_projects(self) -> None:
        for project in self.project:
            print(project)

    def add(self, employee) -> None:
        self.employees.append(employee)

    def print_employees(self) -> None:
        for employee in self.employees:
            print(employee.name)

    def __str__(self) -> str:
        return f"{super().__str__()} and is a project manager of the {self.project} project"
    
class Manager(Employee):
    def __init__(self, id, name) -> None:
        super().__init__(id, name)

    def add(self, employee) -> None:
        self.employees.append(employee)

    def print_employees(self) -> None:
        for employee in self.employees:
            print(employee.name)

    def __str__(self) -> str:
        return f"{self.name} and is a manager"
    
developer1: Developer = Developer(1, "TheReDNooB", "Backend")
print(developer1)
developer1.code()
developer2: Developer = Developer(2, "TheReDNooB2", "Frontend")
developer3: Developer = Developer(3, "Fredo", "Fullstack")
developer4: Developer = Developer(4, "David", "DevOps")
#developer1.add(developer2)

my_project_manager: Project_Manager = Project_Manager(5, "Mark", ["workshop", "Pet Shop"])
my_project_manager2: Project_Manager = Project_Manager(6, "John", ["Wikipedia"])
print(my_project_manager)
print(my_project_manager2)
my_project_manager.add_project("Youtube")
my_project_manager.print_projects()
my_project_manager.add(developer1)
my_project_manager.add(developer2)
my_project_manager.print_employees()
my_project_manager2.add(developer3)
my_project_manager2.add(developer4)
my_project_manager2.print_employees()

my_manager: Manager = Manager(7, "Johnny Doe")
print(my_manager)
my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)
my_manager.print_employees()
class Person():
    def __init__(self, name, gender, age, grade, enemy):
        self.name = name
        self.gender = gender
        self.age = age
        self.grade = grade
        self.enemy = enemy

    def hello(self):
        print(f"Hi, my name is {self.name}")

    def insult(self):
        print(f"Hey {self.enemy} kys loser")

liam = Person("Liam C", "boy", 15, 9, "Jeevan")

liam.hello()
liam.insult()

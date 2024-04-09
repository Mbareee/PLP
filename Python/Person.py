class Person():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"This is {self.name} who is {self.age} years old and is a {self.gender}" )

human = Person("Sheila",29,"girl")
human.introduce()
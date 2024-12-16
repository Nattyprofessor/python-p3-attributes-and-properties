class Human:
    species = "Homo sapiens"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        print("Retrieving age.")
        return self.get_age

    def set_age(self, age):
        if (type(age) in (int, float)) and (0 <= age <= 120):
            print(f"Setting age to { age }")
            self._age = age

        else:
            print("Age must be a number between 0 and 120")

    age = property(get_age, set_age)

    
guido = Human(name="Guido", age=67)
guido.age = 0
print(guido.age)
guido.age = False
print(guido.age)

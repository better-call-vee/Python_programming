class Person:
    def __init__(self, name, age):
        self.naam = name
        self.boyos = age

    def __str__(self):
        return f"Naam: {self.naam}, Boyos: {self.boyos}"


bekti = Person("Tanvee", 23)
print(bekti)

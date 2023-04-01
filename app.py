from Person.Person import Person

class Admin(Person) :
    def __init__(self, name, age) :
        super.__init__(self, name, age) 
        self.name = name
        self.age = age

class Main :
    @staticmethod
    def start() :
        print("Hello")

if __name__ == "__main__" :
    Main.start()
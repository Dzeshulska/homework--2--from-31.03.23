from Person.Person import Person
import Admin1

class User(Person) :
    def __init__(self, name, age, role) :
        super.__init__(self, name, age) 
        self.role = role        

class Main :
    @staticmethod
    def start() :
        admin = Admin1("Kolya", 40, "admin", "hand")
        person = Person("Ivan", 35)
        user = User("Ira", 25, "buyer" )

        print(person.__dict__)
        print(admin.__dict__) 
        print(user.__dict__)       

if __name__ == "__main__" :
    Main.start()



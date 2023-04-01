class Admin1(app.User) :
    def __init__(self, name, age, role, hand) :
        super.__init__(self, name, role,) 
        self.hand = hand       
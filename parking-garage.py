class Pgarage():

    def __init__(self):
       
        pass

    def takeTicket(self):
        pass

    def payforParking(self):
        payment = int(input (f"Hello the cost for parking is $20 dollars"))

        if payment >= 20:
            self.tickets += 1
            self.parking_spaces += 1
            
        else:
            print(f'I am sorry that is not enough.')

        pass

    def leaveGgarage(self):
        pass

    def runner(self):
        pass

    
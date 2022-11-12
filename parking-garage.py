class Pgarage():

    def __init__(self):
       self.amount_of_tickets = [10] # Ashley
       self. parking_spaces = [10] # Ashley
       self.currentTicket = { 'paid': False}

    def takeTicket(self): # Ashley
        return ('Here is your ticket. Have a nice day!')   
        self.amount_of_tickets -= 1 
        self.parking_spaces -= 1 


    def payforParking(self):
        payment = int(input (f"Hello the cost for parking is $20 dollars"))

        if payment >= 20:
            self.tickets += 1
            self.parking_spaces += 1
            self.currentTicket['paid'] == True

        else:
            print(f'I am sorry that is not enough.')
            self.currentTicket['paid'] == False

        pass

    def leaveGarage(self):  # Nick
        if self.currentTicket['paid'] == True:
            return 'Thank you, have nice day!'
        else:
            self.payForParking()
            return 'Thank you, have nice day!'
        self.parkingSpaces += 1
        self.tickets += 1

    def runner(self): # Ashley
        user_ = input('Welcome to my garage. Please start by taking a ticket. (take a ticket) ').lower() 
        if user_ == 'take a ticket': 
            self.takeTicket() 
            self.payforParking()
            self.leaveGgarage()
        else: 
            print('I\'m sorry that is an invalid input. Please try again.') 

    
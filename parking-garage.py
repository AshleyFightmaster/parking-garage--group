class Pgarage():

    def __init__(self):
       self.amount_of_tickets = [1,2,3,4,5,6,7,8,9,10] # Ashley
       self. parking_spaces = [False, False, False, False, False, False, False, False, False, False] # Ashley

    def takeTicket(self): # Ashley
        ticket_number = self.amount_of_tickets.pop()
        self.parking_spaces[ticket_number - 1] = True
        return (f'You have ticket number {ticket_number}.') 
        
    def payforParking(self):
        payment = int(input (f"Hello the cost for parking is $20 dollars"))

        if payment >= 20:
            self.tickets += 1
            self.parking_spaces += 1
            self.paid_ticket[paidfor] == True

        else:
            print(f'I am sorry that is not enough.')
            self.paid_ticket[] == False

        pass

    def leaveGgarage(self):
        pass

    def runner(self): # Ashley
        user_ = input('Welcome to my garage. Please start by taking a ticket. (take a ticket) ').lower() 
        if user_ == 'take a ticket': 
            self.takeTicket() 
            self.payforParking()
            self.leaveGgarage()
        else: 
            print('I\'m sorry that is an invalid input. Please try again.') 

    
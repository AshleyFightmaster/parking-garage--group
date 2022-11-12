 Ashley:
self.amount_of_tickets = [10] 
self. parking_spaces = [10] 

 def.takeTicket(self):
 return ('Here is your ticket. Have a nice day!')   
         self.amount_of_tickets -= 1 
        self.parking_spaces -= 1 

 user_ = input('Welcome to my garage. Please start by taking a ticket. (take a ticket) ').lower() 
        if user_ == 'take a ticket': 
            self.takeTicket() 
            self.payforParking()
            self.leaveGgarage()
        else: 
            print('I\'m sorry that is an invalid input. Please try again.') 
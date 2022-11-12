class Pgarage():

    def __init__(self):

       self.amount_of_tickets = [1,2,3,4,5,6,7,8,9,10] # Ashley
       self. parking_spaces = [False, False, False, False, False, False, False, False, False, False] # Ashley
       self.ticket_number = ''
       self.currentTicket = { 'paid': False}
       self.ticket_Taken = {'parked': False}


    def takeTicket(self): # Ashley
        self.ticket_number = self.amount_of_tickets.pop()
        self.parking_spaces[self.ticket_number - 1] = True
        self.ticket_Taken['parked'] = True
        return (f'You have ticket number {ticket_number}.') 
        
    def payforParking(self):
        payment = int(input (f"Hello the cost for parking is $20 dollars"))

        if payment >= 20:
            
            self.amount_of_tickets[self.ticket_number] += self.ticket_number

            self.currentTicket['paid'] == True

        else:
            print(f'I am sorry that is not enough.')
            self.currentTicket['paid'] == False

        pass

    def leaveGarage(self):  # Nick
        if self.currentTicket['paid'] == True:
            self.parking_spaces[self.ticket_number - 1] = False
            return 'Thank you, have nice day!'
        else:
            self.payForParking()
            return 'Thank you, have nice day!'

    def runner(self): # Ashley
        user_ = input('Welcome to my garage. Please start by taking a ticket. (take a ticket) ').lower() 
        if user_ == 'take a ticket': 
            self.takeTicket() 
        if user_ == 'pay' and self.ticket_Taken['parked'] == True:
            self.payforParking()
        if user_ == 'leave' and self.ticket_Taken['parked'] == True:
            self.leaveGgarage()
        else: 
            print('I\'m sorry that is an invalid input. Please try again.') 

    
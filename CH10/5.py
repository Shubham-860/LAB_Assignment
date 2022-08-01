class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        self.totalSeats = seats
        self.ticket = []

    def getStatus(self):
        print(f"Name os Train {self.name}, and the seats is {self.seats}")

    def getFareInfo(self):
        print("The fare is ", self.fare)

    def bookTickets(self, a):
        if self.seats > 0 and self.seats >= a:
            temp = self.seats - a
            print(f"Your seats has been booked your", end="")
            if a == 1:
                print("seat no is ", self.seats)
            else:
                print("seats no are ", temp, "to", self.seats)
            for i in range(temp, self.seats):
                self.ticket.append(i)
            self.seats = temp
            self.ticket.sort()
        else:
            print("Sorry Train is full")

    def cancel(self, a):
        if a <= (len(self.ticket)):
            if self.totalSeats != self.seats:
                for i in range(a):
                    self.ticket.pop(i)
                self.seats = self.seats + 1
        else:
            print("You are trying to cansel more tickets than your have")


interCity = Train("InterCity Express : 15", 50, 300)
interCity.getStatus()
interCity.getFareInfo()
interCity.bookTickets(3)
interCity.bookTickets(3)
interCity.getStatus()
interCity.cancel(2)
interCity.getStatus()
print(interCity.ticket)

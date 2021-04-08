class abc():
    principal = 0
    amount = 0
    rate = 0
    time = 0
    def getdata(self, principal_amount, rateofinterest, maturityperiod):
        self.principal = principal_amount
        self.rate = rateofinterest
        self.time = maturityperiod

class calculateSI(abc):
    def displaySI(self):
        self.amount = ( self.principal * self.rate * self.time )/100
        print("Simple Interest earned:", self.amount)

class calculateCI(abc):
    def displayCI(self):
        total_amount = (self.principal * (1 + self.rate/100) ** self.time)
        self.amount = total_amount - self.principal
        print("Compound Interest earned:", self.amount)

si = calculateSI()
si.getdata(principal_amount=8000, rateofinterest=2, maturityperiod=2)
si.displaySI()

ci = calculateCI()
ci.getdata(principal_amount=8000, rateofinterest=2, maturityperiod=2)
ci.displayCI()
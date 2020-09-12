class Bankacc():
    def __init__(self,owner_name,Balance):
        self.owner_name = owner_name
        self.Balance = Balance

    def deposit(self,depo):
        self.Balance += depo

    def withdrawn(self,wthdra):
        if (self.Balance > wthdra):
            self.Balance -= wthdra
        else:
            print('Insufficient amount, ',end='')

    def __str__(self):
        return "Your account {}, remaining balance is {}.".format(self.owner_name,self.Balance)


p=Bankacc('Rajat',1000)
p.deposit(200)
p.withdrawn(900)
print(p)

q=Bankacc('Bob',500)
q.deposit(100)
q.withdrawn(700)
print(q)

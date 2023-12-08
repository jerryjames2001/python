class bank:
    def __init__(self,no,nam,typ,ba):
        self.accno=no
        self.name=nam
        self.type=typ
        self.balance=ba
    def display(self):
        print("Account no:\t",self.accno)
        print("Name\t",self.name)
        print("Account type\t",self.type)
        print("Balance\t",self.balance)
    def deposit(self,d):
        self.balance+=d
    def withdraww(self,w):
        if self.balance > w:
            self.balance-=w
        else:
            print("The withdrawal amount is greater than balance")

nu=int(input("Enter account no: "))
na=input("Enter name: ")
typ=input("Enter account type: ")
bal=int(input("Enter current balance"))
obj=bank(nu,na,typ,bal)
obj.display()
dep1=int(input("Enter the ammount to deposit"))
obj.deposit(dep1)
obj.display()
wid=int(input("Enter the withdrawal amount"))
obj.withdraww(wid)
obj.display()
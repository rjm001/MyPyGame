# Account class. Note no def to start it off!
# Errors indicated by "raise" statements

#Note, classes start with capital letters!
#Note, the exception doesn't have to do anything! Just be a class
class AbortTransaction(Exception):
    '''raise this exception to abort a bank transaction'''
    pass


class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = self.validateAmount(balance) #note, you can call methods in the init!
        self.password = password #you could add a password validation to this too !
    
    def validateAmount(self, amount):
        try:
            amount= int(amount)
        except ValueError:
            raise AbortTransaction('Amount must be an integer')
        if amount <= 0:
            raise AbortTransaction('Amount must be positive')
        return amount

    def checkPasswordMatch(self, password):
        if password != self.password:
            raise AbortTransaction('password is wrongo. Wrongo! WrOnGo!! WRONGO!!!!')

    def deposit(self, amountToDeposit):
        amountToDeposit = self.validateAmount(amountToDeposit)
        self.balance = self.balance + amountToDeposit
        return self.balance

    def getBalance(self):
        return self.balance

    def withdraw(self, amountToWithdraw):
        amountToWithdraw = self.validateAmount(amountToWithdraw)#do we have to return the value here? I guess we can, or we could just validate it. What's the advantage of returning it, other than that feature is useful for the constructor?
        if amountToWithdraw > self.balance:
            raise AbortTransaction('You cannot withdraw more than you have in your account') # an alternative would be to allow it but just charge a fee! Like the big banks try to get you to agree to.

        self.balance = self.balance - amountToWithdraw
        return self.balance        
    
    # for debugging. Should be private!
    def show(self):
        print(f'Name: {self.name},')
        print(f'Balance: {self.balance}')
        print(f'Password: {self.password}') #should be a hashed password!

# Bank that manages a dictionary of account objects. Like a 'system' object. That is, this is an "object manager object". It's essentially a platform/manager/system layer. It reflects a real world thing, which makes it sound like a simple idea, but its very powerful! This technique is called composition.
# obviously, in the real world you would want to do input sanitization and have more complicated account numbers and save passwords as hashes.
# Tricky with all these objects: which of the selfs are you referring to! Especiially since the bank deal with account objects! 
# So, watch out for oAccount.self.thing vs. self.thing

from Account import Account, AbortTransaction

class Bank():
    def __init__(self, hours, address, phone):
        self.accountsDict = {}
        self.nextAccountNumber = 0 #key for dictionary of accounts. It looks like we are just doing it from 0, 1, ... .
        self.hours = hours
        self.address = address
        self.phone = phone
    
    def askForValidAccountNumber(self):
        accountNumber = input('What is your account number? ')
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AbortTransaction('The account number must be an integer')
        #note, reusing that AbortTransaction Exception here in two different cases
        if accountNumber not in self.accountsDict:
            raise AbortTransaction('there is no account ' + str(accountNumber))
        return accountNumber
    
    def getUsersAccount(self):
        accountNumber = self.askForValidAccountNumber()
        oAccount = self.accountsDict[accountNumber]
        self.askForValidPassword(oAccount)
        return oAccount
    
    def askForValidPassword(self, oAccount):
        password = input('Please enter your password: ')
        oAccount.checkPasswordMatch(password)
    
    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber #be careful with all the selfs! This is the Bank's self. vs the Accounts' "self"s
        self.accountsDict[newAccountNumber] = oAccount
        self.nextAccountNumber +=1
        return newAccountNumber #note its returning the dictiopnary key! not the object

    def openAccount(self):
        print('*** Open Account ***')
        userName = input("What's your name?")
        userStartingAmount = input("How much money to start?")
        userPassword = input('Choose your password.')
        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print(f"Your new account number is {userAccountNumber}")

    def closeAccount(self):
        print("*** Close Account ***")
        userAccountNumber = self.askForValidAccountNumber() #this includes input validation! nice.
        oAccount = self.accountsDict[userAccountNumber] #better be the right number!
        self.askForValidPassword(oAccount) #note, we are passing the account object to a Bank method!
        theBalance = oAccount.getBalance()
        print(f"you had ${theBalance} in your account, which is being returned to you")
        del self.accountsDict[userAccountNumber] #now that number will never be an account, but that's ok
        print('Your account is now closed.')


    def balance(self):
        print('*** Get Balance ***')
        oAccount = self.getUsersAccount()
        theBalance = oAccount.getBalance()
        print('Your balance is:', theBalance)

    def deposit(self):
        print('*** Deposit ***')
        oAccount = self.getUsersAccount() #it's this order because in Main, first you choose your action, then you give your account. vs the other way. That's something to think about. Shold you choose your action then get your account? I don't know.
        depositAmount = input('Please enter amount to deposit: ')
        theBalance = oAccount.deposit(depositAmount) #the bank manages a deposit through the account
        print('Deposited:', depositAmount)
        print('Your new balance is:', theBalance)

    def withdraw(self):
        print("*** Withdraw ***")
        oAccount = self.getUsersAccount()
        userAmount = input('How much withdrawz?')
        theBalance = oAccount.withdraw(userAmount)
        print(f"Withdrew: {userAmount}. Your new balance is {theBalance}")
    
    def getInfo(self):
        print('Hours:', self.hours)
        print('Address:', self.address)
        print('Phone:', self.phone)
        print('We currently have', len(self.accountsDict), 'account(s) open.')

    # Special method for Bank administrator only
    def show(self):
        print('*** Show ***')
        print('(This would typically require an admin password)')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('Account:', userAccountNumber)
            oAccount.show()
            print()



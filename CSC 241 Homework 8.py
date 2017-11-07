### Assigment 8 Notes

# We want to stimulate a simple ATM machine
# 1.) User will sign in with account to get to the ATM menu (with constant communication
#   a.) The ATM will read the account.txt and make sure there is no IOError accessing the file
#       a1.) The ATM will notify user that the ATM is experiencing problems, and then quit
#   b.) The ATM will prompt user to input ATM 4 digit PIN
#       b1.) The ATM will greet user by name if that user is an account holder,
#       b2.) Print message that indicates 4 pin isnt a current client and quit (No errors)
#   c.) While user does not coose to quit, menu should be repromted without having to reenter code
# 2.) Deposit Option
#   a.) Ask user for the amount to be deposited
#   b.) In case of invalid input, repromt with exception (please enter a numeric value)
#   c.) Update the balance in container and in text file
#   d.) Communicate success of the op
# 3.) Withdraw Option
#   a.) Ask user for the amount to be withdrawn
#       a1.) If  not enough funds available gives the opportunity  to enter different amount
#   b.) In case of invalid input, repromt with exception (please enter a numeric value)
#   c.) Update balance in container and in text file
#   d.) Communicate success
# 4.) Balance Option
#   a.) Shows the current balance of account
# 5.) Quit Option
#   b.) writes new data to accounts.txt then quits

############################################################################################
#containers needed
accountfile = 'accounts.txt'
accounts = {}
run = True

# Sign in
def startUp(accountfile):
    fullaccount = {}
    try:
        infile = open(accountfile,'r+')
    except IOError:
        print('This ATM is experiencing technical difficulties. Please try again later.')
        run = False

    rawAccounts = infile.read().split(' \n')
    #print(rawAccounts)

    for account in rawAccounts:
        account = account.split()
        fullaccount[account[0]] = [account[1]+ ' ' +account[2], (float(account[3]))]
    infile.close()
    return fullaccount

def signIn():
    pin = input('\nPlease enter your 4 digit PIN:\t')
    for k,v in accounts.items():
        if pin == k:
            return pin
            print('\nGreetings', v[0] + '. How can we help you today?')
        else:
            run = False
            print('PIN does not match an account with our bank. Operation Ending.')
            return run
            

def menu():
    menuRun = True
    while(menuRun == True):
        option = input('\n\t1.) Deposit\n \t2.) Withdrawal\n \t3.) View Balance\n \t4.) Quit\n').upper()
        if option == '1' or option[0] == 'D':
            return deposit()
        elif option == '2' or option[0] == 'W':
            return withdrawal()
        elif option == '3' or option[0] == 'B':
            print('\nYour current account balance is:\n$', accounts[matchedPIN][1])
            run = True
            return run
        elif option == '4' or option[0] == 'Q':
            run = False
            return run
    
    
def deposit():
    run = True
    while(run == True):
        try:
            deposit = eval(input('How much would you like to deposit?\t'))
            accounts[matchedPIN][1] += deposit
            print('\nThe deposit was successful. Your current balance is:\n$', accounts[matchedPIN][1])
            run = False
        except:
            print('Please enter a numeric value. Ex: 200.00 or 200')
            run = True
        
def withdrawal():
    run = True
    while(run == True):
        try:
            withdraw = eval(input('How much would you like to withdraw?\t'))
            if accounts[matchedPIN][1] - withdraw > 0:
                accounts[matchedPIN][1] -= withdraw
                print('\nThe withdrawal was successful. Your current balance is:\n$', accounts[matchedPIN][1])
                run = False
            else:
                repeat = input('Insufficent Funds. Would you like to try another amount? Y/N').upper()
                if repeat == 'Y':
                    run = True
                elif repeat == 'N':
                    run = False    
        except:
            print('Please enter a numeric value. Ex: 200.00 or 200')
            run = True

def closingTime(accounts):
    infile = open(accountfile,'w')
    for k,v in accounts.items():
        line = (k +' ' + v[0] + ' ' + str(v[1]) + '\n')
        infile.write(line)
    infile.close()
            
    
print('Welcome to the CSC 241 Bank ATM.')
accounts = startUp(accountfile)
matchedPIN = signIn()
if matchedPIN == False:
    run = False
else:
    while(run == True):
        option = menu()
        if option == False:
            closingTime(accounts)
            print('Thank you for using CSC 241 Bank! Have a good day!')
            break
        else:
            print('\nIs there anything else we can help you with today?')


        

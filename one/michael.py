'''
Written by Michael T  for CSB2019
Contains functions which takes user inputs to update bank balance
'''
def display_balance(balance):
    print(f'\nyou currently have {balance} drachma\n')
    return balance

def deposit(balance):
    print('how many drachma are you depositing today? ')
    amount = val_amount()
    print(f'Depositing {amount} today.')
    total_balance = (balance + amount)
    print(f'You now have {total_balance} drachma.\n')
    return total_balance
        
def val_amount():
    while True:
        amount = input("Enter amount: ")
        try:
            val = round(float(amount), 2)
            if val >= 0:
                break
            else:
                print("Amount can't be negative, try again")
        except ValueError:
            print("Amount must be a number, try again")
    return val

def withdraw(balance):  
    print(f'how many drachma would you like to withdraw today?\nEnter 0 to return to main menu\nYou currently have {balance} drachma')
    amount = val_amount()
    if amount <= balance:
        new_balance = balance - amount
        print(f'Your balance is now::{new_balance}\n')
        return new_balance
    elif amount == 0:
        print('Returning to main menu\n')
        return balance
        display_menu()
    else:
        print('No cash money\n')
        return 0
        withdraw(balance)


def display_menu():
    balance = float(0.00)

    while True:
        menu = ['balance', 'deposit', 'withdraw', 'exit']
        print('please pick one of the following')
        for x in menu:
            print(x)
        userinput = input('\n')
        
        if userinput == 'balance':
            display_balance(balance)
            amount = 0
        elif userinput == 'deposit':
            balance = deposit(balance)
            amount = 0
        elif userinput == 'withdraw':
            balance =withdraw(balance)
            amount = 0
        elif userinput == 'exit':
            print('\nthanks for using this app.\nexitting now.')
            break
        else:
            print('\nunknown choice\nplease select again\n')

display_menu()
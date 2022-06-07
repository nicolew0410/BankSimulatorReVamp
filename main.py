import random #Used for generating ID Number.

#The start of the simulation. This gives context to the user on the purpose of the project mostly aimed at those who have never experienced going to the bank.
print("Welcome to the Bank Simulator! For demonstration purposes, this program is designed to gain insight into what it looks like to manage your own bank account just like in real life!")
print("Please answer the following questions to the best of your ability. After that, you will be able to access and input your financial information shortly.")
print()

accountName = str(input("Enter your full name for your account:  "))
print()

#Function "greet" with a parameter of "message" for customization used to repeat in greeting the user hello and goodbye.
def greet(message):
  print("Hello, " + accountName + ', ' + message)
  print()
greet("welcome to the Aria Bank. Thank you for opening an account with us. " )
  
#Basic data by the user is collected and stored in custom variables with a string requirement.
accountBirthDate = str(input("Enter your birth date Ex: 04/12/2010:  "))
print()
accountUsername = str(input("Please enter a username for your account for future use:  "))
print()
accountPassword = str(input("Please enter a password for your account for future use:  "))
print()
print("Thank you for answering our questions. We will now create a ID for you...")

userIDNumber = random.randint(100000000000,999999999999)
print(str(userIDNumber) + " is your ID Number.")

print()
print("NOTE: Please do not use any commas throughout this simulation. ")
#Float requirement allows decimals which mimics the amount of cents in USD currency.
userBalance = float(input("Enter Starting Balance: $"))
print()

#The user has 4 options from a list to choose from in the Bank Simulation. This will later be a confirmation message to the user.
print("Choose from four options: ")
bankActions = ["1. Withdraw", "2. Deposit","3. Information", "4. Exit"]

#A function to hold code that would be repeated at the end of each option to guide the user back to the main menu.
def resetMenu():
    print()
    print(mainMenuAction)
    for x in bankActions:
      print(x)
for x in bankActions:
  print(x)
  mainMenuAction = ("Going back to menu page...")
#While loop ensures the continuation of the program until the user chooses to exit.
while mainMenuAction != "yes" or "Yes":
  userChooseAction = input("Choose [1|2|3|4]: ")
  #User chooses an action (ex: bankActions[0] is 1. Withdraw) from the list with a case sensitive submission. If statement checks if they match and will enact the action according to the user's input.
  if userChooseAction == "1":
    print()
    withdrawAmount = float(input("How much do you want to withdraw? $"))
    userBalance = (userBalance - withdrawAmount)
    #String requirement combined with the round function allows the program to keep it to the tenths place (similar to pennies). 
    print("Your current balance is $" +   str(round(userBalance,2)))
    resetMenu()

    
  if userChooseAction == "2":
    print()
    depositAmount = float(input("How much do you want to deposit? $"))
    userBalance = (userBalance + depositAmount)
    print("Your current balance is $" +   str(round(userBalance,2)))
    resetMenu()

  if userChooseAction == "3":
    print()
    checkAccountUser = input("What is your username?  ")
    #If statements check the user's identity by matching usernames and passwords. 
    if checkAccountUser == accountUsername:
      checkAccountPassword = input("What is your password?  ")
      if checkAccountPassword == accountPassword:
        print("Success!")
        print()
        print(str(userIDNumber) + " is your ID Number.")
        print("Your account name is under " + accountName + ".")
        print("Your birthday is on " + accountBirthDate + ". Don't forget to redeem your $10 gift card on that day! Read more information about it in our Terms and Conditions.")
        print()
        print("Your current balance is $" + str(round(userBalance,2)))
        resetMenu()
      #Else statements of failure are shown when the usernames and passwords do NOT match.
      else:
        print("Login does not match with our system. Please try again.")
        resetMenu()
    else:
      print("Login does not match with our system. Please try again.")
      resetMenu()

      
  if userChooseAction == "4":
    print()
    print("Your final balance is $" + str(round(userBalance,2)))
    greet("thank you for coming to Aria Bank. Enjoy your day!" )
    quit(0)
income = []
expenses = []

total = income + expenses

while True:
    menu = int(input(
    "Welcome to Your Personal Finance Tracker \n" 
    "1. Add Income \n" 
    "2. Add expense \n" 
    "3. View Balance \n" 
    "4. Exit \n"
    ))



    
    if menu == 1:



        while True:
            incomes = input("What is giving you money?")
            incoming = int(input("How much money is coming?"))

            income.append ([incomes, incoming])

        

            another = input("Would you like to enter another input? y/n")
            if another.lower() == "n":  #lower() returns sting in lower case
                break
        

    elif menu == 2:

        while True:
        
            expense = input("What are you spending money on ")
            spending = int(input("How much is the item?"))

            expenses.append([expense, spending])

            another = input("Would you like to enter another input? y/n")

            if another.lower() == "n":
                break


    elif menu == 3:
        print(income)
        print(expenses)



    elif menu == 4:

        print("Goodbye.")
        break

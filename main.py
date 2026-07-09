print("===== Welcome to the Expense Tracker!=====")
option = int(input(" 1. to add expense.\n 2. to view expense\n 3. to exit\nEnter your option: "))

if option == 1:
    print("You have selected to add an expense.")
elif option == 2:
    print("You have selected to view expenses.")
elif option == 3:
    print("Exiting the Expense Tracker. Goodbye!")
else :
    print("Invalid option selected. Please try again.")

expenses = []
match option:
    case 1:
        
       
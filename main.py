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

expenses = {}


def add_expense():
    expense_name = input("Enter the name of the expense: ").lower()
    expense_category = input("Enter the category of the expense: ").lower()
    expense_amount = float(input("Enter the amount of the expense: "))
   
    expenses[expense_category] = {"Expense Name": expense_name, "Expense Amount": expense_amount}
    print(f"Expense of {expense_name} added successfully!")
   

def view_expense():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("Expenses:")
        for category, details in expenses.items():
            print(f"Category: {category}, Expense Name: {details['Expense Name']}, Amount: {details['Expense Amount']}")
        
def exit_program():
    print("Exiting the Expense Tracker. Goodbye!")
    exit()
    
match option:
    case 1:
        add_expense()   
    case 2:
        view_expense()
    case 3:
        exit_program()


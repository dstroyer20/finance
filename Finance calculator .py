def get_income():
    income = float(input("Welcome to the finance app. What is your yearly income?\n"))
    print(f"Just to confirm, your yearly income is ${income}, right?")
    confirmation = str(input())
    while not confirmation == "Yes":
        income = input("Please put in your income\nIncome: ")
        confirmation = input(f"Your yearly income is ${income}, right?\n")
    return float(income)

#Store the get_income function to get savings
    
income = get_income()

def get_expenses():
    expenses = float(input("Enter your yearly expenses: "))
    print(f"${expenses} is your yearly expense?")
    confirmation = str(input())
    while not confirmation == "Yes":
        expenses = input("Please put in your expenses")
        confirmation = input(f"Your yearly expenses  are ${expenses}, right?")
    return float(expenses)

#Store get savings function to expenses 
expenses = get_expenses()

def get_savings():
    savings = income - expenses
    return float(savings)

savings = get_savings()
print(f"With your income of ${income} and expenses of ${expenses}, I calculate your savings to be ${savings}")



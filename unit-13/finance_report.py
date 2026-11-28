import math 

# Monthly financial information 
monthly_income = 150000

rent = 30000
food = 25000
transport = 15000
internet = 5000
electricity = 10000

# calculate total expenses
expenses = [rent, food, transport, internet, electricity]
total_expenses = sum(expenses)

# calculate remaining balance
balance = monthly_income - total_expenses

# calculate average expense
average_expense = round(total_expenses / len(expenses), 2)

# Calculate daily spending budget
daily_budget = math.floor(balance / 30)

# Generate financial report 
print("========== MONTHLY FINANCIAL REPORT ==========")
print(F"Monthly Income: $ {monthly_income:,.2f}")
print(f"Total Expenses: $ {total_expenses:,.2f}")
print(f"Remaining Balance: $ {balance:,.2f}")
print(f"Average Expense: $ {average_expense:,.2f}")
print(f"Daily Spending Budget: $ {daily_budget:,.2f}")
print("=====================================")

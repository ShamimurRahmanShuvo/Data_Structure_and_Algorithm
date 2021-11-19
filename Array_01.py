expenses = [2200, 2350, 2600, 2130, 2190]

# In Feb, how many dollars you spent extra compare to January?
extra_expense = expenses[1] - expenses[0]
print("Extra Expense in February= $",extra_expense)

# Total expense in 1st quarter?
expense_quarter = expenses[0] + expenses[1] + expenses[2]
print("Total expense in first quarter = $", expense_quarter)

# Find out if you spent exactly 2000 in any month?
found = 2000 in expenses
print("Did I spent 2000 in any month?",found)

# Add 1980 as june expense
expenses.append(1980)
print("First 6months of expense = ", expenses)

# Get 200$ refund in April
expenses[3] = expenses[3] - 200
print("Updated list of expenses = ", expenses)
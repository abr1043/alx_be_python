# prompt user for income and expenses
income = float(input("enter your monthly income: "))
expenses = float(input("enter your monthly total expenses: "))

# calculate monthly savings
monthly_savings = income - expenses

# annual projection with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# output the result
print(f"your monthly savings are ${monthly_savings:.2f}.")
print(f"projected savings after one year, with interest is: ${projected_savings}:.2f}.")

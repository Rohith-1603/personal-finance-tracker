import datetime


def main():
    incomes = []
    expenses = []
    budget = {}  # dict of (month, year): amount

    print("=== Personal Finance Tracker ===")

    while True:
        print("\nMenu:")
        print("1. Set Budget")
        print("2. Add Income")
        print("3. Add Expense")
        print("4. View All Incomes")
        print("5. View All Expenses")
        print("6. Show Summary")
        print("7. View Monthly Report")
        print("8. Exit")

        choice = input("Enter your choice: ")

        
        if choice == '1':
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year (e.g., 2023): "))
            while True:
                amount = float(input("Enter your monthly budget: "))
                if amount <= 0:
                    if amount == 0:
                        print("Please enter value.")
                    else:
                        print("Please enter positive values.")
                else:
                    break
            budget[(month, year)] = amount
            print(f"Budget set to {amount} for {month:02d}-{year}")

        
        elif choice == '2':
            while True:
                amount = float(input("Enter income amount: "))
                if amount <= 0:
                    if amount == 0:
                        print("Please enter value.")
                    else:
                        print("Please enter positive values.")
                else:
                    break
            source = input("Enter income source: ")
            date_str = input("Enter date (dd-mm-yyyy) or press enter for today: ")
            if not date_str:
                date = datetime.date.today()
            else:
                date = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
            incomes.append({"amount": amount, "source": source, "date": date})
            print(" Income added successfully!")

        
        elif choice == '3':
            while True:
                amount = float(input("Enter expense amount: "))
                if amount <= 0:
                    if amount == 0:
                        print("Please enter value.")
                    else:
                        print("Please enter positive values.")
                else:
                    break
            category = input("Enter expense category : ")
            date_str = input("Enter date (dd-mm-yyyy) or press enter for today: ")
            if not date_str:
                date = datetime.date.today()
            else:
                date = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
            expenses.append({"amount": amount, "category": category, "date": date})
            print("Expense added successfully!")

        
        elif choice == '4':
            print("\n=== All Incomes ===")
            if not incomes:
                print("No incomes added yet.")
            else:
                for i, income in enumerate(incomes, start=1):
                    print(f"{i}. {income['source']} - {income['amount']} - {income['date'].strftime('%d-%m-%Y')}")

        
        elif choice == '5':
            print("\n=== All Expenses ===")
            if not expenses:
                print("No expenses added yet.")
            else:
                for i, expense in enumerate(expenses, start=1):
                    print(f"{i}. {expense['category']} - {expense['amount']} - {expense['date'].strftime('%d-%m-%Y')}")

        
        elif choice == '6':
            total_income = sum(i["amount"] for i in incomes)
            total_expense = sum(e["amount"] for e in expenses)
            total_budget = sum(budget.values()) if budget else 0
            remaining = total_budget - total_expense if budget else "No budget set"

            print("\n------ Summary ------")
            if budget:
                print("Set Budgets:")
                for (m, y), amt in sorted(budget.items()):
                    print(f"  {m:02d}-{y}: {amt}")
            else:
                print("Set Budget: No budget set")
            print(f"Total Income: {total_income}")
            print(f"Total Expense: {total_expense}")
            print(f"Remaining Budget: {remaining}")
            print("---------------------")

            if total_expense > total_income:
                print(" Warning: You spent more than you earned!")
            if budget and total_expense > total_budget:
                print(" Warning: You exceeded your total budget limit!")

        
        elif choice == '7':
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year (e.g., 2023): "))
            monthly_incomes = [i for i in incomes if i['date'].month == month and i['date'].year == year]
            monthly_expenses = [e for e in expenses if e['date'].month == month and e['date'].year == year]
            total_monthly_income = sum(i["amount"] for i in monthly_incomes)
            total_monthly_expense = sum(e["amount"] for e in monthly_expenses)
            monthly_budget = budget.get((month, year), 0)
            remaining = monthly_budget - total_monthly_expense if monthly_budget else "No budget set"

            print(f"\n------ Monthly Report for {month:02d}-{year} ------")
            print(f"Set Budget: {monthly_budget if monthly_budget else 'No budget set'}")
            print(f"Total Income: {total_monthly_income}")
            print(f"Total Expense: {total_monthly_expense}")
            print(f"Remaining Budget: {remaining}")
            print("---------------------")

            if total_monthly_expense > total_monthly_income:
                print(" Warning: You spent more than you earned this month!")
            if monthly_budget and total_monthly_expense > monthly_budget:
                print(" Warning: You exceeded your budget limit this month!")

        
        elif choice == '8':
            print("Thank you for using the Finance Tracker!")
            break

        else:
            print(" Invalid choice, please try again.")


if __name__ == "__main__":
    main()

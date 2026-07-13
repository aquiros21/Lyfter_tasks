class Category:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {"name": self.name}
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"])


class Transaction:
    def __init__(self, title, amount, category):
        if not isinstance (title, str) or title.strip() == "":
            raise ValueError("Title can't be blank")
        self.title = title
        if not isinstance (amount, (int, float)):
            raise ValueError ("Please enter numbers only")
        if amount <= 0:
            raise ValueError ("Please enter positive numbers only")
        self.amount = amount
        self.category = category

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category.to_dict(),
            "type": type(self).__name__
        }
    
    @classmethod
    def from_dict(cls, data):
        category = Category.from_dict(data["category"])
        if data["type"] == "Expense":
            return Expense(data["title"], data["amount"], category)
        elif data["type"] == "Income":
            return Income(data["title"], data["amount"], category)
        else:
            raise ValueError("Unknown transaction type")



class Expense(Transaction):
    def signed_amount(self):
        return -self.amount 


class Income(Transaction):
    def signed_amount(self):
        return +self.amount
    

class FinanceManager:
    def __init__(self):
        self.categories = []
        self.transactions = []
    
    def add_category(self, name):
        for existing_category in self.categories:
            if name.lower().strip() == existing_category.name.lower():
                raise ValueError("This is an existing category already")
        else: 
            self.categories.append(Category(name))

    def add_expense(self, title, amount, category_name):
        if not self.categories:
            raise ValueError("No categories available.  Please add a category first.")
        
        matched_category = None
        for existing_category in self.categories:
            if existing_category.name.lower() == category_name.lower():
                matched_category = existing_category
                break
        else: 
            raise ValueError("No Category found")
        
        self.transactions.append(Expense(title, amount, matched_category))

    def add_income(self, title, amount, category_name):
        if not self.categories:
            raise ValueError("No categories available.  Please add a category first.")
        
        matched_category = None
        for existing_category in self.categories:
            if existing_category.name.lower() == category_name.lower():
                matched_category = existing_category
                break
        else: 
            raise ValueError("No Category found")
        
        self.transactions.append(Income(title, amount, matched_category))

    def get_total_income(self):
        total = 0
        for transaction in self.transactions:
            if isinstance(transaction, Income):
                total += transaction.signed_amount()
        return total
    
    def get_total_expenses(self):
        total = 0
        for transaction in self.transactions:
            if isinstance(transaction, Expense):
                total += transaction.amount
        return total       
    
    def get_balance(self):
        return self.get_total_income() - self.get_total_expenses()






















if __name__ == "__main__":
    food = Category("Food")
    print(food.name)

    manager = FinanceManager()
    manager.add_category("Food")
    manager.add_category("Transport")
    for c in manager.categories:
        print(c.name)

    manager.add_expense("Groceries", 50, "Food")
    manager.add_income("Salary", 1000, "Food")

    for t in manager.transactions:
        print(t.title, t.amount, t.category.name, t.signed_amount())
    
    print(manager.get_total_income())
    print(manager.get_total_expenses())
    print(manager.get_balance())
    print(food.to_dict())

    original = Expense("Groceries", 50, food)
    saved = original.to_dict()
    print(saved)

    rebuilt = Transaction.from_dict(saved)
    print(rebuilt.title, rebuilt.amount, rebuilt.category.name, rebuilt.signed_amount())
import json
from logic import Category, Transaction,FinanceManager

def save_data(manager, filename):
    categories_data = []
    for category in manager.categories:
        categories_data.append(category.to_dict())

    transactions_data = []
    for transaction in manager.transactions:
        transactions_data.append(transaction.to_dict())

    all_data = {
        "categories": categories_data,
        "transactions": transactions_data
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=4)


def load_data(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            all_data = json.load(f)

        manager = FinanceManager()

        for category_dict in all_data["categories"]:
            rebuilt_category = Category.from_dict(category_dict)
            manager.categories.append(rebuilt_category)

        for transaction_dict in all_data["transactions"]:
            rebuilt_transaction = Transaction.from_dict(transaction_dict)
            manager.transactions.append(rebuilt_transaction)

        return manager
    
    except FileNotFoundError:
        return FinanceManager()



if __name__ == "__main__":
    new_manager = load_data("nonexistent_file.json")
    print(new_manager.categories)
    print(new_manager.transactions)
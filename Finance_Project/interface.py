import os
import FreeSimpleGUI as sg
from logic import FinanceManager
from persistence import save_data, load_data

DATA_FILENAME = "finance_data.json"

CATEGORY_NAME_KEY = '-CATEGORY_NAME-'
TITLE_KEY = '-TITLE-'
AMOUNT_KEY = '-AMOUNT-'
CATEGORY_KEY = '-CATEGORY-'
TABLE_KEY = '-TABLE-'
TOTAL_INCOME_KEY = '-TOTAL_INCOME-'
TOTAL_EXPENSES_KEY = '-TOTAL_EXPENSES-'
BALANCE_KEY = '-BALANCE-'

SUBMIT_BUTTON = "Submit"
CANCEL_BUTTON = "Cancel"
ADD_CATEGORY_BUTTON = "Add Category"
ADD_EXPENSE_BUTTON = "Add Expense"
ADD_INCOME_BUTTON = "Add Income"

script_folder = os.path.dirname(__file__)
data_file_path = os.path.join(script_folder, DATA_FILENAME)

manager = load_data(data_file_path)


def open_add_category_window():
    category_layout = [
        [sg.Text("Enter category name:")],
        [sg.Input(key=CATEGORY_NAME_KEY)],
        [sg.Button(SUBMIT_BUTTON), sg.Button(CANCEL_BUTTON)]
    ]
    category_window = sg.Window("Add Category", category_layout)

    while True:
        cat_event, cat_values = category_window.read()
        if cat_event in (sg.WIN_CLOSED, CANCEL_BUTTON):
            category_window.close()
            return None
        elif cat_event == SUBMIT_BUTTON:
            category_window.close()
            return cat_values[CATEGORY_NAME_KEY]


def open_transaction_window(transaction_type):
    category_names = []
    for category in manager.categories:
        category_names.append(category.name)

    transaction_layout = [
        [sg.Text("Title:")],
        [sg.Input(key=TITLE_KEY)],
        [sg.Text("Amount:")],
        [sg.Input(key=AMOUNT_KEY)],
        [sg.Text("Category:")],
        [sg.Combo(category_names, key=CATEGORY_KEY, readonly=True)],
        [sg.Button(SUBMIT_BUTTON), sg.Button(CANCEL_BUTTON)]
    ]

    transaction_window = sg.Window(f"Add {transaction_type}", transaction_layout)

    while True:
        trans_event, trans_values = transaction_window.read()
        if trans_event in (sg.WIN_CLOSED, CANCEL_BUTTON):
            transaction_window.close()
            return None
        elif trans_event == SUBMIT_BUTTON:
            transaction_window.close()
            return {
                "title": trans_values[TITLE_KEY],
                "amount": trans_values[AMOUNT_KEY],
                "category": trans_values[CATEGORY_KEY]
            }


def parse_amount(amount_text):
    try:
        return float(amount_text)
    except ValueError:
        raise ValueError("Amount must be a valid number")


def build_table_rows():
    rows = []
    for transaction in manager.transactions:
        rows.append([transaction.title, transaction.amount, transaction.category.name, type(transaction).__name__])
    return rows


def run_app():
    layout = [
        [sg.Text("Personal Finance Tracker")],
        [sg.Table(values=build_table_rows(), headings=["Title", "Amount", "Category", "Type"], key=TABLE_KEY, auto_size_columns=True, expand_x=True, num_rows=10)],
        [sg.Text(f"Income: {manager.get_total_income()}", key=TOTAL_INCOME_KEY),
        sg.Text(f"Expenses: {manager.get_total_expenses()}", key=TOTAL_EXPENSES_KEY),
        sg.Text(f"Balance: {manager.get_balance()}", key=BALANCE_KEY)],
        [sg.Button(ADD_CATEGORY_BUTTON), sg.Button(ADD_EXPENSE_BUTTON), sg.Button(ADD_INCOME_BUTTON)]
    ]

    window = sg.Window("Finance Tracker", layout)

    def refresh_table():
        window[TABLE_KEY].update(values=build_table_rows())

    def refresh_totals():
        window[TOTAL_INCOME_KEY].update(f"Income: {manager.get_total_income()}")
        window[TOTAL_EXPENSES_KEY].update(f"Expenses: {manager.get_total_expenses()}")
        window[BALANCE_KEY].update(f"Balance: {manager.get_balance()}")

    def save():
        save_data(manager, data_file_path)

    def handle_add_category():
        new_category_name = open_add_category_window()
        if new_category_name is not None:
            try:
                manager.add_category(new_category_name)
                save()
            except ValueError as e:
                sg.popup(str(e))

    def handle_add_expense():
        new_expense = open_transaction_window("Expense")
        if new_expense is not None:
            try:
                amount = parse_amount(new_expense["amount"])
                manager.add_expense(new_expense["title"], amount, new_expense["category"])
                refresh_table()
                refresh_totals()
                save()
            except ValueError as e:
                sg.popup(str(e))

    def handle_add_income():
        new_income = open_transaction_window("Income")
        if new_income is not None:
            try:
                amount = parse_amount(new_income["amount"])
                manager.add_income(new_income["title"], amount, new_income["category"])
                refresh_table()
                refresh_totals()
                save()
            except ValueError as e:
                sg.popup(str(e))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == ADD_CATEGORY_BUTTON:
            handle_add_category()
        elif event == ADD_EXPENSE_BUTTON:
            handle_add_expense()
        elif event == ADD_INCOME_BUTTON:
            handle_add_income()

    window.close()


if __name__ == "__main__":
    run_app()
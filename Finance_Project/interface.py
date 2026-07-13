import FreeSimpleGUI as sg
from logic import FinanceManager
from persistence import save_data, load_data

manager = load_data("finance_data.json")


def open_add_category_window():
    category_layout = [
        [sg.Text("Enter category name:")],
        [sg.Input(key='-CATEGORY_NAME-')],
        [sg.Button("Submit"), sg.Button("Cancel")]
    ]
    category_window = sg.Window("Add Category", category_layout)

    while True:
        cat_event, cat_values = category_window.read()
        if cat_event in (sg.WIN_CLOSED, "Cancel"):
            category_window.close()
            return None
        elif cat_event == "Submit":
            category_window.close()
            return cat_values['-CATEGORY_NAME-']


def open_add_expense_window():
    category_names = []
    for category in manager.categories:
        category_names.append(category.name)

    expense_layout = [
        [sg.Text("Title:")],
        [sg.Input(key='-EXPENSE_TITLE-')],
        [sg.Text("Amount:")],
        [sg.Input(key='-EXPENSE_AMOUNT-')],
        [sg.Text("Category:")],
        [sg.Combo(category_names, key='-EXPENSE_CATEGORY-')],
        [sg.Button("Submit"), sg.Button("Cancel")]
    ]

    expense_window = sg.Window("Add Expense", expense_layout)

    while True:
        exp_event, exp_values = expense_window.read()
        if exp_event in (sg.WIN_CLOSED, "Cancel"):
            expense_window.close()
            return None
        elif exp_event == "Submit":
            expense_window.close()
            return {
                "title": exp_values['-EXPENSE_TITLE-'],
                "amount": exp_values['-EXPENSE_AMOUNT-'],
                "category": exp_values['-EXPENSE_CATEGORY-']
            }


def open_add_income_window():
    category_names = []
    for category in manager.categories:
        category_names.append(category.name)

    income_layout = [
        [sg.Text("Title:")],
        [sg.Input(key='-INCOME_TITLE-')],
        [sg.Text("Amount:")],
        [sg.Input(key='-INCOME_AMOUNT-')],
        [sg.Text("Category:")],
        [sg.Combo(category_names, key='-INCOME_CATEGORY-')],
        [sg.Button("Submit"), sg.Button("Cancel")]
    ]

    income_window = sg.Window("Add Income", income_layout)

    while True:
        inc_event, inc_values = income_window.read()
        if inc_event in (sg.WIN_CLOSED, "Cancel"):
            income_window.close()
            return None
        elif inc_event == "Submit":
            income_window.close()
            return {
                "title": inc_values['-INCOME_TITLE-'],
                "amount": inc_values['-INCOME_AMOUNT-'],
                "category": inc_values['-INCOME_CATEGORY-']
            }


def build_table_rows():
    rows = []
    for transaction in manager.transactions:
        rows.append([transaction.title, transaction.amount, transaction.category.name, type(transaction).__name__])
    return rows


layout = [
    [sg.Text("Personal Finance Tracker")],
    [sg.Table(values=build_table_rows(), headings=["Title", "Amount", "Category", "Type"], key='-TABLE-', auto_size_columns=True, expand_x=True, num_rows=10)],
    [sg.Button("Add Category"), sg.Button("Add Expense"), sg.Button("Add Income")]
]

window = sg.Window("Finance Tracker", layout)

def refresh_table():
    window['-TABLE-'].update(values=build_table_rows())


def save():
    save_data(manager, "finance_data.json")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Add Category":
        new_category_name = open_add_category_window()
        if new_category_name is not None:
            try:
                manager.add_category(new_category_name)
                save()
            except ValueError as e:
                sg.popup(str(e))
    elif event == "Add Expense":
        new_expense = open_add_expense_window()
        if new_expense is not None:
            try:
                manager.add_expense(new_expense["title"], float(new_expense["amount"]), new_expense["category"])
                refresh_table()
                save()
            except ValueError as e:
                sg.popup(str(e))
    elif event == "Add Income":
        new_income = open_add_income_window()
        if new_income is not None:
            try:
                manager.add_income(new_income["title"], float(new_income["amount"]), new_income["category"])
                refresh_table()
                save()
            except ValueError as e:
                sg.popup(str(e))

window.close()







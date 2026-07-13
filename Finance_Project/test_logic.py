import unittest
from logic import Category , Transaction, Expense, Income, FinanceManager

class TestCategory(unittest.TestCase):
    
    def test_category_stores_name(self):
        food = Category("Food")
        self.assertEqual(food.name, "Food")


class TestTransaction(unittest.TestCase):

    def test_transaction_rejects_non_numerics(self):
        food = Category("Food")
        with self.assertRaises(ValueError):
            Transaction("Groceries", "twenty", food)

    def test_transaction_negative_number(self):
        food = Category("Food")
        with self.assertRaises(ValueError):
            Transaction("Groceries", -50, food)

    def test_transaction_with_blank_title(self):
        food = Category("food")
        with self.assertRaises(ValueError):
            Transaction("   ", 50, food)

    def test_expense_produces_negative_number(self):
        food = Category("food")
        rent = Expense("Rent", 50, food)
        self.assertEqual(rent.signed_amount(), -50)

    def test_income_produces_positive_number(self):
        food = Category("food")
        salary = Income("Salary", 1000, food)
        self.assertEqual(salary.signed_amount(), 1000)


class TestFinanceManager(unittest.TestCase):
    
    def test_add_category_rejects_duplicate(self):
        manager = FinanceManager()
        manager.add_category("Food")
        with self.assertRaises(ValueError):
            manager.add_category("food")

    def test_add_expense_with_no_categories(self):
        manager = FinanceManager()
        with self.assertRaises(ValueError):
            manager.add_expense("Groceries", 50, "Food")



if __name__ == '__main__':
    unittest.main()
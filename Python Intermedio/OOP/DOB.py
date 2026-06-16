from datetime import date

def check_legal_age(func):
    def wrapper(user):
        if user.age < 18:
            raise ValueError(f"This user is not of legal age")
        return func(user)
    
    return wrapper


class User:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth


    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
    

@check_legal_age
def welcome_user(user):
    return f"Welcome {user.name}."

user1 = User("Adrian", date(2000, 10, 21))
user2 = User("Andres", date(2010, 10, 21))

print(welcome_user(user1))
print(welcome_user(user2))


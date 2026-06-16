def check_numb(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError (f"'{arg}' is not a number")
            
        result = func(*args) 
        return result
			
    return wrapper

@check_numb
def test_func(*args):
    return args

result = test_func(5,6,7,8,9,"hello")
print(result)
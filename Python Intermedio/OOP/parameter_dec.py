def print_param (func):
    def wrapper(*args , **kwargs):
        print(args , kwargs)

        result = func(*args, **kwargs) 
        print(result)

        return result

    return wrapper


@print_param
def test_func(*args , **kwargs):
    return "hello"

test_func("hello", "good bye", greeting = "tal cosa")
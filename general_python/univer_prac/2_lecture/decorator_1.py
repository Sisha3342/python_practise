def my_decorator(func):
    def the_wrapper(*args):
        print("Parameters:", *args)
        result = func(*args)
        print("Result:", result)
        return result
    return the_wrapper

def my_sum(*args):
    result = 0
    for i in args:
        result += i
    return result

if __name__ == '__main__':
    my_sum = my_decorator(my_sum)
    a = my_sum(1, 2, 3)

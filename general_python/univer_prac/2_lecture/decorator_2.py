from enum import Enum
class To_display(Enum):
    ONLY_ARG = 1
    ONLY_RES = 2
    ARG_RES = 3

def my_decorator(func, To_display):
    def the_wrapper(*args):
        result = func(*args)
        if To_display == To_display.ONLY_ARG:
            print("Parameters:", *args)
        elif To_display == To_display.ONLY_RES:
            print("Result:", result)
        else:
            print("Parameters:", *args)
            print("Result:", result)
        return result
    return the_wrapper

def my_sum(*args):
    result = 0
    for i in args:
        result += i
    return result

if __name__ == '__main__':
   my_sum = my_decorator(my_sum, To_display.ARG_RES)
   a = my_sum(1, 2, 3)

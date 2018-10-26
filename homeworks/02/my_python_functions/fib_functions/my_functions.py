def simple_decorator(function):
    def check_func(arg):
        if arg <= -1:
            raise Exaption
        else: return function(arg)
    return check_func

    
@simple_decorator
def fib(n):
    if n == 0:
        return 0
    if n<3:
        return 1
    return fib(n-1) + fib(n-2)
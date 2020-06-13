def decorator_with_params(*args,**kwargs):
    print('')
    print('arguments for decorator_with_params is '+str(args))
    print('keyword arguments for decorator_with_params is '+str(kwargs))
    def decorator_fun(f):
        def wrapper(*args,**kwargs):
            print('')
            print('inside decorator function')
            print('args are '+str(args))
            return f(*args,**kwargs)
        return wrapper
    return decorator_fun


@decorator_with_params(name='testing decorators')
def func1(a,b):
    print ("sum is : " + str(a+b) )


func1(90,20)

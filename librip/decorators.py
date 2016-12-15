def print_result(func_to_decorat):
    def decorated_func(*args):
        print(func_to_decorat.__name__)
        a=func_to_decorat(*args)
        if type(a) == list:
            for i in a: print(i)
        elif type(a) == dict:
            for i in a.keys(): print("{0} = {1}".format(i, a[i]))
        else: print(a)
        return a
    return decorated_func

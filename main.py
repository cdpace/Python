class mydeco:

    def __init__(self, arg):
        self.arg = arg
        pass
    
    def __call__(self,func):
        def wrap(name):
            print(f'arg is {self.arg}')
            print('before')
            func(name)
            print('after')
        return wrap


@mydeco('test')
def my_func(name):
    print(f'hello {name}')


my_func('Chris')
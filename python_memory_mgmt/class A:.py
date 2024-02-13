class A:
    a = 1
    b = 'hello'

    def f(self):
        return 42
    
def make_A():
    name = 'A'
    bases = ()

    a = 1
    b = 'hello'
    
    def f(self):
        return 42
    
    namespace = {'a':a, 'b':b,'f':f}

    A = type(name, bases, namespace)

    return A

#both the abhove code do the same things.


def make_A_more_accurate():
    name = 'A'
    bases = ()
    namespace = type.__prepare__(name, bases)
    body = (
        '''
        code
        '''
    )

    exec(body, globals(), namespace)
    A = type(name, bases, namespace)
    return A

A = make_A_more_accurate()  
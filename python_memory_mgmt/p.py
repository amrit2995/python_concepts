# class MyMetaclass(type):
#     pass

# class A(metaclass=MyMetaclass):
#     pass

# def main():
#     a = A()
#     print(f'{type(a)=}')
#     print(f'{type(A)=}')


import time
class LoadTimeMeta(type):
    base_time = time.perf_counter()

    def __new__(mcs,name, bases, namespace):
        print(mcs, name, bases, namespace)
        namespace['__class_load_time__'] = time.perf_counter() - LoadTimeMeta.base_time
        return super().__new__(mcs, name, bases, namespace)
    
class A(metaclass=LoadTimeMeta):
    pass

class B(A):
    pass


if __name__ == '__main__':
    a = A()
    print(A.__class_load_time__)
    print(B.__class_load_time__)
      


Using Metaclass , if I added some additional functionality , it will get added to the whole hierarchy of the classes.
This donot happen when if I use just a decorator . Then will have to add the same functionality for all the child classes as well.

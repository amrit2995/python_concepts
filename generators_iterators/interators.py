class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current =self.value
        self.value += 1
        return current
    
    def __str__(self):
        return str(self.value)

    
nums = MyRange(1,10)

while True:
    try:
        print(nums)
        next(nums)
    except StopIteration as e:
        print(e)
        break


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self]



my_iterator = MyIterator([1,2,3,4,5])
for item in my_iterator:
    print(item)


In this example:

# MyIterator is a custom iterator class that implements the iterator protocol with __iter__() and __next__() methods.
# The __iter__() method returns the iterator object itself.
# The __next__() method returns the next item in the sequence and updates the index. If there are no more items, it raises a StopIteration exception.
# We create an instance of MyIterator with a list [1, 2, 3, 4, 5] and iterate over it using a for loop. The loop automatically calls __iter__() to obtain an iterator and then calls __next__() repeatedly to fetch each item.
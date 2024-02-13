def my_range(start):
    current = start

    while True:
        yield current
        current += 1

nums = my_range(1,10)


for num in nums:
    print(num)


# Generators
# ++ Instead of returning a result, they yield a value.
# ++ After yielding a value, it keeps that state until the generator run again and yields the next value.
# ++ Generators are iterators as well but the dunder iter and the dunder next methods are created automatically .
# ++ So we don't have to create them like we did in a class.


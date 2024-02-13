def operation1():
    for i in range(3):
        yield f"Operation 1: {i}"

def operation2(input_data):
    for item in input_data:
        yield f"Operation 2: {item}"

def operation3(input_data):
    for item in input_data:
        yield f"Operation 3: {item}"

def operation4(input_data):
    for item in input_data:
        yield f"Operation 4: {item}"

def chain_generators(generators):
    input_data = None
    for generator in generators:
        if input_data is None:
            input_data = generator()
        else:
            input_data = generator(input_data)
        yield from input_data

# Chain the generators together
generators = [operation1, operation2, operation3, operation4]
output_generator = chain_generators(generators)

# Lazily consume the output of each operation
for result in output_generator:
    print(result)

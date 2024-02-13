# def operation1(input_data):
#     # Placeholder for operation1
#     return f"Operation 1 processed: {input_data}"

# def operation2(input_data):
#     # Placeholder for operation2
#     return f"Operation 2 processed: {input_data}"

# def process_inputs(inputs):
#     for input_data in inputs:
#         # Perform operation1 on input
#         output1 = operation1(input_data)
#         yield output1

#         # Perform operation2 on output1
#         output2 = operation2(output1)
#         yield output2

# # List of inputs
# inputs = [1, 2, 3, 4, 5]

# # Iterate over the generator to consume the results
# for result in process_inputs(inputs):
#     print(result)


# def process1(inputs):
#     for input_data in inputs:
#         result = f"Process 1 processed: {input_data}"
#     # yield result
#     return result

# def process2(inputs):
#     for input_data in inputs:
#         result = f"Process 2 processed: {input_data}"
#     yield result

# def process3(inputs):
#     for input_data in inputs:
#         result = f"Process 3 processed: {input_data}"
#     yield result

# def process4(inputs):
#     for input_data in inputs:
#         result = f"Process 4 processed: {input_data}"
#     yield result


def process1(input):
    return f" process 1 {input}"

def process2(input):
    return f" process 2 {input}"

def process3(input):
    return f"process 3 {input}"


input = [1,2,3,4]

def iterate_processses(processes, inputs):
    # for _ in range
    pass

class ProcessIterator:
    def __init__(self,processes, inputs):
        self.processes = processes
        self.inputs = inputs
        self.process_index = 0
        self.input_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.input_index >= len(self.inputs):
            raise StopIteration
        
        process = self.processes[self.process_index]
        input_data = self.inputs[self.input_index]
        result = process(input_data)

        self.process_index = (self.process_index + 1) % len(self.processes)
        if self.process_index == 0:
            self.input_index += 1

        return result


inputs = [1,2,3,4,5]
process_generators = [process1, process2, process3]

process_iterator = ProcessIterator(process_generators, inputs)
for result in process_iterator:
    print(result)
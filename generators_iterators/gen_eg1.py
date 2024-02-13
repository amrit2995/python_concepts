import time



#with yield 
def operation1(inputs):
    i = 0
    while i<len(inputs):
        time.sleep(1)
        yield f"Operation1 input {inputs[i]} processed"
        i += 1

def operation2(inp):
    time.sleep(1)
    print(f"Operation2 performed {inp}")
    # i = 0
    # while i<len(inputs):
    #     yield f"Operation2 input {inputs[i]} processed"

inputs = [1,2,3,4,5]
for output1 in operation1(inputs):
    operation2(output1)


#without yield 
# def operation1(inputs):
#     result = []
#     for i in range(len(inputs)):
#         time.sleep(1)
#         out = f"Operation1 input {inputs[i]} processed"
#         result.append(out)
#     return result

# def operation2(inp):
#     time.sleep(1)
#     print(f"Operation2 performed {inp}")
#     # i = 0
#     # while i<len(inputs):
#     #     yield f"Operation2 input {inputs[i]} processed"


# inputs = [1,2,3,4,5]
# for output1 in operation1(inputs):
#     operation2(output1)


def operation1(inputs):
    i = 0
    while i<len(inputs):
        time.sleep(1)
        yield f"Operation1 input {inputs[i]} processed"
        i += 1

def operation2(inputs):
    i = 0
    while i<len(inputs):
        time.sleep(1)
        yield f"Operation2 input {inputs[i]} processed"
        i += 1

def operation3(inputs):
    i = 0
    while i<len(inputs):
        time.sleep(1)
        yield f"Operation3 input {inputs[i]} processed"
        i += 1

def operation4(inputs):
    i = 0
    while i<len(inputs):
        time.sleep(1)
        yield f"Operation4 input {inputs[i]} processed"
        i += 1

for i in operation1(inputs):
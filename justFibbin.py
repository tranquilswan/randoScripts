listOfNums = [1,2,3,4,5,8181]

def fiber(inputNum):
    print("Enter Fiber")
    if (inputNum == 0):
        return 0
    elif (inputNum == 1):
        return 1
    else:
        return fiber(inputNum - 1) + fiber(inputNum - 2)

print("fib is: ", fiber(8181))

# for num in listOfNums:
#     print("the Fibonacci # at index ", num, " is: ", fiber(num))


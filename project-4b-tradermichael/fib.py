# Author: Michael Le
# Date: 10/21/2019
# Description: Function that returns value based on number position index 1 for fibonacci sequence

def fib(fib_seq):
    """
    fib_seq is an integer, and determines what the integer fibonacci value is
    at that position within the fibonacci sequence starting index at 1
    fibonacci sequence takes previous two values and adds them together for current value
    """
    fib_prev = 0
    fib_current = 0
    for i in range(1,fib_seq+1):
        if (i == 1 or i == 2):
            fib_prev = 1
            fib_current = 1
            fib_current_final = 1
        else:
            fib_current_final = fib_prev + fib_current
            fib_prev = fib_current
            fib_current = fib_current_final
    return fib_current_final
    print(int(fib_current_final))


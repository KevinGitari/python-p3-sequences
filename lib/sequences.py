#!/usr/bin/env python3

#def print_fibonacci(length):
  #  pass
def print_fibonacci(length):
    if length == 0:
        print([])
        return

    num = [0]
    if length > 1:
        num.append(1)
        for i in range(2, length):
            num.append(num[i-1] + num[i-2])
    
    print(num)


print_fibonacci(1)  
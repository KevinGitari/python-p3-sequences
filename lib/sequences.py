#!/usr/bin/env python3

#def print_fibonacci(length):
  #  pass
def print_fibonacci(length):
	print_fibonacci = []
	if length > 0:
		print_fibonacci.append(0)
	if length >= 2:
		print_fibonacci.append(1)
		for i in range(2, length):
			print_fibonacci.append(print_fibonacci[-1] + print_fibonacci[-2])

	print(print_fibonacci)
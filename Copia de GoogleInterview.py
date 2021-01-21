# Google Interview - 14 de julio de 2020

# Having 4 numbers from 1 to 10 each one, make an algorithm if we can
# reach the number 24 with ops (+ and *)

import random

def searchSolution(l, number):
    if l == [] and number > 1:
        return False
    if not l == [] and number <= 0:
        return False
    if l == [] and (number == 0 or number == 1):
        return True
    return searchSolution(l[1:], number - l[0]) or searchSolution(l[1:], number // l[0])


l = [random.randint(1,10) for _ in range(4)]
#print(l)
#print(searchSolution(l, 24))

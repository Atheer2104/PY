import copy
import evaluator

def add(a, b):
    # simple additation
    return a + b

def times(a, b):
    # simple multiplcation
    return a * b

def cons(x, xs):
    # Python's `insert` mutates the list, but `cons` should not
    # we copy list without change anything
    ys = copy.deepcopy(xs)
    # in the zero index we add x
    ys.insert(0, x)
    return ys

# it's like our input
arithmetic = [add, 1, [times, 2, 3]]
lists = [cons, 1, [evaluator.quote, [2, 3]]]

# we evaluate the input
print(evaluator.eval(arithmetic)) # => 7
print(evaluator.eval(lists))      # => [1,2,3]




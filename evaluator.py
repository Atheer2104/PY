def quote(x):
    return x

def eval(code):
    # code can only be evaluated if it's a list
    if type(code) is list:

        # The first item in a list/input is a function
        # that determines what we sould like to do the rest are arguments
        fn = code[0]

        # we don't evaluate quoted expressios it's an func like add
        if fn is quote:
            return code[1]


        # we need to evaluted our aruments/values
        args = []
        # we loop through the list from the first and forward
        for expr in code[1:]:
            args.append(eval(expr))
            #print("expr " + str(expr) + " eval "+ str(eval(expr)))

        # fn gets all of the values that was contained in args
        return fn(*args)

    # If it's not an expression, just return that thing.
    else:
        return code






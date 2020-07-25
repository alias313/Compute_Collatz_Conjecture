"""
This algorithm takes a number n. If n is even, n is multiplied by 0.5. If n is odd, it's multiplied by 3 and it adds one 
to the result.
"""

def show_collatz(n):
    """This functions the steps n takes to get to 1 an what the steps are"""
    res = int(n) # The result of the computations
    print("Step 0: " + str(int(res)))
    for i in range(1, 10000):
        if res % 2 == 0:
            res /= 2
            print("Step " + str(i) + ": " + str(int(res)))
        elif res == 1:
            print("n = " + str(n))
            n_steps = i-1
            return True # It means the Collatz Conjecture holds true in this case
            return n_steps
            break
        else:
            res = (3*res+1)
            print("Step " + str(i) + ": " + str(int(res)))

def collatz_true(n):
    """This function takes in a number and shows all the numbers beetween 
    1 and n and shows how many steps each number takes to get to 1
    """
    global c1
    c1 = False
    for e in range(n):
        res = e+1
        for i in range(100000):
            if res % 2 == 0:
                res /= 2
            elif res == 1:
                c1 = True
                n_steps = i
                break
            else:
                res = (3*res+1)
        if c1 == True:
            print(str(e+1) + ": " + str(n_steps) + " steps.") 

def collatz_true_alt(n, a):
    """This function does the same as collatz_true but this time from n to n+a"""
    global c1
    c1 = False
    for e in range(n, n+a):
        res = e+1
        for i in range(100000):
            if res % 2 == 0:
                res /= 2
            elif res == 1:
                c1 = True
                n_steps = i
                break
            else:
                res = (3*res+1)
        if c1 == True:
            print(str(e+1) + ": " + str(n_steps) + " steps.")

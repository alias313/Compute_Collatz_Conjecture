"""
This algorithm takes a number n. If n is even, n is multiplied by 0.5. If n is odd, it's multiplied by 3 and it adds one 
to the result.
"""

def show_collatz(n):
    """This functions shows the steps n takes to get to 1 and what the steps are"""
    i = 0
    print("Step 0: " + str(computed_number := n))
    while n != 1:
        i += 1
        if n % 2 == 0:
            n /= 2
            print("Step " + str(i) + ": " + str(int(n)))
        else:
            n = 3*n + 1
            print("Step " + str(i) + ": " + str(int(n)))
    
    print(f"""
        {"-"*(30)}
        # Number computed : {computed_number}
        # Number of steps : {i}
        # Collatz holds :   True
        {"-"*(30)}
        """)

def collatz_range(n):
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
    """This function does the same as collatz_range but this time from n to n+a"""
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

show_collatz_input = int(input("Please enter a nonnegative integer:"))
show_collatz(show_collatz_input)
collatz_range_input = int(input("Please enter another nonnegative integer:"))
collatz_range(collatz_range_input)
collatz_true_alt_input = int(input("Please enter another nonnegative integer:"))
collatz_true_alt(collatz_true_input, collatz_true_alt_input)

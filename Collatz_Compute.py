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

def collatz_range_n(n):
    """This function takes in a number and shows all the numbers from 1 to n 
    and shows how many steps each number takes to get to 1"""
    for i in range(1, n+1):
        j = 0
        c = i
        while c != 1:
            j += 1
            c = {
                0: int(c/2),
                1: int(3*c + 1)
            }.get(int(c%2))
        print(f"{i}: {j} steps")


def collatz_range(n, a):
    """This function does the same as collatz_range but this time from n to n+a"""
    for i in range(n, n+a):
        j = 0
        c = i
        while c != 1:
            j += 1
            c = {
                0: int(c/2),
                1: int(3*c + 1)
            }.get(int(c%2))
        print(f"{i}: {j} steps")


show_collatz(int(input("Please enter a nonnegative integer:")))
collatz_range_n(int(input("Please enter another nonnegative integer:")))
collatz_range(int(input("Please enter another nonnegative integer:")), int(input("Please enter another nonnegative integer:")))

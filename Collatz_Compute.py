"""
This algorithm takes a number n. If n is even, n is multiplied by 0.5. If n is odd, it's multiplied by 3 and it adds one 
to the result.
"""
import sys

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


def collatz_specific_range(n, a):
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

if __name__ == "__main__":
    try:
        arg1 = sys.argv[1:]
        arg2 = sys.argv[2]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <function name> <argument/s>")
    
    try:
        arg2 = int(arg2)
        if len(sys.argv) == 4:
            arg3 = int(sys.argv[3])
            if arg3 < 0:
                raise SystemExit("Please enter a positive integer as an argument")
    except ValueError:
        raise SystemExit("Please enter an integer as the second and/or third command-line argument")
    
    if arg2 < 0:
        raise SystemExit("Please enter a positive integer as an argument")

    if arg1 == "show_collatz":
        if len(sys.argv) == 3:
            show_collatz(arg2)
        else:
            raise SystemExit("show_collatz accepts one integer argument")
    elif arg1 == "collatz_range":
        if len(sys.argv) == 3:
            collatz_range(arg2)
        else:
            raise SystemExit("collatz_range accepts one integer argument")
    elif arg1 == "collatz_specific_range":
        if len(sys.argv) == 4 and arg2 < arg3:
            collatz_specific_range(arg2, arg3)
        else:
            raise SystemExit("collatz_specific_range accepts two integer arguments, the first smaller than the second")
    else:
        raise SystemExit("Please enter a valid function name")



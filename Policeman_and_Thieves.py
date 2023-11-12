"""GROUP NUMBER 2 DATA STRUTURE AND ALGORITHMS LEARNING TASK"""

"""POLICEMAN AND THIEVES PROBLEM"""

"""You are given a grid of size N x N that has the following specifications:

    Each cell in the grid contains either a policeman or a thief.
    A policeman can only catch a thief if both are in the same row.
    Each policeman can only catch one thief.
    A policeman cannot catch a thief who is more than K units away from the policeman.
    Write a program to find the maximum number of thieves that can be caught in the grid."""

"""Input format
    
        First line: T (number of test cases)
        For each test case:
        First line: Two space-separated integers N and K
        Next N lines: N space-separated characters (denoting each cell in the grid)"""
from os import system as sys
def police_and_thieves(grid, k):
    """Function to fine the maximum number of thieves that can be caught in the grid each police can catch only one thief"""
    caught = 0

    # Traverse the grid by each row
    for row in grid:

        # Traverse each coloumn in the row
        for coloumn in range(len(row)):

            # If the coloumn has a police
            if row[coloumn] == 'P':

                # Traverse the coloumn from the left to right of the police till the range of k
                for item in range(coloumn-k, coloumn+k+1):

                    # If the item is in the range of the coloumn then continue to find the thief
                    if item >= 0 and item < len(row):

                        # If theres a thief in the range of police then catch the thief
                        if row[item] == 'T':
                            
                            # Add 1 to the caught thief
                            caught += 1

                            # the cahnge the thief to caught and break the loop to find another thief
                            row[item] = 'C'
                            break
    
    # Return the total number of thieves caught after searchin all rows
    return f"\nThe total thieves caught are: {caught}"


# Main function
def main():

    # create a loop to get input from the user and break the loop if the input is an integer
    while 1:
        try:
            test_cases = int(input("\nEnter the number of test cases: "))
            break
        except ValueError:
            print("\nEnter an Integer only!!")

    # Loop through the test cases
    for _ in range(test_cases):
        print(f"\nTEST CASE {_+1}")
        # Get the input from the user N for the row and coloumn (N x N) and K for the range of the police
        n, k = map(int, input("\nEnter the N and K of the Row: ").split())

        # Create a grid to store the input from the user //THis is a 2D array
        grid = []

        # Loop the N input
        for _ in range(n):

            # Append the input to the grid // The input is a list of string using split() func. to nake a list
            grid.append(list(input(f"\nEnter the Row {_+1} : ").upper().split(' '))[0:n])

        # use the police_and_thieves func. and pring the total thieves caught
        print(police_and_thieves(grid, k))

# Call the main function
if __name__ == "__main__":
    main()
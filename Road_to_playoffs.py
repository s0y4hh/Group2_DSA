"""GROUP NUMBER 2"""
"""
In a football championship, N teams are competing against each other on the league stage.
The current number of points of each team are X1, X2, X3....XN. M days of league stage are
remaining and on each day K teams win and each of the winning team's points is incremented by 1.
 Top B teams will qualify for the playoffs in the championship. Officials of the tournament
 want to how many teams have a non-zero probability of making it to the playoffs.
"""
# make a function "Road_to_Playoffs"
def Road_to_Playoffs(N, M, K, B, currentPoints):
        """
        N = number of teams
        M = number of days and points remaining
        K = number of teams that will win
        B = number of teams that make it to playoffs
        """
        # Delare a variable 'lo' for the lower bound and 'hi' for the upper bound

        lo = B - 1 # we start our search from the B-1th team and try to find the minimum number of teams required to qualify for the playoffs.
        hi = N - 1 #  We declare a value of N because all team has a chance to qualify to the playoffs

        # We use binary search to find the minimum number of teams required to qualify for the playoffs.
        while lo < hi:

            # to find the mimd value we use the formula: mid = hi - (hi - lo) // 2
            mid = hi - (hi - lo) // 2

            # if the current points of the B-1th team is greater than the current points of the mid team + M
            if currentPoints[B - 1] > currentPoints[mid] + M:
                 
                # then we set the upper bound to mid - 1
                 hi = mid - 1
            else:
                # otherwise we set the lower bound to mid

                # declare a variable 'temp' to store the value of the current points of the mid team
                temp = 0

                # we use a for loop to iterate from the B-1th team to the mid team
                for i in range(B - 1, mid):

                    # then update the value of the temp variable 
                    temp += currentPoints[mid] + M - currentPoints[i]

                # if the value of temp is less than M * (K - (B - 1) - (N - mid))
                if temp < M * (K - (B - 1) - (N - mid)):

                    # then we set the upper bound to mid - 1
                    hi = mid - 1

                else:
                    # otherwise we set the lower bound to mid
                    lo = mid
        # return and print the value of lo + 1 
        print(f"The number of teams that can make it to playoffs are: {lo + 1}")

def main():
    # create a loop to get input from the user and break the loop if the input is an integer
    while 1:
        try:
            test_cases = int(input("\nEnter the number of test cases: "))
            break
        except ValueError:
            print("\nEnter an Integer only!!")

    # Loop to the user input and test every case
    for _ in range(test_cases):
        print(f"\nTEST {_+1}")

        # get the input from the user and store it in the variables N, M, K, B and currentPoints
        # use the split() method to split the input into a list of strings
        N, M, K, B = map(int, input("\nEnter N, M, K, B: ").split())

        # use the map() method to convert the input separated by space into integers
        currentPoints = list(map(int, input("Enter the current points of each team: ").split()))
        # then reverse the list
        currentPoints.sort(reverse=True)

        # call the function to get the result
        Road_to_Playoffs(N, M, K, B, currentPoints)
if __name__ == "__main__":
    main()
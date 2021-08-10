if __name__ == "__main__":
    test_integer = int(input())

    # constraint 1<= n <= 100
    if (1<= test_integer <= 100):
        if (test_integer % 2 != 0):
            print("Weird")
        elif (test_integer % 2 == 0 and test_integer in range(2, 6)):
            print("Not Weird")
        elif (test_integer % 2 == 0 and test_integer in range(6, 21)):
            print("Weird")
        elif (test_integer %2 == 0 and test_integer > 20):
            print("Not Weird")
    else:
        print("Input not within range")
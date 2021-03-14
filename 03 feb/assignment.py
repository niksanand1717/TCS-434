while True:

    choice = input(
"""
Press 1 to reverse a number\n
Press 2 to find numbers which are divisible by 3 and/or 5 between range given by user\n
Press 3 to print all armstrong numbers between 1 and 10000\n
Press 'q' to exit\n
Choice :- """)

    if choice == '1': import solution_1

    elif choice == '2': import solution_2

    elif choice == '3': import solution_3

    elif choice == 'q': break

    else: print("Enter a valid choice")
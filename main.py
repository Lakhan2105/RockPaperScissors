from getpass import getpass as input

print("E P I C   🪨  📄 ✂️   B A T T L E\n")
print("""Rock     => R or r
Paper    => P or p
Scissors => S or s\n""")

round = 1
n = 0
m = 0

while (round <= 3):
    print("\n\nRound = ", round, "\n")
    p1 = input("Enter your choice Player 1 >")
    print()
    p2 = input("Enter your choice Player 2 >")
    print()
    if (p1 == 'R' or p1 == 'r'):
        if (p2 == 'P' or p2 == 'p'):
            n = n + 1
            print("Paper covers Rock! Player 2 win!")
        elif (p2 == 'S' or p2 == 's'):
            m = m + 1
            print("Rock smashes scissors! Player 1 win!")
        else:
            print("Game is Draw\n")
            print("Player 1 and Player 2 have same value :", p1)

    elif (p1 == 'P' or p1 == 'p'):
        if (p2 == 'S' or p2 == 's'):
            n = n + 1
            print("Scissors cuts Paper! Player 2 win!")
        elif (p2 == 'R' or p2 == 'r'):
            m = m + 1
            print("Paper covers Rock! Player 1 win!")
        else:
            print("Game is Draw\n")
            print("Player 1 and Player 2 have same value :", p1)

    elif (p1 == 'S' or p1 == 's'):
        if (p2 == 'R' or p2 == 'r'):
            n = n + 1
            print("Rock smashes scissors! Player 2 win!")
        elif (p2 == 'P' or p2 == 'p'):
            m = m + 1
            print("Scissors cuts Paper! Player 1 win!")
        else:
            print("Game is Draw")
            print("Player 1 and Player 2 have same value :", p1)

    round = round + 1

print("\n\nThe final result is :")
if (n > m):
    print("Player 2 wins", n, "times")
elif (n == m):
    print("Game is draw finally")
else:
    print("Player 1 wins ", m, "times")
import time
import random
# asks for the sign from user
print("Which sign do you want to have ? x or o")
ask_sign = input()

# introduction
print("""|------|------|------|
|  1   |  2   |  3   |
|------|------|------|
|  4   |  5   |  6   |
|------|------|------|
|  7   |  8   |  9   |
|------|------|------|

Please enter your move like this: 1, 2, 3, 4, 5, 6, 7, 8, 9""")


def tic_tac():  # final display on which the result appears

    return """|------|------|------|
|  {}   |  {}   |  {}   |
|------|------|------|
|  {}   |  {}   |  {}   |
|------|------|------|
|  {}   |  {}   |  {}   |
|------|------|------|""".format(num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9)


# saves the sign in variables
if ask_sign == "x":
    user_sign = "x"
    user_sign_1 = user_sign
    computer_sign = "o"
    computer_sign_1 = computer_sign
elif ask_sign == "o":
    user_sign = "o"
    user_sign_1 = user_sign
    computer_sign = "x"
    computer_sign_1 = computer_sign

total = [10]

num_1 = " "
num_2 = " "
num_3 = " "
num_4 = " "
num_5 = " "
num_6 = " "
num_7 = " "
num_8 = " "
num_9 = " "

found = False
while not False:
    print("Please enter your valid move: ")
    user_input = int(input())
    if user_input in total:
        print("Kindly enter a move which is not used.")
        continue
    # it is the logic for the implementation and registering of input the user gave.
    if user_input not in total:
        total.append(user_input)

        if user_input == 1:
            num_1 = user_sign_1
        elif user_input == 2:
            num_2 = user_sign_1
        elif user_input == 3:
            num_3 = user_sign_1
        elif user_input == 4:
            num_4 = user_sign_1
        elif user_input == 5:
            num_5 = user_sign_1
        elif user_input == 6:
            num_6 = user_sign_1
        elif user_input == 7:
            num_7 = user_sign_1
        elif user_input == 8:
            num_8 = user_sign_1
        elif user_input == 9:
            num_9 = user_sign_1

    # checks for the tie.
    if len(total) == 11:
        print("THE GAME HAS BEEN TIED.")
        print(tic_tac())
        break
    if num_1 == num_2 == num_3 == user_sign_1 or num_4 == num_5 == num_6 == user_sign_1 or num_7 == num_8 == num_9 == user_sign_1 or num_1 == num_4 == num_7 == user_sign_1 or \
                                    num_2 == num_5 == num_8 == user_sign_1 or num_3 == num_6 == num_9 == user_sign_1 or num_1 == num_5 == num_9 == user_sign_1 or num_3 == num_5 == num_7 == user_sign_1:
        print("The user wins. \n ----- CONGRATULATIONS -----")
        print(tic_tac())
        break

    if num_1 == num_2 == num_3 == computer_sign_1 or num_4 == num_5 == num_6 == computer_sign_1 or num_7 == num_8 == num_9 == computer_sign_1 or num_1 == num_4 == num_7 == computer_sign_1 or \
                                    num_2 == num_5 == num_8 == computer_sign_1 or num_3 == num_6 == num_9 == computer_sign_1 or num_1 == num_5 == num_9 == computer_sign_1 or num_3 == num_5 == num_7 == computer_sign_1:
        print("The computer wins. \n Better luck next time. ")
        print(tic_tac())
        break

    # it is the logic for the implementation and registering of random move the computer gave.
    if 1 < len(total) < 11:
        while True:
            ran_no = random.randint(1, 9)
            if ran_no in total:
                continue
            elif ran_no not in total:
                break

        if ran_no not in total:
            total.append(ran_no)
            if ran_no == 1:
                num_1 = computer_sign_1

            elif ran_no == 2:
                num_2 = computer_sign_1

            elif ran_no == 3:
                num_3 = computer_sign_1

            elif ran_no == 4:
                num_4 = computer_sign_1

            elif ran_no == 5:
                num_5 = computer_sign_1

            elif ran_no == 6:
                num_6 = computer_sign_1

            elif ran_no == 7:
                num_7 = computer_sign_1

            elif ran_no == 8:
                num_8 = computer_sign_1

            elif ran_no == 9:
                num_9 = computer_sign_1

            if num_1 == num_2 == num_3 == user_sign_1 or num_4 == num_5 == num_6 == user_sign_1 or num_7 == num_8 == num_9 == user_sign_1 or num_1 == num_4 == num_7 == user_sign_1 or \
                    num_2 == num_5 == num_8 == user_sign_1 or num_3 == num_6 == num_9 == user_sign_1 or num_1 == num_5 == num_9 == user_sign_1 or num_3 == num_5 == num_7 == user_sign_1:
                print("The user wins. \n ----- CONGRATULATIONS -----")
                print(tic_tac())
                break

            if num_1 == num_2 == num_3 == computer_sign_1 or num_4 == num_5 == num_6 == computer_sign_1 or num_7 == num_8 == num_9 == computer_sign_1 or num_1 == num_4 == num_7 == computer_sign_1 or \
                    num_2 == num_5 == num_8 == computer_sign_1 or num_3 == num_6 == num_9 == computer_sign_1 or num_1 == num_5 == num_9 == computer_sign_1 or num_3 == num_5 == num_7 == computer_sign_1:
                print("The computer wins. \n Better luck next time. ")
                print(tic_tac())
                break

        elif ran_no in total:
            if ran_no == 1:
                num_3 = computer_sign_1
                total.append(3)
            elif ran_no == 9:
                num_7 = computer_sign_1
                total.append(7)
            else:
                num_5 = computer_sign_1
                total.append(5)

            if num_1 == num_2 == num_3 == user_sign_1 or num_4 == num_5 == num_6 == user_sign_1 or num_7 == num_8 == num_9 == user_sign_1 or num_1 == num_4 == num_7 == user_sign_1 or \
                    num_2 == num_5 == num_8 == user_sign_1 or num_3 == num_6 == num_9 == user_sign_1 or num_1 == num_5 == num_9 == user_sign_1 or num_3 == num_5 == num_7 == user_sign_1:
                print("The user wins. \n ----- CONGRATULATIONS -----")
                print(tic_tac())
                break

            if num_1 == num_2 == num_3 == computer_sign_1 or num_4 == num_5 == num_6 == computer_sign_1 or num_7 == num_8 == num_9 == computer_sign_1 or num_1 == num_4 == num_7 == computer_sign_1 or \
                    num_2 == num_5 == num_8 == computer_sign_1 or num_3 == num_6 == num_9 == computer_sign_1 or num_1 == num_5 == num_9 == computer_sign_1 or num_3 == num_5 == num_7 == computer_sign_1:
                print("The computer wins. \n Better luck next time. ")
                print(tic_tac())
                break
    print(tic_tac())

time.sleep(4)

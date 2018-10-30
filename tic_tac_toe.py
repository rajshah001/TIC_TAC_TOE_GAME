import time
import random
from tkinter import *

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
    computer_sign = "o"
elif ask_sign == "o":
    user_sign = "o"
    computer_sign = "x"

total = []

num_1 = " "
num_2 = " "
num_3 = " "
num_4 = " "
num_5 = " "
num_6 = " "
num_7 = " "
num_8 = " "
num_9 = " "

while True:
    
    print("Please enter your valid move: ")
    user_input = int(input())

    if user_input in total or user_input > 9:
        print("Kindly enter a move which is not used.")
        continue
    # it is the logic for the implementation and registering of input the user gave.
    if user_input not in total:
        total.append(user_input)

        if user_input == 1:
            num_1 = user_sign
        elif user_input == 2:
            num_2 = user_sign
        elif user_input == 3:
            num_3 = user_sign
        elif user_input == 4:
            num_4 = user_sign
        elif user_input == 5:
            num_5 = user_sign
        elif user_input == 6:
            num_6 = user_sign
        elif user_input == 7:
            num_7 = user_sign
        elif user_input == 8:
            num_8 = user_sign
        elif user_input == 9:
            num_9 = user_sign

    if num_1 == num_2 == num_3 == user_sign or num_4 == num_5 == num_6 == user_sign or num_7 == num_8 == num_9 == user_sign or num_1 == num_4 == num_7 == user_sign or \
                                    num_2 == num_5 == num_8 == user_sign or num_3 == num_6 == num_9 == user_sign or num_1 == num_5 == num_9 == user_sign or num_3 == num_5 == num_7 == user_sign:
        print("The user wins. \n ----- CONGRATULATIONS -----")
        windw = Tk()
        messagebox.showinfo("----- CONGRATULATIONS -----", "you are the winner.")
        windw.mainloop()
        print(tic_tac())
        break

    if num_1 == num_2 == num_3 == computer_sign or num_4 == num_5 == num_6 == computer_sign or num_7 == num_8 == num_9 == computer_sign or num_1 == num_4 == num_7 == computer_sign or \
                                    num_2 == num_5 == num_8 == computer_sign or num_3 == num_6 == num_9 == computer_sign or num_1 == num_5 == num_9 == computer_sign or num_3 == num_5 == num_7 == computer_sign:
        print("The computer wins. \n Better luck next time. ")            
        windw = Tk()
        messagebox.showinfo("Better luck next time. ", "The computer wins.")
        windw.mainloop()
        print(tic_tac())
        break

    # checks for the tie.
    if len(total) == 9:
        #print("THE GAME HAS BEEN TIED.")
        windw = Tk()
        messagebox.showinfo("TIED!", "THE GAME HAS BEEN TIED.")
        windw.mainloop()
        print(tic_tac())
        break

    # it is the logic for the implementation and registering of random move the computer gave.

    while True:
        ran_no = random.randint(1, 9)
        if ran_no in total:
            continue
        elif ran_no not in total:
            break

    if ran_no not in total:
        total.append(ran_no)
        if ran_no == 1:
            num_1 = computer_sign

        elif ran_no == 2:
            num_2 = computer_sign

        elif ran_no == 3:
            num_3 = computer_sign

        elif ran_no == 4:
            num_4 = computer_sign

        elif ran_no == 5:
            num_5 = computer_sign

        elif ran_no == 6:
            num_6 = computer_sign

        elif ran_no == 7:
            num_7 = computer_sign

        elif ran_no == 8:
            num_8 = computer_sign

        elif ran_no == 9:
            num_9 = computer_sign


        if num_1 == num_2 == num_3 == user_sign or num_4 == num_5 == num_6 == user_sign or num_7 == num_8 == num_9 == user_sign or num_1 == num_4 == num_7 == user_sign or \
                    num_2 == num_5 == num_8 == user_sign or num_3 == num_6 == num_9 == user_sign or num_1 == num_5 == num_9 == user_sign or num_3 == num_5 == num_7 == user_sign:
            print("The user wins. \n ----- CONGRATULATIONS -----")
            windw = Tk()
            messagebox.showinfo("----- CONGRATULATIONS -----", "you are the winner.")
            windw.mainloop()
            print(tic_tac())
            break

        if num_1 == num_2 == num_3 == computer_sign or num_4 == num_5 == num_6 == computer_sign or num_7 == num_8 == num_9 == computer_sign or num_1 == num_4 == num_7 == computer_sign or \
                    num_2 == num_5 == num_8 == computer_sign or num_3 == num_6 == num_9 == computer_sign or num_1 == num_5 == num_9 == computer_sign or num_3 == num_5 == num_7 == computer_sign:
            print("The computer wins. \n Better luck next time. ")
            windw = Tk()
            messagebox.showinfo("Better luck next time. ", "The computer wins.")
            windw.mainloop()
            print(tic_tac())
            break

    else:
        pass
    
    print(tic_tac())

time.sleep(4)


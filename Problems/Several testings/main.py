def check(x):
    if x.isdigit():
        if int(x) >= 202:
            print(x)
        else:
            print('There are less than 202 apples! You cheated on me!')
    else:
        print("It is not a digit!")

# user_input = input("Enter a number: ")
# check(user_input)

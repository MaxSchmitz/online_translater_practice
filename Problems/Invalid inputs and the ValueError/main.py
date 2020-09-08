def check():
    user_input = input()
    if user_input.isdigit():
        if 25 <= int(user_input) <= 37:
            print(user_input)
        else:
            print("Correct the error!")
    else:
        print("Correct the error!")
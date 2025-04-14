import random
computer_output = random.randint(1,100)
count = 0
while True:
    user_input = int(input("enter your input btw 1 to 100"))
    count += 1
    if user_input < computer_output :
        print("enter higher number")
    elif user_input >computer_output:
        print(" enter lower number")
    elif user_input == computer_output:
        print(f"congratulations ! you have done it in {count} times. ")
        break
    else:
        print("Invalid output")
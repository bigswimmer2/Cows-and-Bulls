import random

s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-/.,;'[]{}:<>?"
i = 0
fin = ""
while i == 0:
    num = int(input("What length do you want? "))

    password = "".join(random.sample(s, num))

    print(password)
    j = 0
    while(j ==0):
        want = input("Do you this password? ")
        want.lower()
        if want == "yes":
            print("Your Password is " + password)
            break
        elif want == "no":
            break
    if want == "yes":
        fin = input("Do you want a new password or no? ")
        fin.lower()
        while j == 0:
            if fin == "yes":
                break
            elif fin == "no":
                break
    if fin == "no":
        print("This is your final password " + password)
        break
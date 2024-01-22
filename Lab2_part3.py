#lab2_part3

print("Did your PC connected successfully to router?")
a = input()
if a == 'Yes' or a == 'yes':
    print("You are good to go!")
else:
    print("Reboot the router and try to connect")
    print("Did it work?")
    a = input()
    if a == 'Yes' or a == 'yes':
        print("You are good to go!")
    else:
        print("Make sure the cables between the router & modem are plugged in firmly")
        print("Did it work?")
        a = input()
        if a == 'Yes' or a == 'yes':
            print("You are good to go!")
        else:
            print("Move the router to a new location and try to connect.")
            print("Did it work?")
            a = input()
            if a == 'Yes' or a == 'yes':
                print("You are good to go!")
            else:
                print("Get a new router.")
    

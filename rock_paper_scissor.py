import random

option =["rocker","paper","scissor"]

random_num= random.randint(0,2)
choice_computer = option[random_num]
x=input("hi am computer !\nyou are ready to play with me :")
count=0
if x== "yes":
    for i in range(5):
        user_option =int(input("1.rocker\n2.paper\n3.scissor \n(your option)-->"))
        list_option=option[user_option]
        if choice_computer == list_option:
            print("you lost")
        else: 
            print("you win")
            count+=1

else: 
    print("please enter yes or no")
    
print(f'your win times {count}')
print("thank you")
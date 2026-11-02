import random

number=random.randint(1,100)

def menu():
    count=0
    for num in range(5):
        print("=======: guessing number :=======")
        count1=4-count
    

        num=int(input("enter any number 1 to 100 :  "))
        count+=1
        if count==5:
            print("attempts is over...")
            break

        if number>num:
            print("greater then number")
            print(f"remaining attempt : {count1}")

        elif number<num:
            print("smaller then number")
            print(f"remaining attempt : {count1}")

        elif number == num:
            print("congratulations...")
            print(f"number attempt : {count}")
                
            break
        else:
            break
menu()
while True:
    print("if you want to play again so enter yes \n","if not so enter no")
    choice=input("enter choice : ")

    if choice=="yes":
        menu()
    elif choice=="no":
        print("thank you")
        break

    else:
        print("invalid")
        
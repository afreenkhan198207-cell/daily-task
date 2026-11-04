
    

import json

with open("data.json","r+") as file:
    data=json.load(file)

def add():
    print("===========: add number :===========")
    contact={}
    while True:
        name=input("enter name : ")
        if len(name)>2:
            break
        else:
            print("invalid name")
    while True:
        number=input("enter number : ")
        if number.isdigit():
            num=int(number)
            if len(number)==10:
                break
        else:
            print("invalid number")
    while True:
        email=input("enter email : ")
        if "@" in email and email.endswith(".com"):
            break
        else:
            print("invalid email")

    contact={
            "name":name,
            "number":number,
            "email":email
        }
    data.append(contact)
    with open("data.json","w") as file:
        json.dump(data,file,indent=4)
        print("data save successfully")

def search():
    with open("data.json","r") as file:
        data=json.load(file)
        print("=========: search data :=========")
    while True:
        name=input("enter name : ")

        for i in data:
            if i["name"] == name:
                print(i)
                break
            else:
                print("data not found")

def update():
     with open("data.json","r+") as file:
        data=json.load(file)

        while True:
            print("======================")
            print("1 : name")
            print("2 : number")
            print("3 : email")
            print("4 : exit")

            choice=int(input("enter choice : "))

            if choice==1:
                name1=input("enter corrent name : ")
                name2=input("enter new name : ")
                
                for i in data:
                   if i["name"]==name1:
                    i["name"]=name2

                    with open("data.json","w") as file:
                        json.dump(data,file,indent=4)

                        print("save name successfully")
            elif choice==2:
                    with open("data.json","r") as file:
                        data=json.load(file)
                    num1=input("enter corrent number : ")
                    num2=input("enter new number : ")
                    for i in data:
                        if i["number"]==num1:
                          i["number"]=num2

                    with open("data.json","w") as file:
                         json.dump(data,file,indent=4)
                    print("save number successfully")
            elif choice==3:
                    with open("data.json","r+") as file:
                        data=json.load(file)
                    email1=input("enter corrent email : ")
                    email2=input("enter new email : ")
                    for i in data:
                     if i["email"]==email1:
                          i["email"]=email2

                    with open("data.json","w") as file:
                            json.dump(data,file,indent=4)
                            print("save email successfully")
            else:
                print("thank you ")
                break

def delete():
        with open("data.json","r") as file:
            data=json.load(file)
        name=input("enter name : ")
        for i in data:
            if i["name"].lower()==name.lower():
                data.remove(i)
                with open("data.json",'w') as file:
                    json.dump(data,file,indent=4)
                print("delete data successfully")
            else:
                print("data not found")

while True:
    print("===========: menu :============")
    print("1 : add")
    print("2 : search")
    print("3 : update")
    print("4 : delete")
    print("5 : exit")

    choice=input("enter choice : ")
    if choice.isdigit():
        ch=int(choice)
    else:
        print("invalid choice")

    if ch==1:
        add()
    elif ch==2:
        search()
    elif ch==3:
        update()
    elif ch==4:
        delete()
    elif ch==5:
        print("thank you")
        break
    else:
        print("invalid")
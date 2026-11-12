import os 
import json
import datetime
path=r"C:\Users\AFREEN\Desktop\indixpert.tasks\bank_managment\bank_store\bank.json"
path1=os.path.join(path)
path2=r"C:\Users\AFREEN\Desktop\indixpert.tasks\bank_managment\error\bank.log"
error=os.path.join(path2)

class update:
    def __init__(self):
        self.date=datetime.datetime.now()
        pass
    def read(self):
            with open(path1,"r+") as file:
                data=json.load(file)
                return data
    def write(self,data):
                
            with open(path1,"w") as file:
                json.dump(data,file,indent=4)
    def update_profile(self):
        data=self.read()
        while True:
            print("------- UPDATE MENU -------")
            print("1 : name")
            print("2 : email")
            print("3 : address")
            print("4 : exit")
            while True:
                ch=input("enter choice : ")
                if ch.isdigit():
                    choice=int(ch)
                    break
                else:
                    print("invalid")
                    
            if choice==1:
                name1=input("enter corrent name : ")
                name2=input("enter new name : ")
                for i in data:
                    if i["name"]==name1:
                       i["name"]=name2
                       print("----- update name successfully -----")
                       self.write(data)
                    else:
                        print("invalid name")
                        with open(error,"a") as file:
                            file.write(f"[str{self.date}] [error] {name1} \n")
                        
            elif choice==2:
                email1=input("enter corrent email : ")
                email2=input("enter new email : ")
                for i in data:
                    if i["email"]==email1:
                        i["email"]=email2
                        print("------ update email successfully ------")
                        self.write(data)
                    else:
                        print("invalid email")
                        with open(error,"a") as file:
                            file.write(f"[str{self.date}] [error] {email1} \n")
                       
            elif choice==3:
                address1=input("enter corrent address : ")
                address2=input("enter new address : ")
                for i in data:
                    if i["address"]==address1:
                        i["address"]=address2
                        print("------- update address successfully -------")
                        self.write(data)
                    else:
                        print("invalid address")
                        with open(error,"a") as file:
                            file.write(f"[str{self.date}] [error] {address1} \n")
                        
            elif choice==4:
                print("thank you ")
                break
            else:
                print("invalid choice")


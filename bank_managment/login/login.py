import os
import json
import datetime
path=r"C:\Users\AFREEN\Desktop\indixpert.tasks\bank_managment\bank_store\bank.json"
path1=os.path.join(path)
path2=r"C:\Users\AFREEN\Desktop\indixpert.tasks\bank_managment\error\bank.log"
error=os.path.join(path2)

class login:
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
    def login_account(self):
        print("--------- FILL THE DETAILS TO LOGIN ---------")
        data=self.read()
        
        email1=input("enter email : ")
        password1=input("enter password : ")

        for i in data:
            if i["email"]==email1:
                if i["password"]==password1:
                    print("------- login successfully -------")
                    return True
                else:
                    print("invalid password...")
                    with open(error,"a") as file:
                        file.write(f"[str{self.date}] [error] {password1} \n")
                    return False
        else:
            print("invalid email...")
            with open(error,"a") as file:
                file.write(f"[str{self.date}] [error] {email1} \n")
            return False
obj=login()
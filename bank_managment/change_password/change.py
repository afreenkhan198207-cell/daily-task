import os
import json
import datetime

path=r"C:\Users\AFREEN\Desktop\indixpert.tasks\bank_managment\bank_store\bank.json"
path1=os.path.join(path)
path2=r"C:\Users\AFREEN\Desktop\indixpert.tasks\bank_managment\error\bank.log"
error=os.path.join(path2)

class change:
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
    def change_password(self):
        data=self.read()
        print("--------- CHANGE PASSWORD ----------")
        password1=input("enter corrent password : ")
        password2=input("enter new password : ")
        for i in data:
            if i["password"]==password1:
                i["password"]=password2
                print("------- change password successfully --------")
                self.write(data)
        else:
            print("data not found")
            with open(error,"a") as file:
                file.write(f"[str{self.date}] [error] {password1} \n")


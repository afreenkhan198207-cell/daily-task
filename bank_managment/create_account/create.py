import os 
import json
import datetime
import uuid
path=r"C:\Users\AFREEN\Desktop\indixpert.tasks\bank_managment\bank_store\bank.json"
path1=os.path.join(path)
path2=r"C:\Users\AFREEN\Desktop\indixpert.tasks\bank_managment\error\bank.log"
error=os.path.join(path2)

class create:
    def __init__(self):
        self.date=datetime.datetime.now()
        self.number=int(uuid.uuid4().hex[:6],16)
    def read(self):
        with open(path1,"r+") as file:
            data=json.load(file)
            return data
    def write(self,data):
            
        with open(path1,"w") as file:
            json.dump(data,file,indent=4)
    def creat_account(self):
        data=self.read()

        accounts={}
        while True:
            accounts["name"]=input("enter name : ")
            if len(accounts["name"])>2:
                break
            else:
                print("invalid name")
                with open(error,"a") as file:
                    file.write(f"[str{self.date}] [error] {accounts["name"]} \n")
        while True:
            accounts["email"]=input("enter email : ")
            if "@" in accounts["email"] and accounts["email"].endswith(".com"):
                break
            else:
                print("invalid email")
                with open(error,"a") as file:
                    file.write(f"[str{self.date}] [error] {accounts["email"]} \n")
        while True:
            accounts["password"]=input("enter password : ")
            if "password".isalnum():
                if len(accounts["password"])>=6:
                    break
            else:
                print("invalid password")
                with open(error,"a") as file:
                    file.write(f"[str{self.date}] [error] {accounts["password"]} \n")
        while True:
            account_balance=input("enter account balance : ")
            if account_balance.isdigit():
                    accounts["account_balance"]=int(account_balance)
                
                    break
            else:
                print("invalid amount")
                with open(error,"a") as file:
                    file.write(f"[str{self.date}] [error] {accounts["account_balance"]} \n")
        accounts["address"]=input("enter address : ")
        accounts["account_number"]=self.number
        
        data.append(accounts)
        self.write(data)



    
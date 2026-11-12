import os 
import json
import datetime

path=r"C:\Users\AFREEN\Desktop\indixpert.tasks\bank_managment\bank_store\bank.json"
path1=os.path.join(path)
path2=r"C:\Users\AFREEN\Desktop\indixpert.tasks\bank_managment\error\bank.log"
error=os.path.join(path2)

class transfer:
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
    def transfer_money(self):
        data=self.read()
        
        print("-------- TRANSFER MONEY ---------")
        account_number1=int(input("enter first account number : "))
        account_number2=int(input("enter second account number : "))
        amount=int(input("enter amount : "))

        for i in data:
            if i["account_number"] == account_number1:
                sender = i

            if i["account_number"] == account_number2:
                receiver = i

        if sender and receiver:
            if int(sender["account_balance"]) >= amount:

                sender["account_balance"] = int(sender["account_balance"]) - amount
                receiver["account_balance"] = int(receiver["account_balance"]) + amount

                print(f"total amount {sender['account_balance']}")
                print("------- transfer amount successfully -------")

                self.write(data)
                return True

            else:
                print("insufficient balance")
        else:
            print("data not found")
            with open(error,"a") as file:
                file.write(f"[str{self.date}] [error] {account_number1} \n")
            return False
       


import os
import json
import datetime
path=r"C:\Users\AFREEN\Desktop\indixpert.tasks\bank_managment\bank_store\bank.json"
path1=os.path.join(path)
path2=r"C:\Users\AFREEN\Desktop\indixpert.tasks\bank_managment\error\bank.log"
error=os.path.join(path2)

class withdraw:
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
    def withdraw_money(self):
        data=self.read()
        
        print("-------- WITHDRAW MONEY --------")
        account_number=int(input("enter account number : "))
        withdraw_amount=int(input("enter withdraw amount : "))
        for i in data:
            if i["account_number"]==account_number:
                    
                if i["account_balance"]>=withdraw_amount:
                    i["account_balance"]=i["account_balance"]-withdraw_amount
                    print(f"corrent balance is {i["account_balance"]}")
                    self.write(data)
                    return True
                else:
                    print("withdraw amount is more then corrent balance")
                    
                    return False
                    
        else:
            print("data not found")
            with open(error,"a") as file:
                file.write(f"[str{self.date}] [error] {account_number} \n")

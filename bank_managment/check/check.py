import os
import json
import datetime
path=r"C:\Users\AFREEN\Desktop\indixpert.tasks\bank_managment\bank_store\bank.json"
path1=os.path.join(path)
path2=r"C:\Users\AFREEN\Desktop\indixpert.tasks\bank_managment\error\bank.log"
error=os.path.join(path2)


class check:
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
    def check_balance(self):
        data=self.read()
        print("--------- CHECK BALANCE ----------")
            
        account_number1=int(input("enter account number : "))
        for i in data:
            if i["account_number"]==account_number1:
                print(i["account_balance"])
                return True 
            else:
                print("data not found")
                with open(error,"a") as file:
                    file.write(f"[str{self.date}] [error] {account_number1} \n")
                return False

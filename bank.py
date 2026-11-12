
from bank_managment.change_password.change import change
from bank_managment. check.check import check
from bank_managment. create_account.create import create
from bank_managment.deposit.deposit import deposit
from bank_managment. transfer.transfer import transfer
from bank_managment. update.update import update
from bank_managment. withdraw.withdraw import withdraw
from bank_managment.login.login import login

def main(): 
         
        while True:
            print("---------- ACCOUNT MENU ----------")
            
            print("1 : check balance")
            print("2 : deposit money")
            print("3 : withdraw money")
            print("4 : transfer money")
            print("5 : update profile")
            print("6 : change password")
            print("7 : logout")
            
            choice=int(input("enter choice : "))
            
            if choice==1:
                obj=check()
                obj.check_balance()
                
            elif choice==2:
                obj=deposit()
                obj.deposit_money()
                
            elif choice==3:
                obj=withdraw()
                obj.withdraw_money()
                
            elif choice==4:
                obj=transfer()
                obj.transfer_money()
                
            elif choice==5:
                obj=update()
                obj.update_profile()
                
            elif choice==6:
                obj=change()
                obj.change_password()
                
            elif choice==7:
                print("====== logout ======")
                break
            else:
                print("invalid choice")



def menu():
    while True:
        print("========= MENU =========")
        print("1 : creat account")
        print("2 : login")
        print("3 : exit")

        while True:
            ch=input("enter choice : ")
            if ch.isdigit():
                choice=int(ch)
                break
            else:
                print("invalid")
    
        if choice==1:
            obj=create()
            obj.creat_account()
        elif choice==2:
            obj=login()
            obj.login_account()
            main()
        elif choice==3:
            print("thank you ")
            break
        else:
            print("invalid choice")
menu()




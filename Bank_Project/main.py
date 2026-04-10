import json
import random
import string
from pathlib import Path


class Bank:
    database = Path(__file__).parent / 'data.json'
    data = []

    try:
        if database.exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")

    except Exception as err:
        print(f"An Error occurred as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*()_+", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)






    def Createaccount(self):
        info = {
            "name": input("Tell us your name: "),
            "age": int(input("Tell us your age: ")),
            "email": input("Tell us your email: "),
            "pin": int(input("Tell us your 4 digit pin: ")),
            "accountNo": Bank.__accountgenerate(),
            "balance": 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry, you are not eligible to create an account")
        else:
            print("Congratulations, your account has been created successfully")
            for i in info:
                print(f"{i}: {info[i]}")
            
            print("Please note down your account number for future reference")
            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):    
        account_no = input("Please tell your account number: ")
        pin = int(input("Please tell your 4 digit pin: "))

        userdata = [i for i in Bank.data if i['accountNo'] == account_no and i['pin'] == pin]

        if userdata == False:
            print("Sorry, Data not found")

        else:
            amount = int(input("How much money do you want to deposit: "))
            if amount > 10000 or amount <= 0:
                print("Sorry, you cannot deposit more than 10000 at a time")
            
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print(f"Congratulations, you have successfully deposited {amount} in your account")

    def withdrawmoney(self):    
        account_no = input("Please tell your account number: ")
        pin = int(input("Please tell your 4 digit pin: "))

        userdata = [i for i in Bank.data if i['accountNo'] == account_no and i['pin'] == pin]

        if userdata == False:
            print("Sorry, Data not found")

        else:
            amount = int(input("How much money do you want to withdraw: "))
            if userdata[0]['balance'] < amount:
                print("Sorry, you cannot withdraw more than your balance")
            
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print(f"Congratulations, you have successfully withdrawn {amount} from your account")


    def showdetails(self):
        account_no = input("Please tell your account number: ")
        pin = int(input("Please tell your 4 digit pin: "))

        userdata = [i for i in Bank.data if i['accountNo'] == account_no and i['pin'] == pin]

        print("Your account details are as follows\n:")
        for i in userdata[0]:
            print(f"{i}: {userdata[0][i]}")

    def updateaccount(self):
        account_no = input("Please tell your account number: ")
        pin = int(input("Please tell your 4 digit pin: "))  

        userdata = [i for i in Bank.data if i['accountNo'] == account_no and i['pin'] == pin]

        if userdata == False:
            print("Sorry, Data not found")
        else:
            print("You can update your name, age and balance")
            print("Fill the details you want to update and leave the rest blank")

            newdata = {
                "name": input("Please tell your name or press enter to skip: ") or userdata[0]['name'],
                "email": input("Please tell your New email or press enter to skip: ") or userdata[0]['email'],
                "pin": int(input("Please tell your New 4 digit pin or press enter to skip: ") or userdata[0]['pin']),
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']

            newdata['age'] = userdata[0]['age']

            newdata['accountNo'] = userdata[0]['accountNo']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("Congratulations, your account details have been updated successfully")

    def deleteaccount(self):
        account_no = input("Please tell your account number: ")
        pin = int(input("Please tell your 4 digit pin: "))

        userdata = [i for i in Bank.data if i['accountNo'] == account_no and i['pin'] == pin]

        if userdata == False:
            print("Sorry, Data not found")
        else:
            check = input("Are you sure you want to delete your account? (y/n): ")
            if check.lower() == 'n' or check.lower() == 'no' or check.lower() == 'N':
                print("bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
            
                print("Congratulations, your account has been deleted successfully")
                Bank.__update()


user = Bank()

print("Welcome to the Bank")
print("Press 1 to Create an Account")
print("Press 2 for Depositing the Money in the Bank")
print("Press 3 for Withdrawing the Money from the Bank")
print("Press 4 for Details of the Account")
print("Press 5 for Updating the Account Details")
print("Press 6 for Deleting the Account")


check = int(input("Enter your choice: "))

if check == 1:
    user.Createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.deleteaccount()






import json
import random
import string
from pathlib import Path


class Bank:
    database="data.json"
    data=[]
try:
    if Path(database).exists():
        
        
     with open(database)as fs:
        data=json.loads(fs.read())
    else:
        print("no such files exists")
except Exception as err:
    print(f"an exception occured as{err}")
    def createaccount(self):
        data={
            "name":input("Tell your name:-"),
            "age":int(input("tell your age:-")),
            "email":input("tell your email:-"),
            "pin":int(input("tell your 4 number pin:-")),
            "accountNo.":1234,
            "balance":0
        }
        if data['age']<18 or len(str{data['pin']})!=4:
            print()
        pass
    user=Bank()
print("press 1 for crating an account")
print("press 2  for depositing the money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

int(input("tell your response:"))
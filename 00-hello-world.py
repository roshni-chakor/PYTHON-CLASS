print("welcome to ATM")
print("-------------------------")
phone=(input("enter your phone number:"))
bal_part_1=phone[0:2]
bal_part_2=phone[4:6]
bal_str=bal_part_1+bal_part_2
bal=int(bal_str)

spin_str=phone[6:]
spin=int(spin_str)

name=input("Enter your name:")
pin=int(input("Enter pin"))
if pin==spin:
    print("welcome",name)
    wi=int(input("Enter amount:"))
    if wi<=bal:
        if wi %100==0:
            print("---------------")
            print("Transaction is success")
            bal-= wi
            print("your available balance:",bal)
        else:
            print("invalid amount") 
    else:
        print("insufficient balance")
else:
    print("invalid PIN,please try again")                   
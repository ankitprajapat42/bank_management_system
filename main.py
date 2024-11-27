import string

def password_cheaker():
    small = string.ascii_lowercase
    capital=string.ascii_uppercase
    symbol=string.punctuation
    numbers=string.digits
    while True:
        password=input('Enter Password')
        if len(password)>=8:
            d={'small':False,'capital':False,'symbols':False,'numbers':False}
            for i in password:
                if i in small:
                    d['small']=True
                elif i in capital:
                    d['capital']=True
                elif i in symbol:
                    d['symbols']=True
                elif i in numbers:
                    d['numbers']=True
            if tuple(d.values()).count(True)==4:
                return password
                
            else:
                print('Password is Not Strong')
                for i in d:
                    if d[i]==False:
                        print(i,'is Missing')
    
        else:
            print('Password is not Strong , As It has less than 8 Characters')


database = {"SBI101": {'Name':"Anurag Dhakad",
                       'Mobile No': 9460602957,
                       'Address' : 'Alwer',
                       'Balance' : 21020,
                       'Password': "Ankit@123"
                        },
            "SBI102": {'Name':'Amit kumar',
                       'Mobile No': 9413881315,
                       'Address' : 'Vaishali Nagar, Ajmer',
                       'Balance' : 250,
                       'Password': "Ajay@1315"
                        }
            
    
            }
while True:
    print("\n","Welcome to SBI Bank".center(50,'*'),"\n")
    print("1.press 1 for Login\n2.Press 2 for Signup\n3.Press 3 for Forget password\n4.Press 4 for Exit")
    choice = input("Enter your choice : ")
    if choice == '1':
        print("\n","Login".center(50,"="), "\n")
        account_no = input("Enter the account number : ")
        if account_no in list(database.keys()):
            password = input("Enter the password : ")
            if password == database[account_no]['Password']:
                print("\n", "Login Successful".center(50, "="),"\n")
                while True:
                    print("1.Press 1 for Credit \n2.Press 2 for Debit \n3.Press 3 for Change Password \n4.Press 4 for Cheak Balance \n5.Press 5 for Show Deitals \n6.Press 6 for Logout")
                    choice = input("Enter your Choice : ")
                    if choice == '1':
                        c_rupee = int(input("Enter the Credit Money: "))
                        database[account_no].update({'Balance':(database[account_no]['Balance']+c_rupee)})
                        print("Now Total Blance is : ", database[account_no]['Balance'])
                        print("Credit Succesful".center(50,"="), "\n")
                        
                    elif choice == '2':
                        d_rupee = int(input("Enter the Money: "))
                        if d_rupee<=database[account_no]['Balance']:
                            database[account_no].update({'Balance':(database[account_no]['Balance']-d_rupee)})
                            print("Now Total Blance is : ", database[account_no]['Balance'])
                            print("Debit Succesful".center(50,"="), "\n")
                        else:
                            print("Thiis Ammount is Out of range your Balance")
                            print("Debit Faild".center(50,"-"), "\n")
                        
                    elif choice == '3':
                        old_password = input("Enter the old password : ")
                        if old_password == database[account_no]['Password']:
                            new_password = password_cheaker()
                            database[account_no].update({"Password":new_password})
                            print("Password is Changed Succesful".center(50,"="), "\n")
                        else:
                            print("You Enter incorrect password")
                            print("Failed".center(50,"-"), "\n")
                        
                        
                    elif choice == '4':
                        print("-"*50)
                        print(f"Totel Balance : {database[account_no]["Balance"]}")
                        print("-"*50)
                    
                    elif choice == '5':
                        print("\n","Deitals".center(50,"="), "\n")
                        
                        print(f"Account No: {account_no}")
                        print(f"Name : {database[account_no]['Name']}")
                        print(f"Mobile No: {database[account_no]['Mobile No']}")
                        print(f"Address : {database[account_no]['Address']}")
                        print(f"Balance : {database[account_no]['Balance']}")
                        print(f"Password : {database[account_no]['Password']}\n",)
                        
                    elif choice == '6':
                        break
                    else:
                        print("You enter invalid option".center(50,"-"))

            else:
                print("You Enter incorrect password".center(50,"="))
        else:
            print("you enter invalid Account Number".center(50,"-"))
    
    elif choice == '2':
        print("\n","SignUp".center(50,"*"), "\n")
        name = input("Enter the Name : ")
        mobile_no = int(input("Enter the mobile no. : "))
        address = input("Enter the Address : ")
        password1 =password_cheaker()
        account = str(list(database.keys())[-1][0:3]+str(int(list(database.keys())[-1][3:])+1))
        
        database.update({account:{}})
        database[account].update({"Name":name, "Mobile No": mobile_no, "Address" : address, "Password": password1, "Balance" : 0})
        print("* Your Account is Succesfully Created, ".center(50))
        print(f"Account No : {account} \nPassword : {database[account]['Password']}")
        
    elif choice == '3':
        account_no = input("Enter the account no : ")
        if account_no in list(database.keys()):
            mobile_no = int(input("Enter your mobile number : "))
            if mobile_no == database[account_no]['Mobile No']:
                new_password = password_cheaker()
                database[account_no].update({'Password':new_password})
                print("Password is Changed".center(50, "="))
            else:
                print("You Enter incorrect mobile no".center(50,"-"),"\n")
        else:
            print("You enter invalid Account No".center(50,"-"))
    elif choice == '4':
        print("Application close".center(50, "-"))
        break
    else:
        print('You enter invalid option,'.center(50,'-'))

import pyttsx3
machine = pyttsx3.init()

def mach(s1 ,s2):
    rate = machine.getProperty("rate")
    volume=machine.getProperty("volume")
    voices = machine.getProperty("voices")
    machine.setProperty("rate",135)
    machine.setProperty("volume",volume+1.0)   # voices[1] is "Microsoft Zira Desktop" (female).
    machine.setProperty('voice', voices[1].id)
    machine.say(s1)
    machine.say(s2)
    machine.runAndWait()


class Account:
    def __init__(self,acc,bal,pas):
        self.acc=acc
        self.bal=bal
        self.pas=pas
        
    def __debit(self,amt): #private
        self.bal-=amt
        m1=f"Rs {amt} is debited"
        m2=f"Balance left {self.bal}"
        print(m1)
        print(m2)
        mach(m1,m2)
        
    def __credit(self,amt): #private
        self.bal+=amt
        m3=f"Rs {amt} is credited"
        m4=f"Balance left {self.bal}"
        mach(m3,m4)
        print(m3)
        print(m4)

    def password_debit(self):
        amt=int(input("Amount want to debit: "))
        p=int(input("Enter password: "))
        if(p==self.pas):
            return self.__debit(amt)
        else:
            m5="Wrong password...Better luck for next time"
            mach(m5,"")
            print(m5)

    def password_credit(self):
        amt=int(input("Amount want to credit: "))
        ac=(input("Enter Account number: "))
        if(ac==self.acc):
            return self.__credit(amt)
        else:
            m6="It's not your account number. please try again"
            mach(m6,"")
            print(m6)

    def check_bal(self):
        p=int(input("Enter password: "))
        if(p==self.pas):
            m7=f"Balance left {self.bal}"
            mach(m7,"")
            print(m7)
        else:
            m8="Wrong password.We can't show you balance"
            mach(m8,"")
            print(m8)


a1=Account("abcd1234",10000,9933)
print("....Welcome to RNSO bank.... ")

while(True):
    print("1 for check balance \n2 for debit \n3 for credit \n4 for exit")
    st=input("Enter your choice: ")
    if(st=="4"): 
        break
    match(st):
        case("1"):
            a1.check_bal()
            print()
            
        case("2"): 
            a1.password_debit()
            print()
    
        case("3"): 
                a1.password_credit()
                print()
            
        case("4"): 
            print("Thanks for visiting us....")
            break
        case _: 
            print("Invalid choice try again later")


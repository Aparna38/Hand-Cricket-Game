import random
print("!!!!!!HAND CRICKET!!!!!!")
n = random.randint(0,10)
ch=input("Select odd or eve ")
u=int(input("Enter a number for toss"))
print("computer chose ",n)
sum0=0
sum1=0
if ch=="eve":
    if(u+n)%2==0:
        tosswin="user"
        print("You won toss")
        batorbowl=input("Enter batting or bowling")
    else:
        tosswin="computer"
        print("computer won toss")
        l=["batting","bowling"]
        batorbowl=random.choice(l)
else:
    if(u+n)%2==1:
        tosswin="user"
        print("You won toss")
        batorbowl=input("Enter batting or bowling")
    else:
        tosswin="computer"
        print("computer won toss")
        l=["batting","bowling"]
        batorbowl=random.choice(l)
usernum=1
compnum=0
if tosswin=="user":
    if batorbowl=="batting":
        print("You chose batting")
        while(True):
            usernum=int(input("Enter your run "))
            compnum=random.randint(0,10)
            print("Computer's ball ",compnum)
            if (usernum==compnum):
                    break
            sum0=sum0+usernum
        print("Your turn over now computer turn")
        usernum=1
        compnum=0
        while(sum1<=sum0+1):
            usernum=int(input("Bowl "))
            compnum=random.randint(0,10)
            print("Computer's run ",compnum)
            if (usernum==compnum):
                    break
            sum1=sum1+compnum
        print("Game over!!")
        if(sum0>sum1):
            print("Your score: ",sum0)
            print("Computer score: ",sum1)
            print("YOU WON :)")
        else:
            print("Your score: ",sum0)
            print("Computer score: ",sum1)
            print("COMPUTER WON ")

    else:
        while(True):
            usernum=int(input("bowl "))
            compnum=random.randint(0,10)
            print("Computer's run ",compnum)
            if (usernum==compnum):
                    break
            sum1=sum1+compnum
        print("computer turn over now your turn")
        usernum=1
        compnum=0
        while(sum0<=sum1+1):
            usernum=int(input("Enter your run "))
            compnum=random.randint(0,10)
            if (usernum==compnum):
                    break
            sum0=sum0+usernum
            print("Computer's ball ",compnum)
        print("Game over!!")
        if(sum0>sum1):
            print("Your score: ",sum0)
            print("Computer score: ",sum1)
            print("YOU WON :)")
        else:
            print("Your score: ",sum0)
            print("Computer score: ",sum1)
            print("COMPUTER WON ")


if tosswin=="computer":
    if batorbowl=="batting":
        print("computer chose batting")
        while(True):
            usernum=int(input("Bowl "))
            compnum=random.randint(0,10)
            print("Computer's run ",compnum)
            if (usernum==compnum):
                    break
            sum1=sum1+compnum
        print("computer's batting turn over now your turn")
        usernum=1
        compnum=0
        while(sum0+1<=sum1+1):
            usernum=int(input("Enter your run "))
            compnum=random.randint(0,10)
            print("Computer's ball ",compnum)
            if (usernum==compnum):
                    break
            sum0=sum0+usernum
        print("Game over!!")
        if(sum0>sum1):
            print("Your score: ",sum0)
            print("Computer score: ",sum1)
            print("YOU WON :)")
        else:
            print("Your score: ",sum0)
            print("Computer score: ",sum1)
            print("COMPUTER WON ")
    else:
        print("computer chose bowling")
        while(True):
            usernum=int(input("Enter your run "))
            compnum=random.randint(0,10)
            print("Computer's ball ",compnum)
            if (usernum==compnum):
                    break
            sum0=sum0+usernum
        print("Your batting turn over now computer turn")
        usernum=1
        compnum=0
        while(sum1<=sum0+1):
            usernum=int(input("Bowl "))
            compnum=random.randint(0,10)
            print("Computer's run ",compnum)
            if (usernum==compnum):
                    break
            sum1=sum1+compnum
        print("Game over!!")
        if(sum0>sum1):
            print("Your score: ",sum0)
            print("Computer score: ",sum1)
            print("YOU WON :)")
        else:
            print("Your score: ",sum0)
            print("Computer score: ",sum1)
            print("COMPUTER WON ")
        

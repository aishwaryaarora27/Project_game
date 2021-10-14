import random
def winner(comp,plyr):
    if comp==plyr:
        return None
    elif comp=='S':
        if plyr=='W':
            return False
        elif plyr=='G':
            return True
    elif comp=='W':
        if plyr=='S':
            return True
        elif plyr=='G':
            return False
    elif comp=='G':
        if plyr=='S':
            return False
        elif plyr=='W':
            return True




comp=input("Computer's Turn: Snake(S), Water(W) or Gun(G)?")
n=random.randint(1,3)
if n==1:
    comp='S'
elif n==2:
    comp='W'
else:
    comp='G'
plyr=input("Your Turn: Snake(S), Water(W) or Gun(G)?") 
if plyr!='S' and plyr!='W' and plyr!='G':
    print("Please Enter valid choice")
else:
    res=winner(comp,plyr)
    print("Computer chose:"+comp)
    print("You chose:"+plyr)
    if res==None :
        print("It's a tie!")  
    elif res:
        print('You win!')
    else:
        print('You lose!')



def Disposit(wallet):
    dis=float(input('Enter how match do you want to disposit :'))
    wallet+=dis
    print('amount added successfully')
    return wallet

def expenses(wallet):
    category=input('enter the category of expense :')
    exp=float(input('enter how much :'))
    if wallet>=exp:
        if category in expence:
            expence[category]+=exp
        else:
            expence[category]=exp
    else:
        print('You dont have enought money')
    wallet-=exp
    return wallet
def Total():
    print(f'your amount is {wallet} $')
    for key,value in expence.items():
        print(f'you have paiyed {value} $ for {key}')


print('WELCOME')
print('1:add new revenue\n2:add expenses:\n3:Total&total expences\n4:Exit')
wallet=0
expence={}
while True:
    try:
        n=int(input('enter you choise :'))
        if n==1:
            wallet=Disposit(wallet)
        elif n==2:
            wallet=expenses(wallet)
        elif n==3:
            Total()
        elif n==4:
            print('good by')
            break
    except:
        print('wrrong choise')

        



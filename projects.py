import json
print('hello SR')
name=input('Please enter your name :')
age=int(input('please enter your age :'))

r=f'hi {name} your age is {age}'
with open('user','w')as file:
    json.dump(r,file,indent=4)
    print('data saved succesfully')

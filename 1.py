import json
def add_task():
    task=input('enter the task :')
    tasks[task]='Incomplet❌'
def show_taskes():
    j=1
    for key,value in tasks.items():
        print(f'{j}:{key} is {value}')
        j+=1
def complete():
    completed=int(input('enter the number of task you have completed :'))
    list_key=list(tasks.keys())
    if completed in range(len(list_key)+1) :
        tasks[list_key[completed-1]]='Completed✅'
def delete():
    i=int(input('enter the number of task you want to delete :'))
    list_key=list(tasks.keys())
    if i in range(len(list_key)+1):
        tasks.pop(list_key[i-1])
def save_file():
    with open('tasks.json','w')as file:
        json.dump(tasks,file,indent=4)

print('welcom back')
print('1:add task\n2:show tasks\n3:complite task\n4:delete task\n5:save tasks in json file\n6:exit')
tasks={}
while True:  
    try:
   
        n=int(input('enter your choise :'))
        if n==1:
            add_task()
        elif n==2:
            show_taskes()
        elif n==3:
            complete()
        elif n==4:
            delete()
        elif n==5:
            save_file()
        elif n==6:
            print('good by')
            break
        else:
            print(f'{n}: is not valaid')
    except:
        print('Invalaid choise')  

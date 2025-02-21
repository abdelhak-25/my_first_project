import json
tasks={}
print('Hello user')
print('your choise')
print('1:ADD NEW TASK \n2:SHOW LIST OF TASKS"\n3:COMPLETE A TASK\n4:DELET A TASK\n5:SAVE TASKS IN NEW FILE,6:Exit')

while True:
    try:
        choise=int(input('enter your choise : '))
        
        if choise==1:
            task=input('ENTER THE TASK  :')
            tasks[task]='INCOMPLITE❌'
            print('task added successfully')
                        
        elif choise==2:
            j=1
            for tsk,key in tasks.items():
                    print(f'{j}:the task {tsk} is {key} ')
                    j+=1
        elif choise==3:
            i=int(input('enter the number of task complited :'))
            list_key=list(tasks.keys())
            if i in range(len(list_key)):
                tasks[list_key[i-1]]='COMPLETED✅'             
        elif choise==4:
            pop_num=int(input('enter the number of task you want delet :'))
            tasks.pop(list_key[i-1])
        
        elif choise==5:
             file_name=input('Enter the name of file to save in jason')
             with open(file_name,'w')as file:
                  json.dump(tasks,file,indent=4)
             print('tasks saved successfully')

        elif choise==6:
            print('good by')
            break
    except:
         print('Enter the right choise')
      



    



    
    


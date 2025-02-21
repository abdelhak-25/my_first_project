

def add_Appointment():
    Appointment=input('enter the date of Appointment :')
    app_hour=input('enter the time of Appointment :')
    Appointments[Appointment]=app_hour
def show_Appointment():
    for key,value in Appointments.items():
        print(f'you have a date in {key} at {value}')
def delete_Appointment():
    m=int(input('for delete Appointment enter it`s number :'))
    list_key=list(Appointments.keys())
    if m in range(len(list_key)+1):
        Appointments.pop(list_key[m-1])
Appointments={}
print('welcome! to Management_Appointment')
print('1:Add Appointment\n2:Show Appointments\n3:Delete Appointment\n4:Exit')
while True:
    try:
        n=int(input('enter your choise :'))
        if n==1:
            add_Appointment()
        elif n==2:
            show_Appointment()
        elif n==3:
            delete_Appointment()
        elif n==4:
            print('Good by')
            break
    except :
        print('Invalaid choise')
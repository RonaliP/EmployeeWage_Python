import random
Total_workinghours=8
_wageperhour=20
Part_time_hours=4

def checkattendance():
    if random.randint(0,1) == 1:
        print("Employee is present today")
    else:
        print("Employee is absent today")

def calculatewage():
    print("Dailywage of employee is", Total_workinghours*_wageperhour)

if __name__ == '__main__':
    print("WELCOME TO EMPLOYEE WAGE CALCULATION PROGRAM")
    checkattendance()
    calculatewage()
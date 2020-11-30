import random
def checkattendance():
    if random.randint(0,1) == 1:
        print("Employee is present today")
    else:
        print("Employee is absent today")

if __name__ == '__main__':
    print("WELCOME TO EMPLOYEE WAGE CALCULATION PROGRAM")
    checkattendance()
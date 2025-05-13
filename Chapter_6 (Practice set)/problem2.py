marks1 = int(input("Enter Your marks Subject 1: "))
marks2 = int(input("Enter Your marks Subject 2: "))
marks3 = int(input("Enter Your marks Subject 3: "))

# check for total percentage

total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are pass",total_percentage,"%")

else:
    print("You failed, try again next year!",total_percentage,"%")


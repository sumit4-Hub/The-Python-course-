a = int(input("Enter Your age: "))

if(a>=18):
    print("You are above the age of consent")
    print("Good for You")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age")

else:
    print("You are below the age of consent")

print("end of program")
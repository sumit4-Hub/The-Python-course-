username = input("Enter Your Username: ")

characters = (len(username)<10)

if(characters):
    print("This username is less than 10 characters")

else:
    print("This username is not less than 10 characters")
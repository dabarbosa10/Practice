def save_user_data():
    name = input("Enter name: ")
    email = input("Enter email: ")
    contact = input("Enter contact: ")

    user_data= f"Name: {name}\nEmail: {email}\nContact: {contact}\n"

    with open("user_data.txt", "a") as file: 
        file.write(user_data)

save_user_data()
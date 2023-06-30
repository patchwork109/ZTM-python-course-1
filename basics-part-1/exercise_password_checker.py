username = input("What's your username? \n")
password = input("What's your password? \n")
password_length = len(password)
hidden_password = len(password) * '*'

message = f"{username}, your password, {hidden_password}, is {password_length} characters long."
print(message)
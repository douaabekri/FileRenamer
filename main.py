from FileRenamer import File  

USER_DATA_FILE = "users1.txt"

usernames = []
passwords = []

def load_users():
    try:
        with open(USER_DATA_FILE, 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                usernames.append(username)
                passwords.append(password)
    except FileNotFoundError:
        pass

def save_user(username, password):
    with open(USER_DATA_FILE, 'a') as file:
        file.write(f"{username},{password}\n")

def sign_up():
    username = input("Enter a username: ").strip()
    if username in usernames:
        print("Username already taken. Please try another.")
        return
    
    password = input("Enter a password: ").strip()
    usernames.append(username)
    passwords.append(password)
    save_user(username, password)  
    
    print("Sign-up successful! You can now log in.")

def login():
    username = input("Enter your username: ").strip()
    if username not in usernames:
        print("Username not found. Please sign up first.")
        return
    
    password = input("Enter your password: ").strip()
    user_index = usernames.index(username)
    
    if passwords[user_index] == password:
        print(f"Login successful! Welcome, {username}.")
        File.FileRenamer() 
    else:
        print("Incorrect password. Please try again.")

if __name__ == "__main__":
    load_users() 
    
    while True:
        print("\n--- Menu ---")
        print("1. Sign Up")
        print("2. Login")
        print("3. Quit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            sign_up()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

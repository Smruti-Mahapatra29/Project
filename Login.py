import hashlib
import os

# File to store user credentials (username:hashed_password)
USER_DATA_FILE = 'user_data.txt'

def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def save_user(username, password):
    """Save a new user's username and hashed password to the file."""
    with open(USER_DATA_FILE, 'a') as f:
        f.write(f"{username}:{hash_password(password)}\n")

def check_user_exists(username):
    """Check if the user already exists in the file."""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            users = f.readlines()
            for user in users:
                stored_username, _ = user.strip().split(':')
                if stored_username == username:
                    return True
    return False

def verify_login(username, password):
    """Verify if the provided username and password match stored credentials."""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            users = f.readlines()
            for user in users:
                stored_username, stored_password = user.strip().split(':')
                if stored_username == username and stored_password == hash_password(password):
                    return True
    return False

def sign_up():
    """Handle user sign-up."""
    print("\n--- Sign Up ---")
    username = input("Enter a username: ")
    
    if check_user_exists(username):
        print("Username already exists. Try logging in or use a different username.")
    else:
        password = input("Enter a password: ")
        confirm_password = input("Confirm password: ")
        
        if password == confirm_password:
            save_user(username, password)
            print("Sign up successful! You can now log in.")
        else:
            print("Passwords do not match. Please try again.")

def sign_in():
    """Handle user sign-in."""
    print("\n--- Sign In ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if verify_login(username, password):
        print(f"Welcome, {username}! You are now logged in.")
    else:
        print("Invalid username or password. Please try again.")

def main():
    """Main function to handle user choices."""
    while True:
        print("\n1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            sign_up()
        elif choice == '2':
            sign_in()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

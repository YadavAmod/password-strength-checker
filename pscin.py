import re
import getpass  # To hide password input

def check_password_strength(password):
    feedback = []
    strength = "Weak"

    # Check length of the password
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check if password contains both uppercase and lowercase letters
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Check if password contains numbers
    if not re.search(r'[0-9]', password):
        feedback.append("Password should contain at least one digit.")
    
    # Check if password contains special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Password should contain at least one special character (e.g., !, @, #, etc.).")
    
    # Determine strength level
    if len(feedback) == 0:
        strength = "Very Strong"
    elif len(feedback) == 1 or len(password) >= 12:
        strength = "Strong"
    elif len(feedback) == 2:
        strength = "Moderate"
    
    return strength, feedback

def main():
    print("Password Strength Checker")
    print("Enter 'q' to quit the program.")
    
    while True:
        password = getpass.getpass("\nEnter a password to check: ")  # Password is masked (hidden)
        
        if password.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break
        
        strength, feedback = check_password_strength(password)
        
        print(f"\nPassword Strength: {strength}")
        if feedback:
            print("Suggestions to improve your password:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        else:
            print("Great job! Your password is very strong.")

if __name__ == "__main__":
    main()

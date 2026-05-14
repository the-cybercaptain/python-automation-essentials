import random
import string
import re

# Generates a secure random password of given length.
# Ensures at least one uppercase, lowercase, digit, and special character.

def generate_password(pass_length):
    # If password length is less than 4, return an error message
    if pass_length < 4:
        return "❌ Password length should be at least 4 characters for generating."
    else:
        # Ensure the password has at least one uppercase, one lowercase, one digit, and one special character
        upper = random.choice(string.ascii_uppercase)
        lower = random.choice(string.ascii_lowercase)        
        digit = random.choice(string.digits)                 
        special = random.choice(string.punctuation)

        # Calculate how many characters remain to fill after the 4 required characters
        remaining_length = pass_length - 4

        # Pool of all possible characters (letters, digits, punctuation)
        all_characters = string.ascii_letters + string.digits + string.punctuation

        # Generate random characters for the remaining length
        remaining_chars = [random.choice(all_characters) for _ in range(remaining_length)]
        
        # Combine all required and remaining characters into one list
        password_list = [upper, lower, digit, special] + remaining_chars

        # Shuffle the list to ensure randomness of character positions
        random.shuffle(password_list)

        # Join the list into a single string as the final password
        passwd = ''.join(password_list)
        return passwd
    

# Checks the strength of the given password.
# Evaluates based on length, uppercase, lowercase, digit, and special character.
# Returns visual bar, label, description, and score.

def check_password_strength(password, remarks):
    strength = 0

    # Remove spaces from password and calculate length
    length_password = len(password.replace(" ", ""))

    # Check if length is at least 8 characters
    if length_password >= 8:
        remarks.append("✅ Password length is equal or more than 8 characters.")
        strength += 1
    else:
        remarks.append("❌ Password length should be at least 8 characters.")

    # Check for at least one uppercase letter
    if re.search(r'[A-Z]', password):
        remarks.append("✅ Your Password has at least one uppercase letter.")
        strength += 1
    else:
        remarks.append("❌ Password should have at least one uppercase letter.")

    # Check for at least one lowercase letter
    if re.search(r'[a-z]', password):
        remarks.append("✅ Your Password has at least one lowercase letter.")
        strength += 1
    else:
        remarks.append("❌ Password should have at least one lowercase letter.")

    # Check for at least one digit
    if re.search(r'[0-9]', password):
        remarks.append("✅ Your Password has at least one digit.")
        strength += 1
    else:
        remarks.append("❌ Password should have at least one digit.")

    # Check for at least one special character
    if re.search(rf"[{string.punctuation}]", password):
        remarks.append("✅ Your Password has at least one special character.")
        strength += 1
    else:
        remarks.append("❌ Password should have at least one special character.")

    # Return a visual strength bar, label, description, and score based on how many conditions passed
    if strength == 5:
        return "[██████████]", "🔒 Excellent", "✅ Password is strong.", 10
    
    elif strength == 4:
        return "[████████  ]", "🟢 Good", "🔸 Password is moderate.", 8
    
    elif strength == 3:
        return "[██████    ]", "🟡 Fair", "⚠️ Password is medium.", 6
    
    elif strength == 2:
        return "[██        ]", "🔴 Poor", "❌ Password is weak.", 2
    
    else:
        return "[█         ]", "🔴 Very Poor", "❌ Password is very weak.", 0
    


# Main program logic

if __name__ == "__main__":

    print("="*40)
    print("🔐 Password Generator & Strength Checker")
    print("="*40)

    while True:
        # Ask the user what they want to do: generate a password, check strength, or exit
        print("\n\nEnter your choice. What you want?")
        print("-"*40)

        print("1. Generate a password\n2. Check password strength\n3. Exit\n")
        print("-"*40)

        choice = input("Enter your choice: ")
        print("="*40)

        # Validate that the input starts with a digit        
        match = re.match(r'\s*(\d)', choice)
        if match:
            choice = match.group(1)
        else:
            print("❌ Invalid input. Please enter 1, 2, or 3.")
            print("-"*40)
            continue

        if choice == "1":
            # Loop to generate password repeatedly if user wants
            while True:
                pass_length = input("\nEnter password length: ").strip()
                print("-"*40)

                match = re.match(r'\s*(\d)', pass_length)
                if match:
                    pass_length= match.group(1)
                else:
                    print("❌ Invalid input. Please enter 1, 2, or 3.")
                    print("-"*40)
                    continue

                # Check if entered length is a valid number
                if pass_length.isdigit():
                    pass_length = int(pass_length)
                    generated_password = generate_password(pass_length)

                    # If generation failed due to length, print error message                    
                    if generated_password.startswith("❌"):
                        print(f"Generated Password: ➡️    {generated_password}    ⬅️\n")
                        print("="*40)

                    else:
                        # Print the generated password and its strength analysis
                        print(f"\nGenerated Password: ➡️    {generated_password}    ⬅️\n")
                        print("="*40)
                        pass_remarks = []
                        result = check_password_strength(generated_password, pass_remarks)
                        print(f"\n🔍 Result: {result}\n")
                        print("-"*40)
                        print("\n📝 Remarks:")
                        print("-"*40)
                        # Print all the remarks about the entered password
                        for i, remark in enumerate(pass_remarks, 1):
                            print(f"{i}. {remark}")
                        print("="*40)

                else:
                    print("\n❌ Invalid input. Please enter a number.\n")
                    print("-"*40)

                # Ask if user wants to continue generating passwords
                cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
                print("-"*40)

                if cont not in ("yes", "y"):
                    print("\nExiting...")
                    print("="*40)
                    break

        elif choice == "2":
            # Password strength checker
            your_password = input("\nEnter your Password : ").strip()
            print("="*40)
            remarks = []

            results = check_password_strength(your_password, remarks)
            print(f"\n🔍 Result: {result}\n")
            print("-"*40)
            print("\n📝 Remarks:")
            print("-"*40)

            # Print all the remarks about the entered password
            for i, remark in enumerate(pass_remarks, 1):
                print(f"{i}. {remark}")
            print("="*40)

        elif choice == "3":
            # Exit the program gracefully            
            print("\nExiting the program. Goodbye!")
            print("="*40)
            break
        
        # If invalid option was entered
        else:
            print("\nInvalid choice. Please choose a valid option.")
            print("="*40)

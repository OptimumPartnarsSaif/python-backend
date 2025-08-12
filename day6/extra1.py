import re

# ===== Exercise 1: Palindrome Checker with File I/O =====
def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def palindrome_checker():
    input_filename = 'input_words.txt'
    output_filename = 'palindromes.txt'
    
    try:
        with open(input_filename, 'r') as file:
            words = [line.strip() for line in file]
        
        palindromes = [word.upper() for word in words if is_palindrome(word)]
        
        with open(output_filename, 'w') as file:
            for word in palindromes:
                file.write(word + '\n')
                
        print(f"Palindromes written to {output_filename}")
        
    except FileNotFoundError:
        print("Error: Input file not found")
    except IOError:
        print("Error: File operation failed")

# ===== Exercise 2: Temperature Converter =====
def temp_converter():
    input_filename = 'celsius.txt'
    output_filename = 'fahrenheit.txt'
    
    try:
        with open(input_filename, 'r') as file:
            temps = []
            for line in file:
                try:
                    temp = float(line.strip())
                    temps.append(temp)
                except ValueError:
                    print(f"Skipping invalid temperature: {line.strip()}")
        
        with open(output_filename, 'w') as file:
            for temp in temps:
                fahrenheit = (temp * 9/5) + 32
                file.write(f"{temp:.1f}C = {fahrenheit:.1f}F\n")
                
        print(f"Converted temps written to {output_filename}")
        
    except FileNotFoundError:
        print("Error: Input file not found")
    except IOError:
        print("Error: File operation failed")

# ===== Exercise 3: User Registration =====
class InvalidLengthError(Exception): pass
class InvalidCharacterError(Exception): pass

def validate_username(username):
    if len(username) < 5 or len(username) > 15:
        raise InvalidLengthError("Must be 5-15 characters")
    if not username.isalnum():
        raise InvalidCharacterError("Must be alphanumeric")

def user_registration():
    username = input("Enter username: ")
    try:
        validate_username(username)
        with open('users.txt', 'a') as file:
            file.write(username + '\n')
        print("Registration successful!")
    except (InvalidLengthError, InvalidCharacterError) as e:
        print(f"Invalid username: {e}")
    except IOError:
        print("Error writing to file")
    finally:
        print("Registration attempt completed")

# ===== Exercise 4: Log File Analyzer =====
def log_analyzer():
    status_codes = {'200': 0, '404': 0, '500': 0}
    
    try:
        with open('server.log', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 2 and parts[1] in status_codes:
                    status_codes[parts[1]] += 1
        
        with open('report.txt', 'w') as file:
            file.write(f"Successful (200): {status_codes['200']}\n")
            file.write(f"Not Found (404): {status_codes['404']}\n")
            file.write(f"Server Error (500): {status_codes['500']}\n")
            
        print("Log analysis complete")
        
    except FileNotFoundError:
        print("Error: Log file not found")
    except IOError:
        print("Error: File operation failed")

# ===== Exercise 5: Password Strength Checker =====
def check_password_strength(password):
    if len(password) < 8:
        raise ValueError("Minimum 8 characters required")
    if not any(c.isupper() for c in password):
        raise ValueError("Missing uppercase letter")
    if not any(c.islower() for c in password):
        raise ValueError("Missing lowercase letter")
    if not any(c.isdigit() for c in password):
        raise ValueError("Missing digit")
    if not any(c in '!@#$%^&*' for c in password):
        raise ValueError("Missing special character")
    return True

def password_checker():
    strong_passwords = []
    
    try:
        with open('passwords.txt', 'r') as file:
            passwords = [line.strip() for line in file]
            
        for pwd in passwords:
            try:
                if check_password_strength(pwd):
                    strong_passwords.append(pwd)
            except ValueError as e:
                print(f"Weak password '{pwd}': {e}")
                
        with open('strong_passwords.txt', 'w') as file:
            file.write('\n'.join(strong_passwords))
            
        print(f"Found {len(strong_passwords)} strong passwords")
        
    except FileNotFoundError:
        print("Error: Password file not found")
    except IOError:
        print("Error: File operation failed")

# ===== Main Menu =====
def main():
    while True:
        print("\n=== Menu ===")
        print("1. Palindrome Checker")
        print("2. Temperature Converter")
        print("3. User Registration")
        print("4. Log Analyzer")
        print("5. Password Strength Checker")
        print("6. Exit")
        
        choice = input("Select exercise (1-6): ")
        
        if choice == '1':
            palindrome_checker()
        elif choice == '2':
            temp_converter()
        elif choice == '3':
            user_registration()
        elif choice == '4':
            log_analyzer()
        elif choice == '5':
            password_checker()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

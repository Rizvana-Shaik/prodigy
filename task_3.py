import re

def check_password_strength(password):
    """Assess the strength of a password and provide feedback."""
    strength = 0
    feedback = []
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character (e.g., !, @, #).")
    if strength == 5:
        feedback.append("Your password is very strong!")
        rating = "Very Strong"
    elif strength == 4:
        feedback.append("Your password is strong.")
        rating = "Strong"
    elif strength == 3:
        feedback.append("Your password is moderate. Consider adding more complexity.")
        rating = "Moderate"
    else:
        feedback.append("Your password is weak. Consider improving it by following the recommendations above.")
        rating = "Weak"

    return rating, feedback


def main():
    print("Password Strength Checker")
    while True:
        password = input("Enter a password to check (or type 'exit' to quit): ").strip()
        if password.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        
        rating, feedback = check_password_strength(password)
        print(f"\nPassword Strength: {rating}")
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")
        print("-" * 50)


if __name__ == "__main__":
    main()

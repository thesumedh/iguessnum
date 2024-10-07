import random
import time
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

def print_hacker_style(message, color=Fore.GREEN):
    """Simulate typing effect with colored output and emojis."""
    for char in message:
        print(color + char, end='', flush=True)
        time.sleep(0.05)  # Typing effect
    print()  

def suspense_effect():
    """Simulate suspense by printing dots and creating a pause."""
    for _ in range(3):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print()

def guess_number():
    print_hacker_style("🚀 Welcome to the Number Guessing Game!", Fore.YELLOW)  
    
    input("Step 1: Think of the same number in your mind for yourself and your friend (Don't tell me!). Press Enter when you're ready...")
    
    input("Step 2: Now, ask your friend to think of the same number. Press Enter when you're both ready...")
    
    # Generate random even number under 100 to make calculation easy for the user
    my_number = random.choice(range(2, 100, 2)) 
    print_hacker_style(f"\n[INFO] My number is {my_number}. Now, add this number to the total of your number and your friend's number.", Fore.YELLOW)  # Yellow for info
    
    input("Press Enter when you have done the addition...")
    
    print_hacker_style("[INFO] Now, take the sum of all three numbers and divide it by 2.", Fore.YELLOW)
    input("Press Enter when you're ready to continue...")

    print_hacker_style("[INFO] Now, subtract your friend's number from the result.", Fore.YELLOW)
    input("Press Enter when you've done the subtraction...")

    print_hacker_style("\n[INFO] 🚀 Accessing deeper thoughts...", Fore.GREEN)  
    suspense_effect() 
    print_hacker_style("[HACKING] 🚀 Hacking your Brain ", Fore.RED)  
    suspense_effect()  
    
    print_hacker_style("[SUCCESS] I got access to your brain.", Fore.GREEN) 
    suspense_effect() 
    print_hacker_style("[INFO] 🚀 Analyzing data...", Fore.GREEN)
    
    final_result = my_number // 2
    
    print_hacker_style(f"[RESULT] Data processed: {final_result} retrieved.", Fore.MAGENTA)
    time.sleep(1)

    print_hacker_style(f"👉 [INFO] You were thinking of the number: {final_result}... 🗿", Fore.MAGENTA)

if __name__ == "__main__":
    guess_number()

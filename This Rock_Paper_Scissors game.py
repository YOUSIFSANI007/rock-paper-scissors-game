import random

# List of choices
choices = ["rock", "paper", "scissors"]

# Initialize scores
user_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors!")
print("Type 'exit' to stop playing.")

while True:
    # Get user input
    user_choice = input("\nEnter rock, paper, or scissors: ").lower()
    
    # Exit condition
    if user_choice == "exit":
        break
    
    # Validate input
    if user_choice not in choices:
        print("Invalid choice! Try again.")
        continue
    
    # Computer makes a choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    # Display current score
    print(f"Score -> You: {user_score} | Computer: {computer_score}")

print("\nFinal Score:")
print(f"You: {user_score} | Computer: {computer_score}")
print("Thanks for playing!")

import random
def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the game logic."""
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    return "You lose!"
def main():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break
    print("\nThank you for playing!")
    print(f"Final Score - You: {user_score} | Computer: {computer_score}")
if __name__ == "__main__":
    main()

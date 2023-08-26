def get_player_choice(player_num):
    while True:
        choice = input(f"Player {player_num}, choose Rock, Paper, or Scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")


def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
            (player1_choice == 'paper' and player2_choice == 'rock') or \
            (player1_choice == 'scissors' and player2_choice == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"


def main():
    print("Welcome to the Two-Player Rock, Paper, Scissors Game!")

    play_again = True

    while play_again:
        player1_choice = get_player_choice(1)
        player2_choice = get_player_choice(2)

        print(f"Player 1 chose: {player1_choice}")
        print(f"Player 2 chose: {player2_choice}")

        result = determine_winner(player1_choice, player2_choice)
        print(result)

        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input != 'yes':
            play_again = False
            print("Thanks for playing!")


if __name__ == "__main__":
    main()

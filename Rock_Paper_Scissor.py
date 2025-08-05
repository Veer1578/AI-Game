import random
from colorama import Fore, init, Style

init(autoreset=True)

def rock_paper_scissor():
    print(f"{Fore.CYAN}Welcome to Rock Paper Scissors!")
    game = True
    comp_score = 0
    player_score = 0

    while game:
        print(f"{Fore.CYAN}Choose {Fore.LIGHTBLACK_EX}Rock{Fore.CYAN}, {Fore.WHITE}Paper{Fore.CYAN}, {Fore.RED}Scissors")
        player_choice = input(f"{Fore.LIGHTMAGENTA_EX}You choose: ").lower()
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        print(f"{Fore.CYAN}Computer chooses {computer_choice}")

        if player_choice == 'rock':
            if computer_choice == 'rock':
                print(f"{Fore.YELLOW}It's a tie!")
            elif computer_choice == 'paper':
                print(f"{Fore.RED}Computer wins!")
                comp_score += 1
                print(f"{Fore.CYAN}Computer score: {comp_score}")
                print(f"{Fore.CYAN}Player score: {player_score}")
            else:
                print(f"{Fore.GREEN}You win!")
                player_score += 1
                print(f"{Fore.CYAN}Player score: {player_score}")
                print(f"{Fore.CYAN}Computer score: {comp_score}")
        elif player_choice == 'paper':
            if computer_choice == 'rock':
                print(f"{Fore.GREEN}You win!")
                player_score += 1
                print(f"{Fore.CYAN}Player score: {player_score}")
                print(f"{Fore.CYAN}Computer score: {comp_score}")
                
            elif computer_choice == 'paper':
                print(f"{Fore.YELLOW}It's a tie!")
            else:
                print(f"{Fore.RED}Computer wins!")
                comp_score += 1
                print(f"{Fore.CYAN}Computer score: {comp_score}")
                print(f"{Fore.CYAN}Player score: {player_score}")
        elif player_choice == 'scissors':
            if computer_choice == 'rock':
                print(f"{Fore.RED}Computer wins!")
                comp_score += 1
                print(f"{Fore.CYAN}Computer score: {comp_score}")
                print(f"{Fore.CYAN}Player score: {player_score}")
            elif computer_choice == 'paper':
                print(f"{Fore.GREEN}You win!")
                player_score += 1
                print(f"{Fore.CYAN}Player score: {player_score}")
                print(f"{Fore.CYAN}Computer score: {comp_score}")
            else:
                print(f"{Fore.YELLOW}It's a tie!")
        else:
            print(f"{Fore.LIGHTRED_EX}Invalid input")

        play_again = input(f"{Fore.CYAN}Do you want to play?(y/n) ").lower()
        if play_again == 'y':
            continue
        else:
            print(f"{Fore.CYAN}Final Player score: {player_score}")
            print(f"{Fore.CYAN}Final Computer score: {comp_score}")
            break

if __name__ == "__main__":
    rock_paper_scissor()
    



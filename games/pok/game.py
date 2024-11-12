import sys
from manage.cache import delete_pycaches
from games.pok.pok import Pok
from games.pok.logic import calculate_score, compare_hands


def display_hands(players, dealer):
    # Print all of the players hands including the dealer's
    print("\nCurrent Hands:")
    for player_name, player in players.items():
        print(f"{player_name}: {player.hand}")
    print(f"Dealer: {dealer}")


def main():
    while True:  # Main game loop
        num_players = int(input("Enter the number of players: "))
        game = Pok(num_players)  # Create new game instance
        game.deal_cards()

        while True:  # Individual game round loop
            compared_players = set()  # Single set to track compared/jackpot players
            results = {}
            display_hands(game.players, game.dealer.hand)

            # Check for jackpot hands
            dealer_score_info = calculate_score(game.dealer.hand)
            if dealer_score_info['score'] in [8, 9]:
                print("Dealer has a jackpot hand!")

                # Compare dealer's hand with each player's hand
                for player_name, player in game.players.items():
                    player_score_info = calculate_score(player.hand)
                    if player_score_info['score'] in [8, 9]:
                        print(f"{player_name} has a jackpot hand!")
                    result = compare_hands(player, game.dealer)
                    results[player_name] = result
                    compared_players.add(player_name)  # Add to compared players
                    print(f"Result for {player_name} vs Dealer: {result}")
                break

            for player_name, player in game.players.items():
                player_score_info = calculate_score(player.hand)
                if player_score_info['score'] in [8, 9]:
                    print(f"{player_name} has a jackpot hand!")
                    result = compare_hands(player, game.dealer)
                    results[player_name] = result
                    compared_players.add(player_name)  # Add to compared players
                    print(f"Result for {player_name} vs Dealer: {result}")
                    continue

                print("\nPlay:")
                if player_score_info['score'] < 4:
                    print(f"{player_name}, you must draw a card.")
                    game.draw_card(player_name)
                    display_hands(game.players, game.dealer.hand)
                else:
                    choice = input(
                        f"{player_name}, do you want to draw a card? (y/n): ")
                    if choice.lower() == 'y':
                        game.draw_card(player_name)
                        display_hands(game.players, game.dealer.hand)

            # Dealer's turn
            print("\nCheck Cards:")
            check_players = input(
                "Dealer, do you want to check any player's cards? (y/n): ")
            if check_players.lower() == 'y':
                while True:
                    # Only show players who haven't been compared yet
                    available_players = [
                        p for p in game.players.keys()
                        if p not in compared_players
                    ]
                    if not available_players:
                        print(
                            "\nAll players have been checked or have jackpot hands.")
                        break

                    print("\nAvailable players:", ", ".join(available_players))
                    player_to_check = input(
                        "Which player do you want to check? (Enter player number or 'done'): ")
                    if player_to_check.lower() == 'done':
                        break

                    try:
                        player_num = int(player_to_check)
                        player_name = f"Player {player_num}"
                        if player_name in game.players:
                            result = compare_hands(
                                game.players[player_name], game.dealer)
                            results[player_name] = result
                            print(f"\nChecking {player_name}...")
                            print(f"Result for {
                                  player_name} vs Dealer: {result}")
                        else:
                            print(
                                f"Player {player_num} is not available for checking.")
                    except ValueError:
                        print("Please enter a valid player number or 'done'.")

            # Original dealer draw logic
            print("\nDealer Draws Card:")
            if dealer_score_info['score'] < 4:
                print("Dealer must draw a card.")
                game.draw_card('Dealer')
                display_hands(game.players, game.dealer.hand)
            else:
                choice = input("Dealer, do you want to draw a card? (y/n): ")
                if choice.lower() == 'y':
                    game.draw_card('Dealer')
                    display_hands(game.players, game.dealer.hand)

            # Final comparison of hands
            print("\nResults: ")
            for player_name, player in game.players.items():
                if player_name not in compared_players:
                    result = compare_hands(player, game.dealer)
                    results[player_name] = result
            for player_name, result in results.items():
                print(f"{player_name}: {result}")
            break

        # Ask if they want to play again
        print("\nNew Game:")
        while True:
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() == 'y':
                break
            elif play_again.lower() == 'n':
                print("Thanks for playing!\n")
                delete_pycaches()
                sys.exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()

import sys
from manage.cache import delete_pycaches
from games.pok.pok import Pok, calculate_score, compare_hands


def display_hands(players, dealer):
    print("\n")
    # Print all of the players hands including the dealer's
    print("Current Hands:")
    for player_name, player in players.items():
        print(f"{player_name}: {player.hand}")
    print(f"Dealer: {dealer}")
    print("\n")


def main():
    num_players = int(input("Enter the number of players: "))
    game = Pok(num_players)
    game.deal_cards()

    while True:
        display_hands(game.players, game.dealer.hand)

        # Check for jackpot hands
        dealer_score_info = calculate_score(game.dealer.hand)
        print("Play:")
        if dealer_score_info['score'] in [8, 9]:
            print("Dealer has a jackpot hand!")
            # Compare dealer's hand with each player's hand
            for player_name, player in game.players.items():
                player_score_info = calculate_score(player.hand)
                if player_score_info['score'] in [8, 9]:
                    print(f"{player_name} has a jackpot hand!")
                    # Compare hands
                    result = compare_hands(player.hand, game.dealer.hand)
                    print(f"Result for {player_name} vs Dealer: {result}")
            break

        for player_name, player in game.players.items():
            player_score_info = calculate_score(player.hand)
            if player_score_info['score'] in [8, 9]:
                print(f"{player_name} has a jackpot hand!")
                # Compare player's hand with dealer's hand
                result = compare_hands(player.hand, game.dealer.hand)
                print(f"Result for {player_name} vs Dealer: {result}")
                break

        # Allow players to draw cards if no jackpot hands
        for player_name, player in game.players.items():
            if player_score_info['score'] < 4:
                print(f"{player_name}, you must draw a card.")
                game.draw_card(player_name)
            else:
                choice = input(
                    f"{player_name}, do you want to draw a card? (y/n): ")
                if choice.lower() == 'y':
                    game.draw_card(player_name)

        # Dealer's turn
        if dealer_score_info['score'] < 4:
            print("Dealer must draw a card.")
            game.draw_card('Dealer')
        else:
            choice = input("Dealer, do you want to draw a card? (y/n): ")
            if choice.lower() == 'y':
                game.draw_card('Dealer')

        # Final comparison of hands
        dealer_final_hand = game.dealer.hand
        print("\nResults: ")
        for player_name, player in game.players.items():
            player_final_hand = player.hand
            result = compare_hands(player_final_hand, dealer_final_hand)
            print(f"Result for {player_name}: {result}")

        # Ask if they want to play again
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing!\n")
            # delete_pycaches()
            sys.exit()


if __name__ == "__main__":
    main()

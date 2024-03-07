import random

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
random.shuffle(deck)

def deal_card(deck):
    return deck.pop()

def calculate_total(hand):
    total = sum(card_values[card] for card in hand)
    # Adjust for Aces
    ace_count = hand.count('A')
    while total > 21 and ace_count:
        total -= 10
        ace_count -= 1
    return total

def is_blackjack(hand):
    return sorted(hand) in [['10', 'A'], ['A', '10', 'J'], ['A', '10', 'Q'], ['A', '10', 'K']]

def player_turn(deck, player_hand):
    if calculate_total(player_hand) == 21:
        print("Congratulations! You've got a Blackjack!")
        return True

    while True:
        player_choice = input("Hit or Stand? ").lower()
        if player_choice == 'hit':
            player_hand.append(deal_card(deck))
            total = calculate_total(player_hand)
            print("Your hand:", player_hand, "Total:", total)
            if total > 21:
                print("Bust! You lost.")
                return False
            elif total == 21:
                print("Congratulations! You've got 21!")
                return True
        elif player_choice == 'stand':
            return True

def dealer_turn(deck, dealer_hand):
    while calculate_total(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
    return dealer_hand

def play_blackjack(deck):
    while True:
        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]

        print("Your hand:", player_hand, "Total:", calculate_total(player_hand))
        print("Dealer's hand: [", dealer_hand[0], ", ?]")

        if is_blackjack(player_hand):
            print("Blackjack! You win!")
        else:
            # Player's Turn
            if player_turn(deck, player_hand):
                if calculate_total(player_hand) < 21:
                    dealer_hand = dealer_turn(deck, dealer_hand)
                    print("Dealer's hand:", dealer_hand, "Total:", calculate_total(dealer_hand))

                # Determine Winner
                player_total = calculate_total(player_hand)
                dealer_total = calculate_total(dealer_hand)
                if dealer_total > 21 or player_total > dealer_total:
                    print("You win!")
                elif dealer_total > player_total:
                    print("Dealer wins!")
                else:
                    print("It's a tie!")

        # Check if player wants to play again
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

        # Re-shuffle the deck if it's running low
        if len(deck) < 10:
            deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
            random.shuffle(deck)

    print("Thanks for playing!")

# Start the game
play_blackjack(deck)

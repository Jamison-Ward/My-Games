import random

# getCard

def getCard():
    numbers = (2, 3, 4, 5, 6, 7, 8, 9, 10)
    faces = (11, 12, 13)
    card_value = 0
    card_seed = random.randint(1, 13)
    # print('Card seed:', card_seed)
    if card_seed in numbers:
        card_value = card_seed
        card_type = card_seed
    elif card_seed in faces:
        card_value = 10
        if card_seed == 11:
            card_type = 'Jack'
        elif card_seed == 12:
            card_type = 'Queen'
        elif card_seed == 13:
            card_type = 'King'
    elif card_seed == 1:
        card_type = 'Ace'
        if user_score <= 10 or dealer_score <= 10:
            card_value = 11
        else:
            card_value = 1
    # print('Card value: {}\nCard Score: {}'.format(card_value, card_type))
    return card_value, card_type


# getDealerScore

def getDealerScore():
    dealer_value1, dealer_card1 = getCard()
    dealer_value2, dealer_card2 = getCard()
    print('Dealer card 1: {}\nDealer card 2: {}'.format(dealer_card1, dealer_card2))
    dealer_score = dealer_value1 + dealer_value2
    print('Dealer current score:', dealer_score)
    while dealer_score < 17:
        dealer_valueN, dealer_cardN = getCard()
        print('Dealer card:', dealer_cardN)
        dealer_score += dealer_valueN
        print('Dealer score:', dealer_score)
    return dealer_score


# User Loop

yes = ('y', 'Y', 'yes', 'Yes')
no = ('n', 'N', 'no', 'No')
user_response = 'y'

while user_response in yes:
    user_score = 0
    dealer_score = 0
    print('\nWelcome to the Blackjack table. Dealing you in...\n')
    user_value1, user_card1 = getCard()
    user_value2, user_card2 = getCard()
    print('Card 1: {}\nCard 2: {}'.format(user_card1, user_card2))
    user_score = user_value1 + user_value2
    print('Current score:', user_score, '\n')

    while user_response in yes and user_score < 21:
        user_response = input('Another card? (y/n): ')
        while not user_response in yes and not user_response in no:
            user_response = input('Error: Please enter a valid response (y/n): ')
        if user_response in yes:
            user_valueN, user_cardN = getCard()
            user_score += user_valueN
            print('\nCard value:', user_cardN)
            print('Current score:', user_score, '\n')
        elif user_response in no:
            break

    if user_score > 21:
        print('You busted. Dealer wins.')
    elif user_score == 21:
        print('Wow! 21! You win!')
    else:
        print('\nYour score:', user_score)
        dealer_score = getDealerScore()
        print('Dealer score:', dealer_score, '\n')
        if dealer_score > 21:
            print('Dealer busted. You win!')
        elif user_score <= dealer_score:
            print('Too bad. Dealer wins.')
        elif user_score > dealer_score:
            print('Congratulations! You win!')

    user_response = input('\nWould you like to play again? (y/n): ')
    while not user_response in yes and not user_response in no:
        user_response = input('Error: Please enter a valid response (y/n): ')
    if user_response in yes:
        continue
    elif user_response in no:
        print('\nGoodbye')
        break
